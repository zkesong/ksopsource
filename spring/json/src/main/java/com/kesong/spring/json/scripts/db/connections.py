# -*- coding: utf-8 -*-
"""
Created on 2017/12/5.

@author: kesong
"""
import json

from pymysql import OperationalError

import connectPool


class Odspool(object):
    __dept_dict = None

    def __init__(self):
        if self.__dept_dict is None:
            self.__get_depts()
        pass

    def __write_json(self, obj, path):
        json_str = json.dumps(obj)
        writer = open(path, "w")
        writer.writelines(json_str)
        writer.close()

    def __read_json(self, path):
        reader = open(path, "r")
        jsonstr = reader.readline()
        return json.loads(jsonstr)

    def __get_depts(self):
        try:
            conn_v3 = connectPool.Connects.conn_v3_rds_test()
            sql = "select database_name, database_url from source_database_dict"
            cur_v3 = conn_v3.cursor()
            cur_v3.execute(sql)
            name_urls = cur_v3.fetchall()
            dept_dict = {}
            for name_url in name_urls:
                dept_dict[name_url[0]] = name_url[1]
            self.__dept_dict = dept_dict
            self.__write_json(self.__dept_dict, "files/dept_dict.json")
        except OperationalError as err:
            print "无法连接v3库，", err
            print "从本地json文件加载数据..."
            self.__dept_dict = self.__read_json("files/dept_dict.json")

    def get_connection(self, dept):
        if self.__dept_dict.get(dept) == "59.202.60.155":
            return connectPool.Connects(dept).conn_mysql_ods()
        elif self.__dept_dict.get(dept) == "59.202.58.241":
            return connectPool.Connects(dept).conn_mysql_gat()
        elif self.__dept_dict.get(dept) == "59.202.61.17":
            return connectPool.Connects(dept).conn_mysql_hy()
        elif self.__dept_dict.get(dept) == "59.202.60.20":
            return connectPool.Connects(dept).conn_mysql_czrk()