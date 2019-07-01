# -*- coding: utf-8 -*-
# @Time : 2019/7/1 22:57
# @Author : wangmengmeng
import pymysql


class clear_data:
    def __init__(self):
        self.host, self.port, self.username, self.passwd, self.dbname = input("请输入服务器地址,端口号,用户名，密码及数据库名，空格隔开：").split()
        # print(self.host,self.port,self.dbname)
        self.execute_sql()

    def connect(self):
        return pymysql.Connect(host=self.host, port=self.port, user=self.username, passwd=self.passwd, db=self.dbname,
                               charset='utf8')

    def getCursor(self, conn):
        if conn is not None:
            return conn.cursor()

    def closeConn(self, conn):
        if conn is not None:
            conn.close()

    def closeCur(self, cur):
        if cur is not None:
            cur.closeCur()

    # 执行没有变量的sql
    def execute_sql(self, cur, sql):
        cur.execute(sql)

    def get_clearsql(self, cur, dbname):
        sql = "select CONCAT('truncate table ',  table_name, ';')  from information_schema.`TABLES` where TABLE_SCHEMA= %%s"
        res = cur.execute(sql, (dbname))
        print(res)


if __name__ == '__main__':
    a = clear_data()
