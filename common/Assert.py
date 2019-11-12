'''
封装断言
'''
class Assert():

    def equal(self,real,expect,datail):

        assert expect == real,datail



    def notEqual(self,real,expect,datail):

        assert expect != real,datail


