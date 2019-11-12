import pytest
from ..common.login import login
from ..params.param_template import json_template
from ..common.api import ApiCall
from ..params.tools import GetYaml
from ..config.config import conf
from ..common.Assert import Assert
'''
该文件在使用pytest后将被重写
'''
url,app_key,secret = conf().api_conf()


@pytest.fixture()
def test_login():

    '''
    此处的name与data取数据库数据【sql】
    :param Secret_value:
    :return:
    '''
    name = 'passport.login.security'

    case = GetYaml().case_select(name)
    data = case['data']
    check = case['check']
    method = case['method']
    api = case['api']
    datail = case['datail']
    param = json_template(name,data).template()
    # code = login(param, secret).getCode(method)

    code = str(ApiCall(param, secret).api_call(None,api,method)['value']).split('code=')[-1]

    # assert code != 'None'
    Assert().notEqual(code,check,datail)
    return code

@pytest.fixture()
def test_getToken(test_login):


    name = 'passport.userinfo.bycode'
    case = GetYaml().case_select(name)
    data = case['data']
    check = case['check']
    method = case['method']
    api = case['api']
    datail = case['datail']
    data['code'] = test_login
    param = json_template(name, data).template()
    # token = login(param, secret).getToken(method)
    token = ApiCall(param, secret).api_call(None,api,method)['value']['token']

    Assert().notEqual(token,check,datail)
    assert token != None

    return token


def test_add_employee(test_getToken):

    name = 'passport.employee.add'
    case = GetYaml().case_select(name)
    data = case['data']
    check = case['check']
    method = case['method']
    api =case['api']
    datail =case['datail']

    param = json_template(name, data).template()
    result = ApiCall(param, secret).api_call(test_getToken,api,method)

    Assert().equal(result['code'],check,datail)