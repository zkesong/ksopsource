# -*- coding: utf-8 -*-
"""
Created on 2017/11/23.

@author: kesong
"""
import sys
import time

import connectPool
from config import config
from entity import model
from sql import fieldsql, countsql

# 编码设置需要重新加载
reload(sys)
sys.setdefaultencoding('utf-8')

try:
    from pyhs2.haconnection import HAConnection
except ImportError as e:
    print 'error：无法导入pyhs2.haconnection模块(%s)' % e.message
    sys.exit(0)
try:
    database = sys.argv[1]  # 获取部门参数
    log_title = '当前部门：%s' % database
    print log_title
except IndexError as e:
    print 'error：没有传入部门参数(%s)' % e.message
    sys.exit(0)

tongid = sys.argv[2]
# hive连接
hive_conn_pool = HAConnection(hosts=config.hosts, port=config.port,
                         authMechanism=config.authMechanism, configuration=config.conf,
                         timeout=config.timeout)
hive_cur = hive_conn_pool.getConnection().cursor()

# petadata连接
petadata_conn = connectPool.Connects(config.peta_database).conn_ali_petadata_shamo()
petadata_cur = petadata_conn.cursor()

# pgptest连接
pgptest_conn = connectPool.Connects(config.pgptest_database).conn_mysql_test()
pgptest_cur = pgptest_conn.cursor()

# 查询表名
table_count = pgptest_cur.execute(fieldsql.need_clean_sql % database)


for name_db_tb_row in pgptest_cur.fetchall():
    name_db_tb = name_db_tb_row[0]
    table_name = name_db_tb.replace(database + '_', '')
    hive_cur.execute("select hash_unique from %s.%s_invalid_old where tongid=%d" % (database, name_db_tb, int(tongid)))
    print hive_cur.fetchall()
    petadata_cur.execute("select hash_unique from %s_invalid where tongid=%d" % (name_db_tb, int(tongid)))
    print petadata_cur.fetchall()
    sys.exit(0)

