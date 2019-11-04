import unittest
from ..login import login,ApiCall
from ..json_template import json_template
import pytest
from ..db_fixture.mysql_db import DB


'''
该文件在使用pytest后将被重写
'''

# class parameter(unittest.TestCase):
#
#     def __init__(self,methodName = 'runTest',secret = None):
#
#         super(parameter, self).__init__(methodName)
#         self.secret = secret
#
#     @staticmethod
#     def parametrize(testcase_klass, secret = None):
#         """
#         创建一个包含来自给定子类的所有测试的套件，并将参数'secret'传递给它们。【sql】
#         """
#         testloader = unittest.TestLoader()
#         testnames = testloader.getTestCaseNames(testcase_klass)
#         suite = unittest.TestSuite()
#
#         for name in testnames:
#
#             suite.addTest(testcase_klass(name, secret = secret))
#
#         return suite
#
#
# class WbsTest(parameter):
#
#     def setUp(self):
#         '''
#         name要取数据库中的name值，data要取数据库中的data【sql】
#         :return:
#         '''
#
#         name = "passport.login.security"
#         data = {"account": "18888888888", "password": "a111111", "returnUrl": "", "captcha": ""}
#
#         param = json_template(name, data).template()
#
#         code = login(param, self.secret).getCode()
#
#         name = "passport.userinfo.bycode"
#         data = {'code': code}
#         param1 = json_template(name, data).template()
#
#         token = login(param1, self.secret).getToken()
#
#         self.token = token
#
#
#         self.data=DB().select('select * from case1')
#
#
#
#     def tearDown(self):
#         pass
#
#     def test_login(self):
#
#         self.assertIsNotNone(self.token,msg="token为空，登录失败！")
#
#         return self.token
#
#     def test_get_employeesList(self):
#         '''
#            查询客户列表接口
#         '''
#         name = "passport.role.search"
#         data = {"start":0,"limit":100}
#         param2 = json_template(name, data).template()
#
#         result = ApiCall(param2,self.secret).api_call(self.token)
#
#         self.assertEqual(0, result['code'], msg=result['msg'])
#
#
#     def test_add_employee(self):
#         '''
#             添加员工接口
#         '''
#         name = "passport.employee.add"
#         data = {"gender":"0",
#                 "deptIds":[1],
#                 "defaultDept":"",
#                 "documentType":"2",
#                 "joinDate":"2019-10-01",
#                 "roleIds":[],
#                 "education":"2",
#                 "married":"",
#                 "employeeNo":"",
#                 "positionId":42,"name":"赵吉宁",
#                 "documentNo":"1331241523461412312",
#                 "mobile":"13123456789",
#                 "managers":[1],
#                 "email":""}
#         param2 = json_template(name, self.data).template()
#
#         result = ApiCall(param2,self.secret).api_call(self.token)
#
#         self.assertEqual(0,result['code'],msg=result['msg'])
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
    # data3 = DB().select('select * from case1')
    data3={"gender": "0",
     "deptIds": [1],
     "defaultDept": "",
     "documentType": "2",
     "joinDate": "2019-10-01",
     "roleIds": [],
     "education": "2",
     "married": "",
     "employeeNo": "",
     "positionId": 42, "name": "赵吉宁",
     "documentNo": "13312345234614124",
     "mobile": "15100000001",
     "managers": [1],
     "email": ""}
    param2 = json_template(name3, data3).template()

    result = ApiCall(param2, Secret_value).api_call(test_login)

    assert result['code'] == 0 , result['msg']
