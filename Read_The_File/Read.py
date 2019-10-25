import pandas as pd

data = pd.read_excel("/Users/bh/Desktop/icon.csv",names=['name','value'])

a= list(data.get('name'))
b = list(data.get('value'))

k = dict(zip(a,b))


print(k)