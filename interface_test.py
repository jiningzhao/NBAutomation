import unittest
from login import login,ApiCall
from json_template import json_template

class parameter(unittest.TestCase):

    def __init__(self,methodName = 'runTest',secret = None):

        super(parameter, self).__init__(methodName)
        self.secret = secret

    @staticmethod
    def parametrize(testcase_klass, secret = None):
        """
        创建一个包含来自给定子类的所有测试的套件，并将参数'secret'传递给它们。
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()

        for name in testnames:

            suite.addTest(testcase_klass(name, secret = secret))

        return suite

class WbsTest(parameter):

    def setUp(self):
        name = "passport.login.security"
        data = {"account": "18888888888", "password": "a111111", "returnUrl": "", "captcha": ""}

        param = json_template(name, data).template()

        code = login(param, self.secret).getCode()

        name = "passport.userinfo.bycode"
        data = {'code': code}
        param1 = json_template(name, data).template()

        token = login(param1, self.secret).getToken()

        self.token = token

    def tearDown(self):
        pass

    def test_login(self):

        self.assertIsNotNone(self.token,msg="登录成功")

        return self.token

    def test_get_employeesList(self):

        name = "csc.customer.customerIdAuth"
        data = {}
        param2 = json_template(name, data).template()

        result = ApiCall(param2,self.secret).api_call(self.token)

        self.assertEqual(0,result,msg="csc.customer.customerIdAuth")

