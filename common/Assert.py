'''
封装断言
'''
class Assert():
    def __init__(self,assert_type,real,expect,datail):
        if assert_type == 'equal':
            self.equal(real,expect,datail)
        elif assert_type == 'notEqual':
            self.notEqual(real, expect, datail)



    def equal(self,real,expect,datail):

        assert expect == real,datail



    def notEqual(self,real,expect,datail):

        assert expect != real,datail


