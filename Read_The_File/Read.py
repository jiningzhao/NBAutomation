import pandas as pd

'''
接口自动化测试用例写在excel表格中
脚本实现读取excel表格数据并格式化为字典形式
把数据存储到数据库中
'''

data = pd.read_excel("/Users/bh/Desktop/icon.csv",names=['name','value'])

a= list(data.get('name'))
b = list(data.get('value'))

k = dict(zip(a,b))


print(k)