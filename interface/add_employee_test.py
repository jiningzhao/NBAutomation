# import pytest
# from ..params.param_template import json_template
# from ..common.api import ApiCall
# from ..params.tools import GetYaml
# from ..common.Assert import Assert
import pytest
from params.tools import GetYaml
from common.Assert import Assert


class Test_Add_Empolyee_Process():

    @pytest.fixture()
    def test_login(self):

        name = 'passport.login.security'

        response = GetYaml('add_employee_test').case_select(name)

        code = str(response['result']['value']).split('code=')[-1]

        Assert(response['assert_type'],code,response['check'],response['datail'])

        return code

    @pytest.fixture()
    def test_getToken(self,test_login):


        name = 'passport.userinfo.bycode'

        other_data = {'code':test_login}

        response = GetYaml('add_employee_test',other_data=other_data).case_select(name)

        token = response['result']['value']['token']

        Assert(response['assert_type'], token, response['check'], response['datail'])

        return token


    def test_add_employee(self,test_getToken,random_name,random_mobile,random_ID):

        name = 'passport.employee.add'

        other_data = {'mobile':random_mobile,'name':random_name,'documentNo':random_ID}

        response = GetYaml('add_employee_test',other_data=other_data,headers=test_getToken).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])




if __name__ == '__main__':
    # pytest.main(['-v','--setup-show'])
    pytest.main(['-v','-s'])
    # pytest.main(['--collect-only'])
    # pytest.main(['--html=../report/report3.html'])
