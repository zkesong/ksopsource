# -*- coding: utf-8 -*-
"""
Created on 2017/11/25.

@author: kesong
"""
import time

from db import connectPool
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


def tongid_filter(tongid, divisor, mod):
    if divmod(tongid, divisor)[1] == mod:
        return True
    return False


def count_invalid(hive_conn, peta_conn, database, name_db_tb, tbtype):
    cur_hive = hive_conn.cursor()
    cur_hive.execute("set hive.execution.engine = spark")

    # Hive上查询 invalid_old表sql语句
    count_hive_invalid_sql = "select count(1) from %s.%s_%s_old " % (database, name_db_tb, tbtype)
    # 执行Hive查询 valid_old 表
    cur_hive.execute(count_hive_invalid_sql)
    count_hive_invalid = cur_hive.fetchall()[0][0]

    cur_peta = peta_conn.cursor()
    # peta data库查询全部数据和增量数据sql语句
    count_peta_invalid_sql = "select count(1) from %s_%s " % (name_db_tb, tbtype)

    # 执行peta查询
    cur_peta.execute(count_peta_invalid_sql)
    count_peta_invalid = cur_peta.fetchall()[0][0]

    count_log = '====>hive数据量：%s\tpetadata数据量：%s\t' % (count_hive_invalid, count_peta_invalid)
    cur_hive.close()
    cur_peta.close()
    return count_log


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
    petadata_conn = connectPool.Connects(dbconfig.peta_database).conn_ali_petadata()
    petadata_cur = petadata_conn.cursor()

    # pgptest连接
    pgptest_conn = connectPool.Connects(dbconfig.pgptest_database).conn_mysql_test()
    pgptest_cur = pgptest_conn.cursor()

    # 所有表
    count_table = pgptest_cur.execute(commonsql.need_clean_sql % database)
    table_names = pgptest_cur.fetchall()

    # 日志对象
    logger = LogUtil().field_logger()
    error_logger = LogUtil().fielderror_logger()
    logger.info(logconfig.field_peta_hive_title)
    error_logger.error(logconfig.field_peta_hive_title)

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

    log1 = logconfig.field_head % (database, count_table)
    logger.info(log1)
    # 遍历表名
    for name_db_tb_row in table_names:
        name_db_tb = name_db_tb_row[0]
        table_name = name_db_tb.replace(database + '_', '')

        # 设置hive计算引擎
        hive_cur = hive_conn.cursor()
        hive_cur.execute("set hive.execution.engine = spark")

        # 获取表在两边相同的字段
        common_fields = get_common_field(hive_cur, petadata_cur, database, name_db_tb, _tabletype)
        log2 = '表名: %s' % table_name
        logger.info(log2)
        error_logger.error(log2)

        # 输出一下两边数据量
        count_log = count_invalid(hive_conn, petadata_conn, database, name_db_tb, _tabletype)
        logger.info(count_log)

        # 日志结构头
        logger.info(logconfig.field_schema)
        error_logger.error(logconfig.fielderror_schema)

        # 开始时间
        time1 = time.time()
        # 查询所有tongid
        hive_cur = hive_conn.cursor()
        hive_cur.execute("set hive.execution.engine = spark")

        if tabletype == TableType.INVALID:
            hive_cur.execute(fieldsql.hive_select_tongid_invalid % (database, name_db_tb))
        elif tabletype == TableType.INVALID_DETAIL:
            hive_cur.execute(fieldsql.hive_select_tongid_invaliddetail % (database, name_db_tb))
        else:
            hive_cur.execute(fieldsql.hive_select_tongid_valid % (database, name_db_tb))

        tongid_rows = hive_cur.fetchall()
        hive_cur.close()

        error_row = 0
        # 遍历tongid
        for tongid_row in tongid_rows:
            tongid = tongid_row[0]
            if sample:
                # 过滤抽样抽取一些满足条件的tongid
                if not tongid_filter(tongid, int(divisor), int(mod)):
                    continue
            log4 = 'tongid\t%s\t%s\t相同且唯一' % (tongid, tongid)
            logger.info("---------------- 1 行 ------------------\n")
            logger.info(log4)

            sql_field = ', '.join(common_fields)
            # 封装tongid对应的hive数据记录
            hive_cur = hive_conn.cursor()
            petadata_cur = petadata_conn.cursor()

            # 查询数据
            if tabletype == TableType.INVALID:
                hive_cur.execute(fieldsql.hive_invalid_sql % (sql_field, database, name_db_tb, tongid))
                petadata_cur.execute(fieldsql.peta_invalid_sql % (sql_field, name_db_tb, tongid))
            elif tabletype == TableType.INVALID_DETAIL:
                hive_cur.execute(fieldsql.hive_invalid_detail_sql % (sql_field, database, name_db_tb, tongid))
                petadata_cur.execute(fieldsql.peta_invalid_detail_sql % (sql_field, name_db_tb, tongid))
            else:
                hive_cur.execute(fieldsql.hive_valid_sql % (sql_field, database, name_db_tb, tongid))
                petadata_cur.execute(fieldsql.peta_valid_sql % (sql_field, name_db_tb, tongid))

            # 封装每个tongid对应的数据记录
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

            log7 = logconfig.field_result % (success_count, error_count)
            logger.info(log7)
            if error_count is not 0:
                error_row += 1

        # 结束时间
        time2 = time.time()
        total = time2 - time1
        log8 = logconfig.field_tail % (total, error_row)
        print log8
        logger.info(log8)

if __name__ == "__main__":
    try:
        LogUtil.print_time(exec_compare)
    except Exception as e:
        print e



