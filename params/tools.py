import yaml

class GetYaml():

    def __init__(self,casename):
        self.casename = casename
        '''
        苹果电脑路径
        '''
        f = open(r'/Users/tq/Desktop/BYSJ_Git/NBAutomation/params/Yaml/{}.yaml'.format(self.casename))
        '''
        Windows电脑路径
        '''
        # f = open(r'../params/Yaml/{}.yaml'.format(self.casename),encoding='UTF-8')

        self.cases = yaml.safe_load(f)

    def case_read(self):
        return self.cases

    def case_select(self,name):
        for case in GetYaml(self.casename).case_read():
            if case['name'] == name:
                return case



