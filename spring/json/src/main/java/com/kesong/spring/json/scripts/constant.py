# -*- coding: utf-8 -*-
# 常量
"""
Created on 2017/11/29.

@author: kesong
"""


class Strategy:

    USE_SAMPLE = "sample"

    def __init__(self):
        pass


class Err:

    PARAM_ERROR = "param error"

    def __init__(self):
        pass


class TableType:

    INVALID = "invalid"

    VALID = "valid"

    INVALID_DETAIL = "invaliddetail"

    PRE = "pre"

    def __init__(self):
        pass


class CmpType:

    SINGLE_TABLE = "single_table"
    SINGLE_DATABASE = "single_database"
    ALL_TABLE = "all_table"
    ALL_DATABASE = "all_database"

    def __init__(self):
        pass

