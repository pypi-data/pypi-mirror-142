"""
焕影小程序功能服务端的基本工具函数,以类的形式封装
"""
try:  # 加上这个try的原因在于本地环境和云函数端的import形式有所不同
    from qcloud_cos import CosConfig
    from qcloud_cos import CosS3Client
except ImportError:
    try:
        from qcloud_cos_v5 import CosConfig
        from qcloud_cos_v5 import CosS3Client
    except ImportError:
        raise ImportError("请下载腾讯云COS相关代码包:pip install cos-python-sdk-v5")
import requests
import json
from hyService.error import ProcessError
import os
local_path_ = os.path.dirname(__file__)

class GetConfig(object):
    @staticmethod
    def hy_sdk_client(Id:str, Key:str):
        # 从cos中寻找文件
        REGION: str = 'ap-beijing'
        TOKEN = None
        SCHEME: str = 'https'
        BUCKET: str = 'hy-sdk-config-1305323352'
        client_config = CosConfig(Region=REGION,
                                  SecretId=Id,
                                  SecretKey=Key,
                                  Token=TOKEN,
                                  Scheme=SCHEME)
        return CosS3Client(client_config), BUCKET

    def load_json(self, path:str, default_download=False):
        try:
            if os.path.isdir(path):
                raise ProcessError("请输入具体的配置文件路径,而非文件夹!")
            if default_download is True:
                print(f"\033[34m 默认强制重新下载配置文件...\033[0m")
                raise FileNotFoundError
            with open(path) as f:
                config = json.load(f)
                return config
        except FileNotFoundError:
            dir_name = os.path.dirname(path)
            try:
                os.makedirs(dir_name)
            except FileExistsError:
                pass
            base_name = os.path.basename(path)
            print(f"\033[34m 正在从COS中下载配置文件...\033[0m")
            print(f"\033[31m 请注意,接下来会在{dir_name}路径下生成文件{base_name}...\033[0m")
            Id = input("请输入SecretId:")
            Key = input("请输入SecretKey:")
            client, bucket = self.hy_sdk_client(Id, Key)
            data_bytes = client.get_object(Bucket=bucket,Key=base_name)["Body"].get_raw_stream().read()
            data = json.loads(data_bytes.decode("utf-8"))
            # data["SecretId"] = Id  # 未来可以把这个加上
            # data["SecretKey"] = Key
            with open(path, "w") as f:
                data_str = json.dumps(data, ensure_ascii=False)
                # 如果 ensure_ascii 是 true (即默认值),输出保证将所有输入的非 ASCII 字符转义。
                # 如果 ensure_ascii 是 false，这些字符会原样输出。
                f.write(data_str)
                f.close()
            print(f"\033[32m 配置文件保存成功\033[0m")
            return data
        except json.decoder.JSONDecodeError:
            print(f"\033[31m WARNING: 配置文件为空!\033[0m")
            return {}

    def load_file(self, cloud_path:str, local_path:str):
        """
        从COS中下载文件到本地,本函数将会被默认执行的,在使用的时候建议加一些限制.
        :param cloud_path: 云端的文件路径
        :param local_path: 将云端文件保存在本地的路径
        """
        if os.path.isdir(cloud_path):
            raise ProcessError("请输入具体的云端文件路径,而非文件夹!")
        if os.path.isdir(local_path):
            raise ProcessError("请输入具体的本地文件路径,而非文件夹!")
        dir_name = os.path.dirname(local_path)
        base_name = os.path.basename(local_path)
        try:
            os.makedirs(dir_name)
        except FileExistsError:
            pass
        cloud_name = os.path.basename(cloud_path)
        print(f"\033[31m 请注意,接下来会在{dir_name}路径下生成文件{base_name}\033[0m")
        Id = input("请输入SecretId:")
        Key = input("请输入SecretKey:")
        client, bucket = self.hy_sdk_client(Id, Key)
        print(f"\033[34m 正在从COS中下载文件: {cloud_name}, 此过程可能耗费一些时间...\033[0m")
        data_bytes = client.get_object(Bucket=bucket,Key=cloud_path)["Body"].get_raw_stream().read()
        # data["SecretId"] = Id  # 未来可以把这个加上
        # data["SecretKey"] = Key
        with open(local_path, "wb") as f:
            # 如果 ensure_ascii 是 true (即默认值),输出保证将所有输入的非 ASCII 字符转义。
            # 如果 ensure_ascii 是 false，这些字符会原样输出。
            f.write(data_bytes)
            f.close()
        print(f"\033[32m 文件保存成功\033[0m")

    # def update_config(self, path:str):
    #     if os.path.isdir(path):
    #         raise ProcessError("请输入具体的配置文件路径,而非文件夹!")
    #     base_name = os.path.basename(path)
    #     print(f"\033[34m 正在保存{base_name}到COS中...\033[0m")
    #     try:
    #         with open(path) as f:
    #             data = json.load(f)
    #     except FileNotFoundError:
    #         print(f"\033[31m {path}文件不存在!\033[0m")
    #     try:
    #         Id = data["SecretId"]
    #         Key = data["SecretKey"]
    #     except KeyError:
    #         Id = input("请输入SecretId:")
    #         Key = input("请输入SecretKey:")
    #     client, bucket = self.hy_sdk_client(Id, Key)
    #     a = json.dumps(data)
    #     try:
    #         client.put_object(Bucket=bucket,Body=a,Key=base_name)
    #     except qcloud_cos.cos_exception.CosServiceError:
    #         print(f"\033[31m 本h函数暂时不可用, 云端COS的权限为只可读不可写\033[0m")
    #         print(f"\033[31m 保存失败!\033[0m")
    #     return True

class CosConf(GetConfig):
    """
    从安全的角度出发,将一些默认配置文件上传至COS中,接下来使用COS和它的子类的时候,在第一次使用时需要输入Cuny给的id和key
    用于连接cos存储桶,下载配置文件.
    当然,在service_default_download = False的时候,如果在运行路径下已经有conf/service_config.json文件了,
    那么就不用再次下载了,也不用输入id和key
    事实上这只需要运行一次,因为配置文件将会被下载至源码文件夹中
    如果要自定义路径,请在继承的子类中编写__init__函数,将service_path定向到指定路径
    """
    # 下面这些参数是类的共享参数
    __SECRET_ID:str = None  # 服务的id
    __SECRET_KEY:str = None  # 服务的key
    __REGION: str = None  # 服务的存储桶地区
    __TOKEN:str = None  # 服务的token,目前一直是None
    __SCHEME:str = None  # 服务的访问协议,默认实际上是https
    __BUCKET:str = None  # 服务的存储桶
    __SERVICE_CONFIG:dict = None  # 服务的配置文件
    service_path:str = f"{local_path_}/conf/service_config.json"  #配置文件路径,默认是函数运行的路径下的conf文件夹
    service_default_download = False  # 是否在每次访问配置的时候都重新下载文件
    @property
    def service_config(self):
        if self.__SERVICE_CONFIG is None or self.service_default_download is True:
            self.__SERVICE_CONFIG = self.load_json(self.service_path, self.service_default_download)
        return self.__SERVICE_CONFIG

    @property
    def client(self):
        client_config = CosConfig(Region=self.region,
                                  SecretId=self.secret_id,
                                  SecretKey=self.secret_key,
                                  Token=self.token,
                                  Scheme=self.scheme)
        return CosS3Client(client_config)

    def get_key(self, key:str):
        try:
            data = self.service_config[key]
            if data == "None":
                return None
            else:
                return data
        except KeyError:
            print(f"\033[31m没有对应键值{key},默认返回None\033[0m")
            return None

    @property
    def secret_id(self):
        if self.__SECRET_ID is None:
            self.__SECRET_ID = self.get_key("SECRET_ID")
        return self.__SECRET_ID

    @secret_id.setter
    def secret_id(self, value:str):
        self.__SECRET_ID = value

    @property
    def secret_key(self):
        if self.__SECRET_KEY is None:
            self.__SECRET_KEY = self.get_key("SECRET_KEY")
        return self.__SECRET_KEY

    @secret_key.setter
    def secret_key(self, value:str):
        self.__SECRET_KEY = value

    @property
    def region(self):
        if self.__REGION is None:
            self.__REGION = self.get_key("REGION")
        return self.__REGION

    @region.setter
    def region(self, value:str):
        self.__REGION = value

    @property
    def token(self):
        # if self.__TOKEN is None:
        #     self.__TOKEN = self.get_key("TOKEN")
        # 这里可以注释掉
        return self.__TOKEN

    @token.setter
    def token(self, value:str):
        self.__TOKEN= value

    @property
    def scheme(self):
        if self.__SCHEME is None:
            self.__SCHEME = self.get_key("SCHEME")
        return self.__SCHEME

    @scheme.setter
    def scheme(self, value:str):
        self.__SCHEME = value

    @property
    def bucket(self):
        if self.__BUCKET is None:
            self.__BUCKET = self.get_key("BUCKET")
        return self.__BUCKET

    @bucket.setter
    def bucket(self, value):
        self.__BUCKET = value

    def downloadFile_COS(self, key, bucket:str=None, if_read:bool=False):
        """
        从COS下载对象(二进制数据), 如果下载失败就返回None
        """
        CosBucket = self.bucket if bucket is None else bucket
        try:
            # 将本类的Debug继承给抛弃了
            # self.debug_print(f"Download from {CosBucket}", font_color="blue")
            obj = self.client.get_object(
                Bucket=CosBucket,
                Key=key
            )
            if if_read is True:
                data = obj["Body"].get_raw_stream().read()  # byte
                return data
            else:
                return obj
        except Exception as e:
            print(f"\033[31m下载失败! 错误描述:{e}\033[0m")
            return None

    def showFileList_COS_base(self, key, bucket, marker:str=""):
        """
        返回cos存储桶内部的某个文件夹的内部名称
        :param key: cos云端的存储路径
        :param bucket: cos存储桶名称，如果没指定名称（None）就会寻找默认的存储桶
        :param marker: 标记,用于记录上次查询到哪里了
        ps:如果需要修改默认的存储桶配置，请在代码运行的时候加入代码 s.bucket = 存储桶名称 （s是对象实例）
        返回的内容存储在response["Content"]，不过返回的数据大小是有限制的，具体内容还是请看官方文档。
        """
        response = self.client.list_objects(
            Bucket=bucket,
            Prefix=key,
            Marker=marker
        )
        return response

    def showFileList_COS(self, key, bucket:str=None)->list:
        """
        实现查询存储桶中所有对象的操作，因为cos的sdk有返回数据包大小的限制，所以我们需要进行一定的改动
        """
        marker = ""
        file_list = []
        CosBucket = self.bucket if bucket is None else bucket
        while True:  # 轮询
            response = self.showFileList_COS_base(key, CosBucket, marker)
            try:
                file_list.extend(response["Contents"])
            except KeyError:
                pass
            if response['IsTruncated'] == 'false':  # 接下来没有数据了,就退出
                break
            file_list.extend(response["Contents"])
            marker = response['NextMarker']
        return file_list

    def uploadFile_COS(self, buffer, key, bucket:str=None):
        """
        从COS上传数据,需要注意的是必须得是二进制文件
        """
        CosBucket = self.bucket if bucket is None else bucket
        try:
            self.client.put_object(
                Bucket=CosBucket,
                Body=buffer,
                Key=key
            )
            return True
        except Exception as e:
            print(e)
            return False

class ResponseWebSocket(CosConf):
    # 网关推送地址
    __HOST:str = None
    @property
    def sendBackHost(self):
        if self.__HOST is None:
            self.__HOST = self.get_key("HOST")
        return self.__HOST

    @sendBackHost.setter
    def sendBackHost(self, value):
        self.__HOST = value

    def sendMsg_toWebSocket(self, message,connectionID:str = None):
        if connectionID is not None:
            retmsg = {'websocket': {}}
            retmsg['websocket']['action'] = "data send"
            retmsg['websocket']['secConnectionID'] = connectionID
            retmsg['websocket']['dataType'] = 'text'
            retmsg['websocket']['data'] = json.dumps(message)
            requests.post(self.sendBackHost, json=retmsg)
            print("send success!")
        else:
            pass

    @staticmethod
    def create_Msg(status, msg):
        """
        本方法用于创建一个用于发送到WebSocket客户端的数据
        输入的信息部分,需要有如下几个参数:
        1. id,固定为"return-result"
        2. status,如果输入为1则status=true, 如果输入为-1则status=false
        3. obj_key, 图片的云端路径, 这是输入的msg本身自带的
        """
        msg['status'] = "false" if status == -1 else 'true'  # 其实最好还是用bool
        msg['id'] = "async-back-msg"
        msg['type'] = "funcType"
        msg["format"] = "imageType"
        return msg

# 功能服务类
class Service(ResponseWebSocket):
    """
    服务的主函数,封装了cos上传\下载功能以及与api网关的一键通讯
    将类的实例变成一个可被调用的对象,在服务运行的时候,只需要运行该对象即可
    当然,因为是类,所以支持继承和修改
    """

    def process(self, *args, **kwargs):
        """
        处理函数,在使用的时候请将之重构
        """
        pass

    def __call__(self, *args, **kwargs):
        """
        调用函数，下面的调用函数实际上是一个模板，后续是可以重写的
        *args, **kwargs用于方便继承时候的拓展
        下列模板仅仅是一种服务的使用方式：
        前端传入特定格式的信息，本方法通过前端信息下载cos图片
        根据下载的图片“直接”输入到process()方法中，得到结果图片，然后再上传至cos
        根据前端的信息格式，本模板自动判定是否需要回传消息（但是无论是否回传，消息都在代码执行的时候被生成了）
        实际上“判定”的工作被封装在sendMsg_toWebSocket方法中，如果connectionID为None（即前端信息中没有单独的connectionID），
        就不发送数据。
        """
        # msg = kwargs["msg"]
        # # print("GET", msg)
        # back_msg = {}  # 回传消息
        # connectionID = None
        # try:
        #     # 初始化一些数据
        #     send_msg: dict = msg["send_msg"]  # 获得cos数据字典
        #     download_path: str = send_msg["obj_key"]  # 获得cos下载路径
        #     upload_path = download_path.replace("old-image", "new-image")  # 获得cos上传路径
        #     back_msg["time"] = send_msg["time"]  # 时间戳
        #     back_msg["uid"] = send_msg["uid"]  # 用户id
        #     back_msg["hd_key"] = upload_path  # 回传云端结果图片路径
        #     connectionID = msg["connectionID"] if "connectionID" in msg.keys() else None  # 获得长连接id
        #     # 开始处理
        #     print("start...")
        #     resp = self.downloadFile_COS(download_path, if_read=False)  # 下载图片
        #     image_byte = resp['Body'].get_raw_stream().read()  # 读取二进制图片
        #     image_pre = self.byte_cv2(image_byte, flags=cv2.IMREAD_COLOR)  # 将二进制图片转为cv2格式
        #     # 数据图片下载完毕，开始功能处理
        #     print("processing...")
        #     image = self.process(image_pre)
        #     image_byte = self.cv2_byte(image, imageType=".jpg")  # 将处理完毕的图片转为二进制格式
        #     self.uploadFile_COS(buffer=image_byte, key=upload_path)  # 将字节流图片上传至cos
        #     back_msg = self.create_Msg(status=1, msg=back_msg)  # 处理成功,在回传消息中添加成功的消息
        #     print("success!")
        # except Exception as e:
        #     # 处理失败
        #     print(e)
        #     back_msg = self.create_Msg(status=-1, msg=back_msg)  # 给WebSocket返回一个处理失败的消息
        #     print("fail!")
        # self.sendMsg_toWebSocket(message=back_msg, connectionID=connectionID)  # 向websocket返回消息
        pass

# 焕影服务的日志函数
class Diary(CosConf):
    """
    焕影服务的日志函数,继承自CosConf配置类,存储桶路径发生了一些改变.
    对于配置文件,如果要自定义路径,请在继承的子类中编写__init__函数,将service_path定向到指定路径
    """
    def __init__(self):
        self.bucket = "hy-hcy-data-logs-1306602019"  # 默认bucket为hy-hcy-data-logs-1306602019, 也可以在初始化以后手动设置
        self.__upPath:str = ""  # 上传文件的路径
        self.__diaryName:str = ""  # 日志文件的名称
        self.__msg:dict = {}

    @property
    def upPath(self) -> str:
        return self.__upPath

    @upPath.setter
    def upPath(self, value):
        # 传入的是一个列表或者单个元素, upPath=upPath + "/" + x
        if isinstance(value, list):
            for x in value:
                self.__upPath = f"{self.__upPath}/{x}" if len(self.__upPath) != 0 else f"{x}"
        else:
            self.__upPath = f"{self.__upPath}/{value}" if len(self.__upPath) != 0 else f"{value}"

    @upPath.deleter
    def upPath(self):
        self.__upPath = ""

    @property
    def diaryName(self) -> str:
        return self.__diaryName

    @diaryName.setter
    def diaryName(self, value):
        # 传入的是一个列表或者单个元素, diaryName=diaryName + "_" + x
        if isinstance(value, list):
            for x in value:
                self.__diaryName = f"{self.__diaryName}/{x}" if len(self.__diaryName) != 0 else f"{x}"
        else:
            self.__diaryName = f"{self.__diaryName}/{value}" if len(self.__diaryName) != 0 else f"{value}"

    @diaryName.deleter
    def diaryName(self):
        self.__diaryName = ""

    @property
    def msg(self) -> dict:
        return self.__msg

    @msg.setter
    def msg(self, value):
        if isinstance(value, dict):
            self.__msg.update(value)
        else:
            raise TypeError("必须输入字典类型参数!")

    @msg.deleter
    def msg(self):
        self.__msg = {}

    def upload2COS(self):
        if not len(self.upPath) * len(self.diaryName):
            raise ProcessError("日志的上传路径和名称不能为空!")
        try:
            self.client.put_object(
                Bucket=self.bucket,
                Body=json.dumps(self.__msg).encode(),
                Key=f"{self.upPath}/{self.diaryName}"
            )
            return True
        except Exception as e:
            print(e)
            return False




if __name__ == "__main__":
    # a = sys.modules["CV2Bytes"]
    d = Diary()
    d.upPath = "test"
    d.diaryName = "test"
    print(d.upPath)
    print(d.diaryName)
    d.upload2COS()
