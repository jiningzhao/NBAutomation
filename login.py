'''
开发者：赵吉宁
脚本功能：接口登录
时间：
'''
class Login():
    def __init__(self):
        pass

    def md5(self,data): # md5加密算法，且加密后的字符串全部大写——>针对于密码、sign值（拼接之后）的加密
        pass

    def sign(self): # 根据一定拼接方式，生成sign值——>针对于传参中sign字符串的拼接
        pass

    def UrlEncoding(self): # url编码——>针对于传参中data的url编码
        pass

    n={
        "name": "passport.login.security",
        "version": "",
        "app_key": "test",
        "data": "%7B%22account%22%3A%2218888888888%22%2C%22password%22%3A%226846860684F05029ABCCC09A53CD66F1%22%2C%22returnUrl%22%3A%22%22%2C%22captcha%22%3A%22%22%7D",
        "timestamp": "2019-10-24 00:36:51",
        "format": "json",
        "sign": "CB8DF0EBA7CAC9AFECCB0A618F8C4A10"
    }

    data={
        "account":"18888888888",
        "password":"6846860684F05029ABCCC09A53CD66F1",
        "returnUrl":"",
        "captcha":""
    }