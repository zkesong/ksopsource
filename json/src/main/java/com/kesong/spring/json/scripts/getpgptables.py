# -*- coding: utf-8 -*-
"""
Created on 2017/12/13.

@author: kesong
"""
# 连接pgp data
import json

from db import connectPool
from config import dbconfig
from sql import commonsql

# 连接pgp test
conn_pgp_test = connectPool.Connects(dbconfig.pgptest_database).conn_mysql_test()
cur_pgp_test = conn_pgp_test.cursor()

count = cur_pgp_test.execute(commonsql.pgp_valid_table)
need_compare_tables = cur_pgp_test.fetchall()

table_list = []
for _ in need_compare_tables:
    table_list.extend(_)
jsonStr = json.dumps(table_list)
writer = open("files/tables.json", "w")
writer.writelines(jsonStr)
writer.close()
