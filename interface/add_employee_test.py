# import pytest
# from ..params.param_template import json_template
# from ..common.api import ApiCall
# from ..params.tools import GetYaml
# from ..common.Assert import Assert
import pytest
from params.tools import GetYaml
from common.Assert import Assert


class Test_Add_Employee_Process():

    # @pytest.fixture()
    # def test_add_department(sel, get_Token, random_massage):
    #
    #     name = 'old_add_department'
    #
    #     other_data = {
    #         'param': {
    #             'name':random_massage['job'],
    #             'departmentTypeCode': random_massage['number(1-2)']
    #         }
    #     }
    #
    #     response = GetYaml('add_employee', other_data=other_data, headers=get_Token).case_select(name)
    #
    #     Assert(response['assert_type'], response['result']['success'], response['check'], response['result'])
    #
    #     print('部门：', other_data['param']['name'])

        # return response['result']['data']

    @pytest.fixture()
    def test_add_position(sel,get_Token,random_massage):

        name = 'old_add_position'
        other_data = {
            'param':{
                'name':random_massage['job'],
                'propertyCode':random_massage['number(1-3)']
            }
        }

        response = GetYaml('add_employee',other_data=other_data,headers=get_Token).case_select(name)

        Assert(response['assert_type'], response['result']['success'], response['check'], response['result']['msg'])
        print('职位：',other_data['param']['name'])
        return response['result']['data']

    def test_add_employee(self,get_Token,random_massage,test_add_position):

        name = 'passport.employee.add'

        other_data = {
            'mobile':random_massage['mobile'],
            'name':random_massage['name'],
            'documentNo':random_massage['ID_card'],
            'positionId':test_add_position,
            'deptIds':[1]
        }

        response = GetYaml('add_employee',other_data=other_data,headers=get_Token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])
        print('员工:',other_data['name'])
        Assert('IN',other_data['mobile'],'mobile',None,response['DB_table'])


if __name__ == '__main__':
    # pytest.main(['-v','-s','--setup-show'])
    # pytest.main(['-v','--pdb'])
    pytest.main(['-v','-s'])
    # pytest.main(['--collect-only'])
    # pytest.main(['--html=../report/report3.html'])
