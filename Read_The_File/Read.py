import pandas as pd
import xmind
from xmind2testcase.utils import xmind_testcase_to_json_file
from xmind2testcase.utils import xmind_testsuite_to_json_file
from xmind2testcase.utils import get_xmind_testcase_list

'''
接口自动化测试用例写在excel表格中
脚本实现读取excel表格数据并格式化为字典形式
把数据存储到数据库中
'''

# data = pd.read_excel("/Users/bh/Desktop/icon.csv",names=['name','value'])
#
# a= list(data.get('name'))
# b = list(data.get('value'))
#
# k = dict(zip(a,b))
#
#
# print(k)




def main():
    xmind_file = '/Users/bh/Desktop/Xmind文件/3.1.0-银行频道/银行频道.xmind'
    testcases = get_xmind_testcase_list(xmind_file)
    print(testcases)

main()