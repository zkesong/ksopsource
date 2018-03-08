# -*- coding: utf-8 -*-
"""
Created on 2017/12/5.

@author: kesong
"""
# huawei hive连接配置
huhive_hosts = ['59.202.248.121', '59.202.248.121']
huhive_port = 21066
huhive_authMechanism = "KERBEROS"
huhive_conf = {"krb_host": "hadoop.hadoop.com", "krb_service": "hive"}
huhive_timeout = 600000

# ali hive连接配置
ali_hosts = ["172.31.72.52", "172.31.72.54"]
ali_port = 10000
ali_authMechanism = "KERBEROS"
ali_conf = {"krb_host": "emr-header-1.cluster-12", "krb_service": "hive"}
ali_timeout = 60000000

# peta连接
# peta_database = "shamo"
# peta_database = "petadata_kafka"
peta_database = "pgp"

# pgptest数据库
pgptest_database = "pgp_test"

pgp_database = "pgp"

# 查询字段
query_per_times = 20