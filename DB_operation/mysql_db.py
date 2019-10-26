from pymysql import connect,cursors
from pymysql.err import OperationalError
import os
import configparser as cparser
import json

'''
================读取 db_config.ini 文件设置=================
'''
# 定位当前脚本所在位置的上两级
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
# 对文件路径进行格式处理
base_dir = base_dir.replace("\\","/")
# 定位到db_config.ini文件
file_path = base_dir + "/db_config.ini"

# ConfigParser功能——读取写入配置文件
cf = cparser.ConfigParser()
# read(filename)——直接读取文件内容
cf.read(file_path)

host = cf.get("mysqlconf","host")
port = cf.get("mysqlconf","port")
db = cf.get("mysqlconf","db_name")
user = cf.get("mysqlconf","user")
password = cf.get("mysqlconf","password")

'''
====================封装 MySQL 基本操作=====================
'''
class DB():

    def __init__(self):
        try:
            # 连接数据库
            self.conn = connect(host = host,
                                user = user,
                                password = password,
                                db = db,
                                charset = 'utf8mb4',
                                cursorclass = cursors.DictCursor)


        except OperationalError as e:
            print("MySQL Error %d: %s" % (e.args[0],e.args[1]))


    # 清除数据库表
    def clear(self,table_name):

        # 编写sql语句，删除指定数据库表
        real_sql = "delete from " + table_name +";"

        with self.conn.cursor() as cursors:

            # 在mysql中取消外键约束（设置外键约束: SET FOREIGN_KEY_CHECKS=1; ）
            cursors.execute("SET FOREIGN_KEY_CHECKS=0;")

            # 执行sql，删除数据库表
            cursors.execute(real_sql)

        # 提交执行语句
        self.conn.commit()

    # 插入表数据
    def insert(self,table_name,table_data):

        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ");"
        print(real_sql)

        with self.conn.cursor() as cursors:
            cursors.execute(real_sql)

        self.conn.commit()

    def select(self,sql):

        with self.conn.cursor() as cursors:
            cursors.execute(sql)

        self.conn.commit()

        result1 = cursors.fetchall()

        result1 = json.loads(result1[0]['data'],encoding="utf-8")
        print("+++",result1)


    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db = DB()
    table_name = "case1"
    # data = {"account": "18888888889", "password": "a111111", "returnUrl": "", "captcha": ""}
    interface_name = "passport.employee.add"
    data = {"gender":"0",
                "deptIds":[1],
                "defaultDept":"",
                "documentType":"2",
                "joinDate":"2019-10-01",
                "roleIds":[],
                "education":"2",
                "married":"",
                "employeeNo":"",
                "positionId":42,
                "name":"赵吉宁",
                "documentNo":"133124152346142",
                "mobile":"10900000005",
                "managers":[1],
                "email":""}
    print(json.dumps(data))
    table_data = {"interface_name":interface_name,"data":json.dumps(data,ensure_ascii=False)}
    db.clear(table_name)
    db.insert(table_name,table_data)
    db.select('select * from case1')
    db.close()
