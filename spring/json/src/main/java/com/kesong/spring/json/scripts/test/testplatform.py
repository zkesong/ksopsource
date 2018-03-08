# -*- coding: utf-8 -*-
"""
Created on 2017/11/24.

@author: kesong
"""
import platform

from utils.osutil import OSUtil

print platform.python_version()

print str(platform.platform()).find('Windows') == -1

print OSUtil.is_linux()

print OSUtil.is_windows()
