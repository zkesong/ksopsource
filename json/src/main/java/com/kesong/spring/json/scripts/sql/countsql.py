# -*- coding: utf-8 -*-
# countsql module
"""
Created on 2017/11/23.

@author: kesong

sql statements for table count compare
"""
# invalid table sql
hive_invalid_sql = "select count(1) from %s.%s_invalid_old"
peta_invalid_sql = "select count(1) from %s_invalid"

# invalid detail table sql
hive_invalid_detail_sql = "select count(1) from %s.%s_invalid_detail_old"
peta_invalid_detail_sql = "select count(1) from %s_invalid_detail"

# valid table sql
hive_valid_sql = "select count(1) from %s.%s_valid_old"
pgphive_valid_sql = "select count(1) from %s.%s_old"
peta_valid_sql = "select count(1) from %s_valid"
pgp_valid_sql = "select count(1) from %s"

# ods sql
hive_ods = "select count(1) from %s.%s_pre"
ods = "select count(1) from %s"
