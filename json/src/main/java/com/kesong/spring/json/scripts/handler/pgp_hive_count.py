# -*- coding: utf-8 -*-
"""
Created on 2017/12/13.

@author: kesong
"""
# -*- coding: utf-8 -*-
from pyhs2.error import Pyhs2Exception
from db import connectPool
import sys
import time

from config import dbconfig
from constant import TableType
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
    # 获取部门和表类型参数
    try:
        database = sys.argv[1]
        tablename = sys.argv[2]
        tabletype = sys.argv[3]
    except IndexError as e:
        print '没有参数:database,tablename'
    else:
        try:
            # 开始时间
            start_time = time.time()
            hive_conn = HAConnection(hosts=dbconfig.huhive_hosts,
                                  port=dbconfig.huhive_port,
                                  authMechanism=dbconfig.huhive_authMechanism,
                                  configuration=dbconfig.huhive_conf, timeout=dbconfig.huhive_timeout)
            # 连接hive
            conn = hive_conn.getConnection()

            # 连接pgp test
            conn_pgp = connectPool.Connects(dbconfig.pgp_database).conn_mysql_pgp()
            cur_pgp = conn_pgp.cursor()

            # 获取日志对象
            logger = LogUtil().count_logger()
            error_logger = LogUtil().counterror_logger()

            # 开始对比
            cur_hive = conn.cursor()
            # 设置hive计算引擎
            cur_hive.execute("set hive.execution.engine = spark")

            # 查询语句准备
            if tabletype == TableType.INVALID:
                count_hive_sql = countsql.hive_invalid_sql % (database, tablename)
                count_pgp_sql = countsql.pgp_invalid_sql % tablename
            elif tabletype == TableType.INVALID_DETAIL:
                count_hive_sql = countsql.hive_invalid_detail_sql % (database, tablename)
                count_pgp_sql = countsql.pgp_invalid_detail_sql % tablename
            else:
                count_hive_sql = countsql.pgphive_valid_sql % (database, tablename)
                count_pgp_sql = countsql.pgp_valid_sql % tablename

            # 执行Hive查询
            cur_hive.execute(count_hive_sql)
            count_hive = cur_hive.fetchall()[0][0]

            # 执行peta查询
            cur_pgp.execute(count_pgp_sql)
            count_pgp = cur_pgp.fetchall()[0][0]

            # 对比逻辑
            if count_hive == count_pgp:
                success_result = "%s\t%s\t%s" % (tablename, count_hive, count_pgp)
                logger.info(success_result)
            else:
                error_logger.error("%s\t%s\t%s" % (tablename, count_hive, count_pgp))
            cur_hive.close()

            # 关闭连接
            cur_pgp.close()
        except Pyhs2Exception as err:
            error_logger.error("表不存在: %s" % err)


if __name__ == "__main__":
    exec_compare()
