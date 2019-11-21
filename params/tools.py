import yaml

class GetYaml():

    def __init__(self,casename):
        self.casename = casename

        f = open(r'../params/Yaml/{}.yml'.format(self.casename),encoding="utf-8")
        self.cases = yaml.safe_load(f)

    def case_read(self):
        return self.cases

    def case_select(self,name):
        for case in GetYaml(self.casename).case_read():
            if case['name'] == name:
                return case



