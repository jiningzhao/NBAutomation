import yaml

class GetYaml():

    def __init__(self):

        f = open('/Users/tq/Desktop/BYSJ_Git/NBAutomation/params/Yaml/test.yaml')
        self.y = yaml.safe_load(f)

    def login_yaml(self):
        for i in self.y:
            if i['name']=='passport.login.security':
                return i
        return None

    def add_employee_yaml(self):
        for i in self.y:
            if i['name']=='passport.employee.add':
                return i
        return None

a=GetYaml().login_yaml()
print(a)