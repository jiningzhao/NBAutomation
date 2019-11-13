# import pytest
# from ..params.param_template import json_template
# from ..common.api import ApiCall
# from ..params.tools import GetYaml
# from ..common.Assert import Assert
import pytest
from params.param_template import json_template
from common.api import ApiCall
from params.tools import GetYaml
from common.Assert import Assert
'''
该文件在使用pytest后将被重写
'''

class Test_Add_Empolyee_Process():

    @pytest.fixture()
    def test_login(self):

        '''
        此处的name与data取数据库数据【sql】
        :param Secret_value:
        :return:
        '''
        name = 'passport.login.security'

        case = GetYaml('add_employee_test').case_select(name)
        data = case['data']
        check = case['check']
        method = case['method']
        api = case['api']
        datail = case['datail']
        param = json_template(name,data).template()
        # code = login(param, secret).getCode(method)

        code = str(ApiCall(param).api_call(None,api,method)['value']).split('code=')[-1]

        # assert code != 'None'
        Assert().notEqual(code,check,datail)
        return code

    @pytest.fixture()
    def test_getToken(self,test_login):


        name = 'passport.userinfo.bycode'
        '''
        GetYaml传测试用例文件名
        '''

        case = GetYaml('add_employee_test').case_select(name)
        data = case['data']
        check = case['check']
        method = case['method']
        api = case['api']
        datail = case['datail']

        data['code'] = test_login
        param = json_template(name, data).template()
        # token = login(param, secret).getToken(method)
        token = ApiCall(param).api_call(None,api,method)['value']['token']

        Assert().notEqual(token,check,datail)
        assert token != None

        return token


    def test_add_employee(self,test_getToken):

        name = 'passport.employee.add'
        case = GetYaml('add_employee_test').case_select(name)
        data = case['data']
        check = case['check']
        method = case['method']
        api =case['api']
        datail =case['datail']

        param = json_template(name, data).template()
        result = ApiCall(param).api_call(test_getToken,api,method)

        Assert().equal(result['code'],check,datail)


if __name__ == '__main__':
    # pytest.main(['-v','--setup-show'])
    pytest.main(['--html=report3.html'])
