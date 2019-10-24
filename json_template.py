'''
开发者：赵吉宁
脚本功能：入参模板
时间：2019-10-24
'''

import time
class json_template():
    def __init__(self,name,data):
        self.name = name
        self.data = data

    def template(self):
        param = {
            "name": self.name,
            "version": "",
            "app_key": "test",
            "data": self.data,
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
            "format": "json"
        }
        return param
