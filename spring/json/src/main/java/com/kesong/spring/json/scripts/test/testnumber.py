# coding=utf-8
import os, sys

from sql import fieldsql

var1 = 1
print type(var1)
del var1  # 删除变量
# print var1

out = open(os.getcwd()+'testdata.py', 'w')
print type(out)
del out
# print out # 删除引用

# int
print int.bit_length(8)
print sys.maxsize
print sys.maxunicode
print sys.maxint

# float
a = 5.026
print round(a, 2)
print float('%.2f' % a)
from decimal import Decimal
print Decimal(a).quantize(Decimal('0.00'))

# translate
print complex(1, 2) * complex(0, 1)
print eval("1 == 1")
print eval("not 2 is 3")
print not 2 == 3

print hex(15)
print hex(20)

print cmp(1, 2)
print cmp(10, 4)

import random
# random
lst = range(1, 10, 2)
print lst
random.shuffle(lst)  # 打乱顺序
print lst
print random.choice(lst)
print random.randrange(1, 10, 2)
print random.uniform(1, 10)

# lst2 = range(22, 3434, 10)
# print lst2
# print range(0, len(lst2), 2)

query_per_count = 30

lst = range(0, 1000, query_per_count)
print lst
for index in range(0, len(lst), 2):
    print fieldsql.hive_invalid_sql % ('gs_hj', 'gs_hj_wb', lst[index:index+2][0], lst[index:index+2][1])

print divmod(22, 10)


def a():
    return 1
    print 1

print a()

