import yaml

class GetYaml():

    def __init__(self):

        f = open('/Users/tq/Desktop/BYSJ_Git/NBAutomation/params/Yaml/test.yaml')
        self.cases = yaml.safe_load(f)


    def case_read(self):
        # for case in self.cases:
        #     print(case)
        #     self.case_split(case)

        return self.cases

    def case_select(self,name):
        for case in GetYaml().case_read():
            if case['name'] == name:
                return case



GetYaml().case_read()