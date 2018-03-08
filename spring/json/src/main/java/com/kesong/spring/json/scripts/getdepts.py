# -*- coding: utf-8 -*-
"""
Created on 2017/12/7.

@author: kesong
"""
import json

from db import connectPool
from config import dbconfig

conn_pgp_test = connectPool.Connects(dbconfig.pgptest_database).conn_mysql_test()
cur_pgp_test = conn_pgp_test.cursor()
query_distinct_depts = "select distinct dept_short_name from direct_info"
cur_pgp_test.execute(query_distinct_depts)
dept_rows = cur_pgp_test.fetchall()
dept_list = []
for _ in dept_rows:
    dept_list.extend(_)
jsonStr = json.dumps(dept_list)
writer = open("files/depts.json", "w")
writer.writelines(jsonStr)
writer.close()
