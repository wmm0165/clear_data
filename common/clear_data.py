# -*- coding: utf-8 -*-
# @Time : 2019/7/1 22:57
# @Author : wangmengmeng
import pymysql


class clear_data:
    def __init__(self):
        self.host, self.port, self.username, self.passwd, self.dbname = input("请输入服务器地址,端口号,用户名，密码及数据库名，空格隔开：").split()
        # print(self.host,self.port,self.dbname)
        self.connect = pymysql.Connect(host=self.host, port=int(self.port), user=self.username, passwd=self.passwd,
                                       db=self.dbname,
                                       charset='utf8')
        self.cur = self.connect.cursor()

    def clear_data(self):
        sql = "select CONCAT('truncate table ',  table_name, ';')  from information_schema.`TABLES` where TABLE_SCHEMA= %s"
        self.cur.execute(sql, (self.dbname))
        res = self.cur.fetchall()
        print(res)
        print(type(res))
        for s in res:
            self.cur.execute(s[0])
            print(s[0])


if __name__ == '__main__':
    a = clear_data()
    a.clear_data()
