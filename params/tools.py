# import yaml
from ruamel import yaml
from config.config import conf
import time
from common.api import ApiCall
import sys


class GetYaml():

    def __init__(self,casename,other_data = None,headers = None):

        self.casename = casename
        self.other_data = other_data
        self.headers = str(headers)
        f = open(r'../params/Yaml/{}.yml'.format(self.casename),encoding="utf-8")
        self.cases = yaml.safe_load(f)


    def case_select(self,name):
        for case in self.cases:
            if case['name'] == name:
                if self.other_data != None:
                    for i in self.other_data:
                        case['data'][i] = self.other_data[i]
                if str(name)[0:3] == 'old':
                    return self._response_old(case)
                else:
                    return self._response_new(case)

    def _response_old(self,case):

        param = json_template(case['name'],case['data']['param'],self.headers).old_template()

        result = ApiCall(param).api_call(self.headers,case['api'],case['method'])

        if 'DB_table' in case:
            DB_table = case['DB_table']
        else:
            DB_table = None

        response = {
            'result':result,
            'assert_type':case['assert_type'],
            'check':case['check'],
            'datail':case['datail'],
            'DB_table':DB_table
        }

        return response

    def _response_new(self,case):

        param = json_template(case['name'], case['data'],self.headers).template()

        result = ApiCall(param).api_call(self.headers, case['api'], case['method'])

        if 'DB_table' in case:
            DB_table = case['DB_table']
        else:
            DB_table = None

        response = {
            'result':result,
            'assert_type':case['assert_type'],
            'check':case['check'],
            'datail':case['datail'],
            'DB_table':DB_table
        }

        return response


class json_template():
    def __init__(self,name,data,token):
        self.name = name
        self.data = data
        self.token = token
        self.url, self.app_key, self.secret = conf().api_conf()

    def template(self):
        param = {
            "access_token":self.token,
            "name": self.name,
            "version": "",
            "app_key": self.app_key,
            "data": self.data,
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
            "format": "json"
        }

        return param

    def old_template(self):

        param = {
            'token': self.token,
            'param': self.data
        }


        return param