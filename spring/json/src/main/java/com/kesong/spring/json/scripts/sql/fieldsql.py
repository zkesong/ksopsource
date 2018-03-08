# -*- coding: utf-8 -*-
# fieldsql module
"""
Created on 2017/11/23.

@author: kesong

sql statements for table field compare
"""

# get hash sum
hash_hive_template = "sum(cast(conv(substr(md5(%s),-3),16,10) as int))"
hash_peta_template = "sum(cast(conv(substr(md5(%s),-3),16,10) as int))"

# select tongid
hive_select_tongid_invalid = "select tongid from %s.%s_invalid_old"
peta_select_tongid_invalid = "select tongid from %s_invalid"
hive_select_tongid_valid = "select tongid from %s.%s_valid_old"
peta_select_tongid_valid = "select tongid from %s_valid"
hive_select_tongid_invaliddetail = "select tongid from %s.%s_invalid_detail_old"
peta_select_tongid_invaliddetail = "select tongid from %s_invalid_detail"

# invalid table sql
hive_invalid_sql = "select %s from %s.%s_invalid_old where tongid = %s"
hash_hive_invalid_sql = "select %s ,count(1)  from  %s.%s_invalid_old %s"
peta_invalid_sql = "select %s from %s_invalid where tongid = %s"
hash_peta_invalid_sql = "select %s ,count(1)  from  %s_invalid%s"

# invalid detail table sql
hive_invalid_detail_sql = "select %s from %s.%s_invalid_detail_old where tongid = %s"
hash_hive_invaliddetail_sql = "select %s ,count(1)  from  %s.%s_invalid_detail_old %s"
peta_invalid_detail_sql = "select %s from %s_invalid_detail where tongid = %s"
hash_peta_invaliddetail_sql = "select %s ,count(1)  from  %s_invalid_detail%s"

# valid table sql
hive_valid_sql = "select %s from %s.%s_valid_old where tongid = %s"
hash_hive_valid_sql = "select %s ,count(1)  from  %s.%s_valid_old %s"
peta_valid_sql = "select %s from %s_valid where tongid = %s"
hash_peta_valid_sql = "select %s ,count(1)  from  %s_valid%s"
