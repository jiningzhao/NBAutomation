'''
封装断言
'''
class Assert():
    def __init__(self,assert_type,real,expect,datail):
        if assert_type == 'equal':
            self.equal(real,expect,datail)
        elif assert_type == 'notEqual':
            self.notEqual(real, expect, datail)
        elif assert_type == 'IN':
            self.IN(real, expect, datail)
        elif assert_type == 'notIN':
            self.not_IN(real, expect, datail)
        elif assert_type == 'cover':
            self.cover(real, expect, datail)
        elif assert_type == 'notCover':
            self.not_Cover(real, expect, datail)
        else:
            self.error(assert_type)


    def equal(self,real,expect,datail):

        assert expect == real,datail

    def notEqual(self,real,expect,datail):

        assert expect != real,datail

    def IN(self,real,expect,datail):

        assert real in expect,datail

    def not_IN(self,real,expect,datail):

        assert real not in expect,datail

    def cover(self,real,expect,datail):

        assert expect in real, datail

    def not_Cover(self,real,expect,datail):

        assert expect not in real,datail

    def error(self,assert_type):

        assert 1 == 0,"没有匹配到断言类型【{}】，请联系管理员添加，或更换断言类型！".format(assert_type)