# -*- coding: utf-8 -*-
"""
Created on 2017/12/21.

@author: kesong
"""
import json
import os
import sys
import re

from config import logconfig
from db.connections import Odspool
from handler.ods_hive_count import OdsHiveComparator
from utils.logutil import LogUtil
from utils.osutil import OSUtil


def single_table(param_dict):
    script = param_dict['script']
    table = param_dict['table']
    tabletype = param_dict['tabletype']
    match_obj = re.match("[a-z]+_hj", str(table))
    if match_obj is None:
        match_obj = re.match("[a-z]+", str(table))
    database = match_obj.group()
    command = "python %s %s %s %s" % (script, database, table, tabletype)
    os.system(command)


def all_table(param_dict):
    __import__("getpgptables")
    if OSUtil.is_linux():
        tbfile_dir = './files/'
    else:
        tbfile_dir = 'F:/project/python/datacompare/files/'
    json_reader = open(tbfile_dir + "tables.json", "r")
    jsonstr = json_reader.readline()
    tables = json.loads(jsonstr)
    print "table count:", len(tables)

    logger = LogUtil().count_logger()
    error_logger = LogUtil().counterror_logger()
    logger.info(logconfig.count_pgp_hive_title)
    error_logger.error(logconfig.count_pgp_hive_title)
    logger.info(logconfig.count_pgphive_schema)
    error_logger.error(logconfig.counterror_pgphive_schema)

    for table in tables:
        param_dict['table'] = table
        single_table(param_dict)


def single_database(param_dict):
    database = param_dict['database']
    print 'current database:', database
    tabletype = param_dict['tabletype']
    sample = param_dict['sample']
    script = param_dict['script']
    if tabletype == "pre":
        OdsHiveComparator.exec_compare(database, Odspool().get_connection(database))
        sys.exit(0)
    if sample:
        command = "python %s '%s' '%s' '%s' '%s'" % (script, database, tabletype, param_dict['divisor']
                                                     , param_dict['mod'])
    else:
        command = "python %s '%s' '%s'" % (script, database, tabletype)
    os.system(command)


def all_database(param_dict):
    __import__("getdepts")
    if OSUtil.is_linux():
        dbfile_dir = './files/'
    else:
        dbfile_dir = 'F:/project/python/datacompare/files/'

    json_reader = open(dbfile_dir+"depts.json", "r")
    jsonstr = json_reader.readline()
    databases = json.loads(jsonstr)
    print "all depts", databases
    for database in databases:
        param_dict['database'] = database
        single_database(param_dict)
