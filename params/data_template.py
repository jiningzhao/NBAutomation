'''
data模版
'''
from DB_fixture import mysql_db


class data_template():

    def passport_login_security(self,account,password):
        '''
        在此处取data中各项的值
        :param account:
        :param password:
        :return:
        '''
        # mysql_db.DB().select('SELECT account,password from user')
        data = {
            "account": account,
            "password": password,
            "returnUrl": "",
            "captcha": ""
        }

        return data

    def passport_userinfo_bycode(self,code):

        data = {
            'code': code
        }

        return data

    def passport_employee_add(self,):

        data = {

        }
        return data