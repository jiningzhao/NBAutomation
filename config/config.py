import os
import configparser as cparser

# 定位当前脚本所在位置的上级
base_dir = str(os.path.dirname(__file__))
# 对文件路径进行格式处理
base_dir = base_dir.replace("\\","/")
# 定位到api_config.ini文件
file_path = base_dir + "/api_config.ini"

# ConfigParser功能——读取写入配置文件
cf = cparser.ConfigParser()
# read(filename)——直接读取文件内容
cf.read(file_path)

class conf():
    def api_conf(self):
        url = cf.get("url","url")
        api = cf.get("url",'api_1')

        return url,api

    def login_conf(self):
        url = cf.get("url","url")
        api = cf.get("url","api_1")

        return url,api