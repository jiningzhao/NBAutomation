import HTMLTestRunner
import unittest
from interface.add_employee_test import WbsTest,parameter
import os
import time


'''
secret要从数据库中取
'''
secret = "123456"

now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))


'''
测试用例集的问题在使用pytest之后会被取代
'''
# 创建测试用例集
suite = unittest.TestSuite()

# 往测试用例集添加测试用例
suite.addTests(parameter.parametrize(WbsTest,secret))

# 设定测试报告文件地址
report_path = os.path.join(os.getcwd(),'report')

# 设定测试报告文件名称
report_abspath = os.path.join(report_path,"result_"+now+".html")

# 打开文件
fp = open(report_abspath,"wb")


if __name__ == "__main__":

    # 运行测试并生成测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"接口自动化用例测试报告：",
                                           description=u"用例执行情况：")
    runner.run(suite)

    # 关闭文件
    fp.close()