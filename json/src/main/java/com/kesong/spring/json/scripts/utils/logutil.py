# -*- coding: utf-8 -*-
# 日志工具类
"""
Created on 2017/11/25.

@author: kesong
"""
import time
import logging
import logging.config

from utils.osutil import OSUtil


class LogUtil(object):

    # 单例模式
    __instance = None

    # 私有装饰器 读取日志配置文件
    if OSUtil.is_linux():
        # __CONFIG_FILE = "/home/youshu/yscredit/ks/python/datacompare/utils/logger.conf"
		__CONFIG_FILE = "/yscredit/yscredit_test/fusu_test/datacompare/utils/logger.conf"
    else:
        __CONFIG_FILE = "win_logger.conf"

    def __init__(self):
        logging.config.fileConfig(LogUtil.__CONFIG_FILE)

    # 在init执行之前
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    # 计算方法执行时间
    @staticmethod
    def print_time(function):
        start_tine = time.time()
        function()
        end_time = time.time()
        total_time = end_time - start_tine
        print 'total_time: %.2f s' % total_time

    # 日志配置
    __ROOT = 'root'
    __COMPARE_COUNT = 'count'
    __COMPARE_FIELD = 'field'
    __COMPARE_COUNT_ERROR = 'errorcount'
    __COMPARE_FIELD_ERROR = 'errorfield'

    def default_logger(self):
        return logging.getLogger(LogUtil.__ROOT)

    def count_logger(self):
        return logging.getLogger(LogUtil.__COMPARE_COUNT)

    def counterror_logger(self):
        return logging.getLogger(LogUtil.__COMPARE_COUNT_ERROR)

    def field_logger(self):
        return logging.getLogger(LogUtil.__COMPARE_FIELD)

    def fielderror_logger(self):
        return logging.getLogger(LogUtil.__COMPARE_FIELD_ERROR)
