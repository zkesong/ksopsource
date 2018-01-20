# -*- coding: utf-8 -*-
"""
Created on 2017/12/5.

@author: kesong
"""


class Singleton(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            Singleton.__instance = object.__new__(cls, *args, **kwargs)
        return Singleton.__instance


print Singleton()
print Singleton()