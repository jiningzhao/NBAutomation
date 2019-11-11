
'''
data模版
'''


from ..DB_fixture import mysql_db



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
            "name": "赵吉宁自动化测试9",
            "email": "", "gender": "0",
            "mobile": "15600000009",
            "deptIds": [1],
            "married": "",
            "roleIds": [],
            "joinDate": "2019-10-01",
            "managers": [1],
            "education": "2",
            "documentNo": "1411123w331244151",
            "employeeNo": "",
            "positionId": 42,
            "defaultDept": "",
            "documentType": "2"}
        return data