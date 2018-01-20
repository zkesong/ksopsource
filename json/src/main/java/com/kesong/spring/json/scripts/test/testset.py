# -*- coding: utf-8 -*-
"""
Created on 2017/11/25.

@author: kesong
"""
a = set('abcd')

b = set('defg')

print a

print b

print a & b

print a | b

print a - b

hive_result = [('col1', 'int', 'not null'), ('col2', 'char', 'null'), ('col3', 'varchar', 'null')]
peta_result = [('col2', 'char', 'null'), ('col3', 'varchar', 'null'), ('col4', 'int', 'not null'),
               ('col1', 'char', 'null'), ('col6', 'varchar', 'null')]


common_field = []
col_dict = dict()
for hivecol_tuple in hive_result:
    hivecol = hivecol_tuple[0]
    col_dict[hivecol] = '@'

for petacol_tuple in peta_result:
    petacol = petacol_tuple[0]
    if col_dict.has_key(petacol):
        common_field.append(petacol)


print common_field

