# -*- coding: utf-8 -*-
"""
Created on 2017/11/25.

@author: kesong
"""
import time

import connectPool
from config import logconfig
from constant import TableType
from pyhs2.haconnection import HAConnection
from config import dbconfig

from sql import commonsql
from sql import fieldsql
from utils.logutil import LogUtil
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_common_field(hive_cur, peta_cur, database, name_db_tb, tbtype):
    common_fields = []

    hive_cur.execute("show columns from %s.%s_%s_old" % (database, name_db_tb, tbtype))
    hive_result = hive_cur.fetchall()

    peta_cur.execute("show columns from %s_%s" % (name_db_tb, tbtype))
    peta_result = peta_cur.fetchall()

    col_dict = dict()
    for hivecol_tuple in hive_result:
        hivecol = hivecol_tuple[0]
        col_dict[hivecol] = '@'
    for petacol_tuple in peta_result:
        petacol = str(petacol_tuple[0])
        if col_dict. has_key(petacol):
            common_fields.append(petacol)
    hive_cur.close()

    return common_fields


def exec_compare():
    # 获取参数
    try:
        params = sys.argv
        if len(params) == 3:
            database = params[1]
            tabletype = params[2]
            sample = False
        elif len(params) == 5:
            database = params[1]
            tabletype = params[2]
            divisor = params[3]
            mod = params[4]
            sample = True
    except IndexError as index_error:
        print "传入参数列表：database，tabletype, divisor，mod； 错误信息：", index_error

    # hive连接
    hive_conn_pool = HAConnection(hosts=dbconfig.huhive_hosts, port=dbconfig.huhive_port,
                                  authMechanism=dbconfig.huhive_authMechanism, configuration=dbconfig.huhive_conf,
                                  timeout=dbconfig.huhive_timeout)
    hive_conn = hive_conn_pool.getConnection()

    # petadata连接
    # petadata_conn = connectPool.Connects(dbconfig.peta_database).conn_ali_petadata_shamo()
    petadata_conn = connectPool.Connects(dbconfig.peta_database).conn_ali_petadata()
    petadata_cur = petadata_conn.cursor()

    # pgptest连接
    pgptest_conn = connectPool.Connects(dbconfig.pgptest_database).conn_mysql_test()
    pgptest_cur = pgptest_conn.cursor()

    count_table = pgptest_cur.execute(commonsql.need_clean_sql % database)
    table_names = pgptest_cur.fetchall()

    logger = LogUtil().field_logger()
    error_logger = LogUtil().fielderror_logger()
    log1 = logconfig.field_head % (database, count_table)
    logger.info(log1)
    error_logger.error(log1)

    # 判断表类型
    if tabletype == TableType.INVALID:
        _tabletype = 'invalid'
        logger.info(logconfig.tbtype_invalid)
        error_logger.error(logconfig.tbtype_invalid)
    elif tabletype == TableType.INVALID_DETAIL:
        _tabletype = 'invalid_detail'
        logger.info(logconfig.tbtype_invaliddetail)
        error_logger.error(logconfig.tbtype_invaliddetail)
    else:
        _tabletype = 'valid'
        logger.info(logconfig.tbtype_valid)
        error_logger.error(logconfig.tbtype_valid)

    # 遍历表名
    for name_db_tb_row in table_names:
        name_db_tb = name_db_tb_row[0]
        table_name = name_db_tb.replace(database + '_', '')

        # 设置hive计算引擎
        hive_cur = hive_conn.cursor()
        hive_cur.execute("set hive.execution.engine = spark")

        # 获取表在两边相同的字段
        common_fields = get_common_field(hive_cur, petadata_cur, database, name_db_tb, _tabletype)
        common_fields.append("count")
        log2 = '-----------------表名: %s---------------' % table_name
        logger.info(log2)
        error_logger.error(log2)

        # 日志结构头
        log3 = '字段\thive数据\tpetadata数据\t对比结果'
        logger.info(log3)
        error_logger.error(log3)

        # 开始时间
        time1 = time.time()
        error_row = 0
        
        # 拼接sql语句
        where_sql = ""
        if sample:
            where_sql = "where tongid % %s = %s" % (divisor, mod)
        new_common_fields = []
        for field in common_fields:
            if field == "count":
                continue
            new_common_fields.append((fieldsql.hash_hive_template + " as " + field) % field)
        sql_field = ', '.join(new_common_fields)

        # 查询数据
        hive_cur = hive_conn.cursor()
        petadata_cur = petadata_conn.cursor()
        if tabletype is TableType.INVALID:
            hive_cur.execute(fieldsql.hash_hive_invalid_sql % (sql_field, database, name_db_tb, where_sql))
            petadata_cur.execute(fieldsql.hash_peta_invalid_sql % (sql_field, name_db_tb, where_sql))
        elif tabletype is TableType.INVALID_DETAIL:
            hive_cur.execute(fieldsql.hash_hive_invaliddetail_sql % (sql_field, database, name_db_tb, where_sql))
            petadata_cur.execute(fieldsql.hash_peta_invaliddetail_sql % (sql_field, name_db_tb, where_sql))
        else:
            hive_cur.execute(fieldsql.hash_hive_valid_sql % (sql_field, database, name_db_tb, where_sql))
            petadata_cur.execute(fieldsql.hash_peta_valid_sql % (sql_field, name_db_tb, where_sql))

        # 封装数据记录
        hive_result_row = tuple(hive_cur.fetchall()[0])
        hive_row_dict = dict()
        index = 0
        for hive_data in hive_result_row:
            cur_field_key = common_fields[index]
            hive_row_dict[cur_field_key] = hive_data
            index += 1

        peta_result_row = petadata_cur.fetchall()[0]
        peta_row_dict = dict()
        index = 0
        for peta_data in peta_result_row:
            cur_field_key = common_fields[index]
            peta_row_dict[cur_field_key] = peta_data
            index += 1
        del index

        # 开始比较字段
        success_count = 0
        error_count = 0
        for key in common_fields:
            hive_data = hive_row_dict[key]
            peta_data = peta_row_dict[key]
            if cmp(hive_data, str(peta_data)) == 0:
                log5 = '%s\t%s\t%s\t%s' % (key, hive_data, peta_data, 'SUCCESS')
                logger.info(log5)
                success_count += 1
            else:
                log6 = '%s\t%s\t%s\t%s' % (key, hive_data, peta_data, 'ERROR')
                error_logger.error(log6)
                error_count += 1

        log7 = '相同字段数：%s\t不同字段数：%s\t' % (success_count, error_count)
        logger.info(log7)
        if error_count is not 0:
            error_row += 1

        # 结束时间
        time2 = time.time()
        total = time2 - time1
        log8 = '当前表对比完毕！\t耗时：%.2fs\t异常行数：%s\t' % (total, error_row)
        logger.info(log8)


if __name__ == "__main__":
    # try:
    #     pass
    # except Exception as e:
    #     print e
    LogUtil.print_time(exec_compare)



