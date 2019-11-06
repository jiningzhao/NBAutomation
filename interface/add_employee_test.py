from ..common.login import login
from ..common.another_api import ApiCall
from ..common.json_template import json_template
import pytest
from ..db_fixture.mysql_db import DB


'''
该文件在使用pytest后将被重写
'''


@pytest.fixture()
def name_and_data():
    # name = 'passport.login.security'
    # data = {"account": "18888888888", "password": "a111111", "returnUrl": "", "captcha": ""}
    name = []
    data = []
    value={'passport.login.security':{"account": "18888888888", "password": "a111111", "returnUrl": "", "captcha": ""}}
    for k,v in value.items():
        name.append(k)
        data.append(v)

    return name[0],data[0]

@pytest.fixture()
def Secret_value():
    secret = '123456'
    return secret

@pytest.fixture()
def test_login(Secret_value,name_and_data):
    '''
    此处的name与data取数据库数据【sql】
    :param Secret_value:
    :return:
    '''
    # name1 = "passport.login.security"
    # data1 = {"account": "18888888888", "password": "a111111", "returnUrl": "", "captcha": ""}
    name1,data1 = name_and_data
    param = json_template(name1, data1).template()

    code = login(param, Secret_value).getCode()

    name2 = "passport.userinfo.bycode"
    data2 = {'code': code}
    param1 = json_template(name2, data2).template()

    token = login(param1, Secret_value).getToken()

    token = token

    assert token != None

    yield token


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
