import json_template
from login import login
import unittest
from interface_test import WbsTest


if __name__ == "__main__":
    secret = "123456"

    suite = unittest.TestSuite()
    # WbsTest().test_login(secret)
    suite.addTests(unittest.makeSuite(WbsTest))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # name = "passport.login.security"
    # data = {"account":"18888888888","password":"a111111","returnUrl":"","captcha":""}
    #
    # param = json_template.json_template(name,data).template()
    #
    # a = login(param,secret)
    # b = a.getCode()
    #
    #
    # name = "passport.userinfo.bycode"
    # data = {'code':b}
    # param1 = json_template.json_template(name, data).template()
    #
    # c = login(param1,secret)
    # d = c.getToken()

    # name = "csc.customer.customerIdAuth"
    # data = {}
    # param2 = json_template.json_template(name, data).template()
    #
    #
    # e = login(param2,secret)
    # f = e.api_call(d)