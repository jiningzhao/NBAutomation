'''
封装断言
'''
from DB_fixture.mysql_db import DB
class Assert():
    def __init__(self,assert_type,real,expect,datail = None,DB_table = None):
        if assert_type == 'equal':
            self.equal(real,expect,datail)
        elif assert_type == 'notEqual':
            self.notEqual(real, expect, datail)
        elif assert_type == 'IN':
            self.IN(real, expect, datail,DB_table)
        elif assert_type == 'notIN':
            self.not_IN(real, expect, datail,DB_table)
        elif assert_type == 'cover':
            self.cover(real, expect, datail)
        elif assert_type == 'notCover':
            self.not_Cover(real, expect, datail)
        else:
            self.error(assert_type)


    def equal(self,real,expect,datail):

        assert expect == real, datail



    def notEqual(self,real,expect,datail):

        assert expect != real,datail

    def IN(self,real,expect,datail,DB_table):

        expect_1 = DB(DB_table[0]).select(DB_table[1],expect,real)
        real_1 = {expect:real}

        assert real_1 in expect_1,datail

    def not_IN(self,real,expect,datail,DB_table):

        assert real not in expect,datail

    def cover(self,real,expect,datail):

        assert expect in real, datail

    def not_Cover(self,real,expect,datail):

        assert expect not in real,datail

    def error(self,assert_type):

        assert 1 == 0,"没有匹配到断言类型【{}】，请联系管理员添加，或更换断言类型！".format(assert_type)