# -*- coding: utf-8 -*-
"""
Created on 2017/12/4.

@author: kesong
"""
# table name with database prefix sql
need_clean_sql = "select table_name from direct_info \
                  where clean_valve != 'NONE' and dept_short_name = '%s' \
                  and is_rule = '1' and is_cert = '0' and export_type = '1'"

pgp_valid_table = "SELECT table_name from share_table_index_dict GROUP BY table_name"
