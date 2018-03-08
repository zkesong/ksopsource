# -*- coding: utf-8 -*-
"""
Created on 2017/12/14

@author: kesong

清洗数据对比ali emr和huawei hive上各表数据量

"""
from db import connectPool
import sys
import time

from config import dbconfig
from config import logconfig
from constant import TableType
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


def exec_compare():
    try:
        # 获取部门和表类型参数
        database = sys.argv[1]
        tabletype = sys.argv[2]
    except IndexError as err:
        print '没有参数:database,tabletype；%s' % err
    else:
        # 开始时间
        start_time = time.time()

        # huawei hive
        hive_pool = HAConnection(hosts=dbconfig.huhive_hosts,
                              port=dbconfig.huhive_port,
                              authMechanism=dbconfig.huhive_authMechanism,
                              configuration=dbconfig.huhive_conf, timeout=dbconfig.huhive_timeout)
        hive_conn = hive_pool.getConnection()

        # emr hive
        emr_pool = HAConnection(hosts=dbconfig.ali_hosts, port=dbconfig.ali_port, authMechanism=dbconfig.ali_authMechanism,
                              configuration=dbconfig.ali_conf, timeout=dbconfig.ali_timeout)
        emr_conn = emr_pool.getConnection()

        # 连接pgp test
        conn_pgp_test = connectPool.Connects(dbconfig.pgptest_database).conn_mysql_test()
        cur_pgp_test = conn_pgp_test.cursor()

        # 获取日志对象
        logger = LogUtil().count_logger()
        error_logger = LogUtil().counterror_logger()
        logger.info(logconfig.count_emr_hive_title)
        error_logger.error(logconfig.count_emr_hive_title)

        # 查询每个部门下所有表名
        count = cur_pgp_test.execute(commonsql.need_clean_sql % database)
        log_head = logconfig.count_head % (database, count)
        logger.info(log_head)
        logger.info(logconfig.count_emrhive_schema)
        error_logger.error(logconfig.counterror_emrhive_schema)

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

            cur_hive = hive_conn.cursor()
            cur_emr = emr_conn.cursor()
            # 使用spark 不用mapreduce
            cur_hive.execute("set hive.execution.engine = spark")
            cur_emr.execute("set hive.execution.engine = spark")

            # 查询语句准备
            if tabletype == TableType.INVALID:
                count_hive_sql = countsql.hive_invalid_sql % (database, db_tb_name)
            elif tabletype == TableType.INVALID_DETAIL:
                count_hive_sql = countsql.hive_invalid_detail_sql % (database, db_tb_name)
            else:
                count_hive_sql = countsql.hive_valid_sql % (database, db_tb_name)

            # 执行Hive查询
            cur_hive.execute(count_hive_sql)
            count_hive = cur_hive.fetchall()[0][0]

            # 执行emr查询
            cur_emr.execute(count_hive_sql)
            count_emr = cur_emr.fetchall()[0][0]

            # 结果对比
            if count_hive == count_emr:
                success_count += 1
                success_result = "%s_%s_%s\t%s\t%s" % (database, table, tabletype, count_hive, count_emr)
                logger.info(success_result)
            else:
                error_count += 1
                error_logger.error("%s_%s_%s\t%s\t%s" % (database, table, tabletype, count_hive, count_emr))
            cur_hive.close()
            cur_emr.close()
        # 结束时间
        end_time = time.time()
        # 总耗时
        total_time = end_time - start_time
        tail_log = logconfig.count_tail % (success_count, error_count, total_time)
        logger.info(tail_log)

if __name__ == "__main__":
    exec_compare()


