# -*- coding: utf-8 -*-
"""
Created on 2017/11/25.

@author: kesong
"""
import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)

print text
