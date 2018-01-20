# -*- coding: utf-8 -*-
"""
Created on 2017/11/24.

@author: kesong
"""
import hashlib

m2 = hashlib.md5()

src = 'hello world'

m2.update(src)

print m2.hexdigest()
