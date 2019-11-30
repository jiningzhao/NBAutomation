# -*- coding:utf-8 -*-
# import pytest
# from ..params.param_template import json_template
# from ..common.api import ApiCall
# from ..params.tools import GetYaml
# from ..common.Assert import Assert
import pytest
from params.tools import GetYaml
from common.Assert import Assert


class Test_Add_Market_Process():

    def one_test(self,get_Token):

        name = 'obj.pageinfo.get'

        response = GetYaml('add_market_test',headers=get_Token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])

    def two_test(self,get_Token):

        name = 'obj.pageinfo.get'

        response = GetYaml('add_market_test',headers=get_Token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])

    def three_test(self,get_Token):

        name = 'obj.objfield.selectshowjson'

        response = GetYaml('add_market_test',headers=get_Token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])

    def four_test(self,get_Token):

        name = 'ac.activityType.list2'

        response = GetYaml('add_market_test',headers=get_Token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])


    def five_test(self,get_Token):

        name = 'ac.labelConf.list2'

        response = GetYaml('add_market_test',headers=get_Token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])


    def add_market_test(self, get_Token,random_massage):

        name = 'ac.activity.add'
        other_data = {'name':random_massage['sentence']+'(JN)'}
        response = GetYaml('add_market_test', other_data=other_data,headers=get_Token).case_select(name)

        Assert(response['assert_type'], response['result']['code'], response['check'], response['result']['msg'])


if __name__ == '__main__':
    pytest.main(['-v','-s'])
    # pytest.main(['-v','-s'])
    # pytest.main(['--collect-only'])
    # pytest.main(['--html=../report/report3.html'])
