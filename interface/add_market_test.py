import pytest
from ..login import login,ApiCall
from ..json_template import json_template

secret = "123456"
name = "passport.login.security"
data = {"account": "18888888888", "password": "a111111", "returnUrl": "", "captcha": ""}

param = json_template(name, data).template()

code = login(param, secret).getCode()

name = "passport.userinfo.bycode"
data = {'code': code}
param1 = json_template(name, data).template()

token = login(param1, secret).getToken()

def test_login():
    # self.assertIsNotNone(token, msg="登录成功")
    assert token != None , "不存在Token！"
    return token


def test_get_employeesList():
    '''
       查询客户列表接口
    '''
    name = "passport.role.search"
    data = {"start": 0, "limit": 100}
    param2 = json_template(name, data).template()

    result = ApiCall(param2, secret).api_call(token)

    # self.assertEqual(0, result['code'], msg=result['msg'])
    assert result['code'] == 0 , result['msg']

def test_add_employee():
    '''
        添加员工接口
    '''
    name = "passport.employee.add"
    data = {"gender": "0",
            "deptIds": [1],
            "defaultDept": "",
            "documentType": "2",
            "joinDate": "2019-10-01",
            "roleIds": [],
            "education": "2",
            "married": "",
            "employeeNo": "",
            "positionId": 42, "name": "赵吉宁",
            "documentNo": "133124152346134",
            "mobile": "10900000009",
            "managers": [1],
            "email": ""}
    param2 = json_template(name, data).template()

    result = ApiCall(param2, secret).api_call(token)

    # self.assertEqual(0, result['code'], msg=result['msg'])
    assert result['code'] == 0 , result['msg']