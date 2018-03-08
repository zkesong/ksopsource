# -*- coding: utf-8 -*-
"""
@author: fu su ke song
清洗数据对比ods和hive上各表数据量
"""
from db import connectPool
import sys
import time

from config import dbconfig
from config import logconfig
from sql import commonsql
from sql import countsql
from utils.logutil import LogUtil

try:
    from pyhs2.haconnection import HAConnection
except ImportError as e:
    print '导入pyhs2.haconnection模块错误'

# 设置编码
reload(sys)
sys.setdefaultencoding('utf-8')


class OdsHiveComparator:
    
    def __init__(self):
        pass
    
    @staticmethod
    def exec_compare(database, ods_conn):
        # 开始时间
        start_time = time.time()
        hive_conn = HAConnection(hosts=dbconfig.ali_hosts, port=dbconfig.ali_port, authMechanism=dbconfig.ali_authMechanism,
                              configuration=dbconfig.ali_conf, timeout=dbconfig.ali_timeout)
        # 连接hive
        conn = hive_conn.getConnection()

        # 连接ods
        cur_ods = ods_conn.cursor()

        # 连接pgp test
        conn_pgp_test = connectPool.Connects(dbconfig.pgptest_database).conn_mysql_test()
        cur_pgp_test = conn_pgp_test.cursor()

        # 获取日志对象
        logger = LogUtil().count_logger()
        error_logger = LogUtil().counterror_logger()
        logger.info(logconfig.count_ods_hive_title)
        error_logger.error(logconfig.count_ods_hive_title)

        # 查询每个部门下所有表名
        count = cur_pgp_test.execute(commonsql.need_clean_sql % database)
        log_head = logconfig.count_head % (database, count)
        logger.info(log_head)
        logger.info(logconfig.count_odshive_schema)
        error_logger.error(logconfig.counterror_odshive_schema)

        # 所有需要清洗的表名和库名数据
        need_clean_tables = cur_pgp_test.fetchall()
        cur_pgp_test.close()
        conn_pgp_test.close()

        # 统计结果
        success_count = 0
        error_count = 0
        for need_clean_table in need_clean_tables:
            db_tb_name = need_clean_table[0]
            table = db_tb_name.replace(database + '_', '')

            cur_hive = conn.cursor()

            # 查询语句准备
            count_hive_sql = countsql.hive_ods % (database, db_tb_name)
            count_ods_sql = countsql.ods % table

            # 执行Hive查询
            cur_hive.execute(count_hive_sql)
            count_hive = cur_hive.fetchall()[0][0]

            # 执行ods查询
            cur_ods.execute(count_ods_sql)
            count_ods = cur_ods.fetchall()[0][0]

            # 对比逻辑
            if count_hive == count_ods:
                success_count += 1
                success_result = "%s_%s_ods\t%s\t%s" % (database, table, count_hive, count_ods)
                logger.info(success_result)
            else:
                error_count += 1
                error_logger.error("%s_%s_ods\t%s\t%s" % (database, table, count_hive, count_ods))
            cur_hive.close()
        # 结束时间
        end_time = time.time()
        # 总耗时
        total_time = end_time - start_time
        tail_log = logconfig.count_tail % (success_count, error_count, total_time)
        logger.info(tail_log)

        # 关闭连接
        cur_ods.close()
