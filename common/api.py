
'''
开发者：赵吉宁
脚本功能：接口登录
时间：2019-10-23
'''
# encoding: utf-8

import requests
from ..config.config import conf
from ..common.login import login
from ..params.tools import GetYaml


class ApiCall(login):

    # 将token值传入请求头，实现接口的调用
    def api_call(self,token,api,method='get'):
        '''
        接口名取数据【sql】
        :param token:
        :return:
        '''
        url,app_key,secret = conf().api_conf()
        header = {"token": token}
        if token == None:
            header = None


        if method == 'post':

            response = requests.post(url + api, params=self.param, headers=header)

        else:
            response = requests.get(url+api,params = self.param,headers = header)


        result = response.json()

        return result