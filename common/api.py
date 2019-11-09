
'''
开发者：赵吉宁
脚本功能：接口登录
时间：2019-10-23
'''
# encoding: utf-8

import requests
from ..common.login import login

class ApiCall(login):

    # 将token值传入请求头，实现接口的调用
    def api_call(self,token):
        '''
        接口名取数据【sql】
        :param token:
        :return:
        '''

        response = requests.get("https://service-wbs310.newtamp.cn/{}/api".format(self.param['name'].split(".")[0]),params = self.param,headers = {"token":token})
        result = response.json()
        # print("Preview:",result)
        return result