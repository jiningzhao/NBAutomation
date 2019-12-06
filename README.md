# 接口自动化测试框架
>python + request + pytest + yaml实现接口测试自动化
### 一.背景
   接口测试实施在多系统的平台架构下，有着极为高效的成本收益比（当然，单元测试收益更高，但实施单元测试的成本投入更大，技术要求更高，所以应该选择更适合自身的才是最好的方案）。

接口测试天生为高复杂性的平台带来高效的缺陷检测和质量监督能力，平台复杂，系统越庞大，接口测试的效果越明显。

总的来说，接口测试是保证高复杂性系统质量的内在要求和低成本的经济利益驱动作用下的最佳方案，主要体现在如下三个方面：

1、节省了测试成本

   根据数据模型推算，底层的一个程序BUG可能引发上层的8个左右BUG，而且底层的BUG更容易引起全网的死机；接口测试能够提供系统复杂度上升情况下的低成本高效率的解决方案。

2、接口测试不同于单元测试

   接口测试是站在用户的角度对系统接口进行全面高效持续的检测。

3、效益更高

   将接口测试实现为自动化和持续集成，当系统复杂度和体积越大，接口测试的成本就越低，相对应的，效益产出就越高。
#### 运行环境：
+ python 3.6
#### 引用包：
+ requests
+ hashlib
+ urllib.parse
+ os
+ configparser
+ pymysql
+ json
+ pytest
+ faker
+ yaml
+ time
#### 测试用例书写：
##### 新接口（/XXX/api接口）yaml
```
# 新增员工
-
  datail: 新增员工
  name: passport.employee.add
  api: /passport/api
  method: post
  headers: None
  data:
        {
        name: 'None',
        email: '',
        gender: 0,
        mobile: 'None',
        deptIds: 'None',
        married: '',
        roleIds: [],s
        joinDate: '2019-11-27',
        managers: [ 0 ],
        education: 2,
        documentNo: 'None',
        employeeNo: '',
        positionId: 'None',
        defaultDept: '',
        documentType: 2
        }
  assert_type: equal
  check: 0
  DB_table:
      - wbs240
      - wbs_employee
```
##### 新接口（/XXX/api接口）testcase
```
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
```
##### 老接口（.json）yaml
```
# 添加职位
-
  datail: 新增职位
  name: old_add_position
  api: /http/saas/position/add.json
  method: post
  headers: None
  data:
        {
          param:
            {
            name: None,
            propertyCode: None
            }
        }
  assert_type: equal
  check: true
```
##### 老接口testcase
```
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
```