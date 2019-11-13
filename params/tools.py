import yaml

class GetYaml():

    def __init__(self,casename):
        self.casename = casename
        f = open(r'/Users/tq/Desktop/BYSJ_Git/NBAutomation/params/Yaml/{}.yaml'.format(self.casename))
        self.cases = yaml.safe_load(f)


    def case_read(self):

        return self.cases

    def case_select(self,name):
        for case in GetYaml(self.casename).case_read():
            if case['name'] == name:
                return case



