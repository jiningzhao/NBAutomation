from ..common.login import login
from ..DB_fixture.param_template import json_template
import pytest
from ..DB_fixture.data_template import data_template
from ..DB_fixture.mysql_db import DB
from ..common.api import ApiCall

'''
该文件在使用pytest后将被重写
'''


@pytest.fixture()
def name_and_data():

    name1 = 'passport.login.security'
    data1 = data_template().passport_login_security('18888888888', 'a111111')

    return name1,data1

@pytest.fixture()
def param(name_and_data):

    name1,data1 = name_and_data
    param = json_template(name1, data1).template()

    return param

@pytest.fixture()
def Secret_value():

    secret = '123456'

    return secret

@pytest.fixture()
def test_login(Secret_value,param):
    '''
    此处的name与data取数据库数据【sql】
    :param Secret_value:
    :return:
    '''

    code = login(param, Secret_value).getCode()

    assert code != 'None'

    name2 = "passport.userinfo.bycode"
    data2 = data_template().passport_userinfo_bycode(code)
    param1 = json_template(name2, data2).template()
    token = login(param1, Secret_value).getToken()


    assert token != None

    return token


def test_add_employee(test_login,Secret_value):
    '''
    此处的name与data取数据库数据【sql】
    :param test_login:
    :param Secret_value:
    :return:
    '''
    name3 = "passport.employee.add"
    data3 = DB().select('select * from case1')

    param2 = json_template(name3, data3).template()

    result = ApiCall(param2, Secret_value).api_call(test_login)

    assert result['code'] == 0 , result['msg']
