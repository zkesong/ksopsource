# -*- coding: utf-8 -*-
"""
Created on 2017/11/24.

@author: kesong
"""
import platform


class OSUtil:

    def __init__(self):
        pass

    @staticmethod
    def is_linux():
       return str(platform.platform()).find('Linux') == 0

    @staticmethod
    def is_windows():
        return str(platform.platform()).find('Windows') == 0

