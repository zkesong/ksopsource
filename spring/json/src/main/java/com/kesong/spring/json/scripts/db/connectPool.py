# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 17:31:59 2017

@author: YScredit
"""
import pymysql

try:
    from impala.dbapi import connect
except ImportError:
    pass
"""
元数据库读入模板
dedupTBL_IDSql = "select TBL_ID from TBLS where TBL_NAME = '%s_%s_dedup'"%(database,table)
cur_metastore.execute(dedupTBL_IDSql)
dedupTBL_ID=cur_metastore.fetchall()[0][0]
dedup_numberSql = "SELECT * FROM TABLE_PARAMS WHERE tbl_id = %s"%dedupTBL_ID

"""
# 连接池，所有的连接连接都放在这个模块下管理
# 命名是要连接的库和端口名，以及要连接的数据库
# 输入的是要连接的库名
# 返回的是游标或者数据库连接

__author__ = 'chuancy zhang'
__version__ = '0.3'


class Connects():
    def __init__(self, db1):
        self.db1 = db1

    def mysql_jkfw(self):
        conn = pymysql.connect(host='59.202.59.213',
                               port=3306,
                               user='jkfw',
                               password='Jkfw123',
                               db=self.db1,
                               charset='utf8')
        cur = conn.cursor()
        return cur

    def mysql_pgp(self):
        conn = pymysql.connect(host='59.202.60.133',
                               port=3306,
                               user='pgp',
                               password='Ys87052730',
                               db=self.db1,
                               charset='utf8')
        cur = conn.cursor()
        return cur

    def mysql_ods(self):
        conn = pymysql.connect(host='59.202.60.155',
                               port=3306,
                               user='hjdb',
                               password='sfbgthjsjk',
                               db=self.db1,
                               charset='utf8')
        cur = conn.cursor()
        return cur

    def conn_mysql_ods(self):
        conn = pymysql.connect(host='59.202.60.155',
                               port=3306,
                               user='hjdb',
                               password='sfbgthjsjk',
                               db=self.db1,
                               charset='utf8')
        return conn

    def mysql_gat(self):
        conn = pymysql.connect(host='59.202.58.241',
                               port=3306,
                               user='hjdb',
                               password='sfbgthjsjk',
                               db=self.db1,
                               charset='utf8')
        cur = conn.cursor()
        return cur

    def conn_mysql_gat(self):
        conn = pymysql.connect(host='59.202.58.241',
                               port=3306,
                               user='hjdb',
                               password='sfbgthjsjk',
                               db=self.db1,
                               charset='utf8')
        return conn

    def mysql_hive_metastore(self):
        conn = pymysql.connect(host='59.202.34.179',
                               port=3306,
                               user='root',
                               password='root',
                               db=self.db1,
                               charset='utf8')
        cur = conn.cursor()
        return cur

    def mysql_hy(self):
        conn = pymysql.connect(host='59.202.61.17',
                               port=3306,
                               user='hjdb',
                               password='sfbgthjsjk',
                               db=self.db1,
                               charset='utf8')
        cur = conn.cursor()
        return cur

    def conn_mysql_hy(self):
        conn = pymysql.connect(host='59.202.61.17',
                               port=3306,
                               user='hjdb',
                               password='sfbgthjsjk',
                               db=self.db1,
                               charset='utf8')
        return conn

    def conn_hive(self):
        conn = connect(host='59.202.34.179',
                       port=10000,
                       auth_mechanism='PLAIN',
                       user='root',
                       password='root',
                       database=self.db1)
        cur = conn.cursor()
        return cur

    def mysql_test(self):
        conn = pymysql.connect(host='59.202.60.133',
                               port=3306,
                               user='pgptest',
                               password='pgptest123',
                               db=self.db1,
                               charset='utf8')
        cur = conn.cursor()
        return cur

    def conn_mysql_pgp(self):
        conn = pymysql.connect(host='59.202.60.133',
                               port=3306,
                               user='pgp',
                               password='Ys87052730',
                               db=self.db1,
                               charset='utf8')
        return conn

    def conn_mysql_pgp_hive_test(self):
        conn = pymysql.connect(host='59.202.59.213',
                               port=3306,
                               user='pgp',
                               password='Ys87052730',
                               db=self.db1,
                               charset='utf8')
        return conn

    def conn_mysql_ods(self):
        conn = pymysql.connect(host='59.202.60.155',
                               port=3306,
                               user='hjdb',
                               password='sfbgthjsjk',
                               db=self.db1,
                               charset='utf8')
        return conn

    def conn_mysql_gat(self):
        conn = pymysql.connect(host='59.202.60.158',
                               port=3306,
                               user='hjdb',
                               password='sfbgthjsjk',
                               db=self.db1,
                               charset='utf8')
        return conn

    def conn_mysql_hive_metastore(self):
        conn = pymysql.connect(host='59.202.34.179',
                               port=3306,
                               user='root',
                               password='root',
                               db=self.db1,
                               charset='utf8')
        return conn

    def conn_mysql_test(self):
        conn = pymysql.connect(host='59.202.60.133',
                               port=3306,
                               user='pgptest',
                               password='pgptest123',
                               db=self.db1,
                               charset='utf8')
        return conn

    def conn_mysql_jkfw(self):
        conn = pymysql.connect(host='59.202.59.213',
                               port=3306,
                               user='jkfw',
                               password='Jkfw123',
                               db=self.db1,
                               charset='utf8')
        return conn

    def conn_mysql_hy(self):
        conn = pymysql.connect(host='59.202.61.17',
                               port=3306,
                               user='hjdb',
                               password='sfbgthjsjk',
                               db=self.db1,
                               charset='utf8')
        return conn

    def conn_mysql_czrk(self):
        conn = pymysql.connect(host='59.202.60.20',
                               port=3306,
                               user='hjdb',
                               password='hjdb123',
                               db=self.db1,
                               charset='utf8')
        return conn

    def conn_ali_petadata_shamo(self):
        conn = pymysql.connect(host='172.31.70.176',
                               port=3306,
                               user='shamo',
                               password='Alibaba1688',
                               db=self.db1,
                               autocommit=True,
                               charset='utf8')
        return conn

    def conn_ali_petadata_test(self):
        conn = pymysql.connect(host='47.96.215.254',
                               port=3306,
                               user='petadata',
                               password='petadata',
                               db=self.db1,
                               autocommit=True,
                               charset='utf8')
        return conn

    def conn_ali_petadata(self):
        conn = pymysql.connect(host='172.31.68.44',
                               port=3306,
                               user='yscredit',
                               password='Yscredit4321',
                               db=self.db1,
                               autocommit=True,
                               charset='utf8')
        return conn

    @staticmethod
    def conn_v3_rds_test():
        conn = pymysql.connect(host='172.31.74.123',
                               port=3306,
                               user='yscredit',
                               password='yscreditemrtest',
                               db='ys_emr_dict_test',
                               autocommit=True,
                               charset='utf8')
        return conn
