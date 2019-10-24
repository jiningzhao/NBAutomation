import unittest
from login import login
from json_template import json_template


class WbsTest(unittest.TestCase):

    # def __init__(self,secret):
    #     self.secret = secret

    def setUp(self):

        pass

    def tearDown(self):
        pass

    def test_login(self):
        name = "passport.login.security"
        data = {"account": "18888888888", "password": "a111111", "returnUrl": "", "captcha": ""}

        param = json_template(name, data).template()

        a = login(param, secret = "123456")
        b = a.getCode()

        name = "passport.userinfo.bycode"
        data = {'code': b}
        param1 = json_template(name, data).template()

        c = login(param1, secret = "123456")
        d = c.getToken()

        self.assertIsNotNone(d,msg="登录成功")

    def test_get_employeesList(self):
        pass

