'''
开发者：赵吉宁
脚本功能：接口登录
时间：
'''
class login():
    def __init__(self):
        pass

    def md5(self,data): # md5加密算法，且加密后的字符串全部大写——>针对于密码、sign值（拼接之后）的加密
        pass

    def sign(self): # 根据一定拼接方式，生成sign值——>针对于传参中sign字符串的拼接
        pass

    def urlEncoding(self): # url编码——>针对于传参中data的url编码
        pass

    def getCode(self): # 获取返回值中的code值备用
        pass

    def getToken(self): # 获取token值备用
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

    code_response = {"name":"passport.userinfo.bycode",
                    "version":"",
                    "app_key":"test",
                    "data":"%7B%22code%22%3A%2242dc0a8b-d580-48d4-98d6-ad67ac521187%22%7D",
                    "timestamp":"2019-10-24 00:59:55",
                    "format":"json",
                    "sign":"A1776C18F00F74DB281D951C060A8EE5"}
    code_request = {
    "code":0,
    "msg":"操作成功",
    "value":{
        "accessCode":"",
        "admin":1,
        "assetsManagement":"100000000万元",
        "cardEnterpirseAddress":"",
        "createTime":1483409443000,
        "createTimeLong":0,
        "createdBy":null,
        "customerNum":108,
        "defaultPassword":0,
        "depId":null,
        "deptCode":"",
        "deptName":"",
        "dismissionDate":null,
        "displayCusNum":null,
        "documentNo":"",
        "documentNoType":null,
        "documentNoTypeStr":"",
        "documentType":null,
        "education":null,
        "email":"Jensen@163.com",
        "empDeptVoList":null,
        "entId":2099,
        "enterpirseAddress":"",
        "enterpirseLogo":"https://fs.newbanker.cc/img/2099/2019/7/9/c852fc0a656e4f4b824424eff47c8b6b.jpeg",
        "enterpirseName":"北京牛投邦科技咨询有限公司300",
        "enterpriseIntruduction":"<p>q</p>",
        "enterpriseQrcodeImg":"https://fs.newbanker.cc/img/2099/2019/6/21/7ba5895b2ede4bae99d0e5bc7245a660.jpg",
        "external":0,
        "faId":null,
        "gender":null,
        "honors":"NB",
        "id":1,
        "identifiedAuth":1,
        "independent":0,
        "introduction":"Are you kidding me?",
        "joinDate":null,
        "lastLoginIp":"124.126.0.166",
        "lastLoginTime":1571821435000,
        "loginConfig":2,
        "manager":null,
        "married":null,
        "mobile":"18888888888",
        "name":"全局管理员",
        "name1":"S25jQndIbmU=",
        "no":"",
        "outId":"f5b67c95-078f-402b-8570-bc3624efb4a5",
        "pictureUrl":"https://fs.newbanker.cc/1571283534397__1_Advisor_1571283534397.jpg",
        "positionDesc":"",
        "positionId":null,
        "positionName":"",
        "shortBy":"牛投邦300",
        "specialty":"All",
        "status":1,
        "style":1,
        "superAdmin":1,
        "systemCode":"",
        "thumbsCount":5,
        "token":"3d7b123c9-77aa-4b78-a41e-6e64641174c0",
        "updateTime":1571821435000,
        "updatedBy":null,
        "weChatID":"Jensen"
    }
}

