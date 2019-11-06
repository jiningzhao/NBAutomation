class data_template():

    def passport_login_security(self,account,password):
        data={
            "account": account,
            "password": password,
            "returnUrl": "",
            "captcha": ""
        }
        return data

    def passport_userinfo_bycode(self,code):
        data={
            'code': code
        }
        return data