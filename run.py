import json_template
from login import login
import HTMLTestRunner
import unittest
from interface_test import WbsTest,parameter
import os
import time


if __name__ == "__main__":
    secret = "123456"
    now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
    # 创建测试用例集
    suite = unittest.TestSuite()

    # 往测试用例集添加测试用例
    suite.addTests(parameter.parametrize(WbsTest,secret))

    # 设定测试报告文件地址
    report_path = os.path.join(os.getcwd(),'report')
    # 设定测试报告文件名称
    report_abspath = os.path.join(report_path,"result_"+now+".html")
    fp = open(report_abspath,"wb")

    # 运行测试并生成测试报告
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"接口自动化用例测试报告：",
                                           description=u"用例执行情况：")
    runner.run(suite)
    fp.close()