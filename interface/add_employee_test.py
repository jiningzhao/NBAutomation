# import pytest
# from ..params.param_template import json_template
# from ..common.api import ApiCall
# from ..params.tools import GetYaml
# from ..common.Assert import Assert
import pytest
from params.tools import GetYaml
from common.Assert import Assert


class Test_Add_Empolyee_Process():

    def test_add_employee(self,get_Token,random_massage):

        name = 'passport.employee.add'

        other_data = {'mobile':random_massage['mobile'],'name':random_massage['name'],'documentNo':random_massage['ID_card']}

        response = GetYaml('add_employee',other_data=other_data,headers=get_Token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])
        Assert('IN','mobile',other_data['mobile'],response['result']['msg'],response['DB_table'])

if __name__ == '__main__':
    pytest.main(['-v','--setup-show'])
    # pytest.main(['-v','-s'])
    # pytest.main(['--collect-only'])
    # pytest.main(['--html=../report/report3.html'])
