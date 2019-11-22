import yaml
from config.config import conf
import time
from common.api import ApiCall


class GetYaml():

    def __init__(self,casename,other_data = None,headers = None):
        self.casename = casename
        self.other_data = other_data
        self.headers = headers

        f = open(r'../params/Yaml/{}.yml'.format(self.casename))
        self.cases = yaml.safe_load(f)

    def case_select(self,name):
        for case in self.cases:
            if case['name'] == name:
                if self.other_data != None:
                    for i in self.other_data:
                        case['data'][i] = self.other_data[i]
                return self._response(case)

    def _response(self,case):

        param = json_template(case['name'], case['data']).template()

        result = ApiCall(param).api_call(self.headers, case['api'], case['method'])

        response = {
            'result':result,
            'assert_type':case['assert_type'],
            'check':case['check'],
            'datail':case['datail']
        }

        return response


class json_template():
    def __init__(self,name,data):
        self.name = name
        self.data = data
        self.url, self.app_key, self.secret = conf().api_conf()

    def template(self):
        param = {
            "name": self.name,
            "version": "",
            "app_key": self.app_key,
            "data": self.data,
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
            "format": "json"
        }
        return param