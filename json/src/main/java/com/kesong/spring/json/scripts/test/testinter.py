# -*- coding: utf-8 -*-
"""
Created on 2017/11/30.qaq

@author: kesong
"""
from connectPool import Connects

print type(Connects("pgp").conn_mysql_pgp())

# __import__动态加载模块
a = 2

if a == 1:
    print "加载模块一"
    __import__("testin")

else:
    print "加载模块二"
    __import__("testmd5")

# __debug__
print __debug__

# abs 取绝对值
print abs(-1)

# all 检查数据完整性
print all([]), all(())
print all([0, 1, 2]), all(('', 2, ))

# any 只要有一个数据正确 ： 不为0，空，False
print any([0, 1, '']), any([]), any([0, False, ''])

# basestring str unicode的父类(抽象类) 只能用于判断是否是字符串
print isinstance("aaa", basestring)

# bin 二进制格式
print bin(-10)

# int 整型
print int(-0b1010)

# issubclass
print issubclass(bool, int)

# isinstance
print isinstance("a", str)

# chr
print chr(0x30), chr(0x31), chr(0x61)

# compile
c1 = compile("print 'exec'", "", "exec")
c2 = compile("1 == 1", "c", "eval")
print c1

# exec
exec c1

# eval
print eval(c2)

# next
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
# dir模块目录
print dir()

print __package__

# 当前文件名
print __file__

# 模块文档注释
print __doc__


def p():
    print __name__
    print '__name__'
# 当前执行的主函数
print __name__

p()

# reduce
print reduce(lambda fn, ln: fn + " " + ln + "\n", ['zeng', 'kesong', 'li', 'sss'])

# enumerate
seq = ['a', 'b', 'c', 'd', 'e']
print seq
for ele in seq:
    print ele

for index, ele in enumerate(seq):
    print seq[index]

# dict
webster = {"Aardvark": "A star of a popular children's cartoon show.", "Baa": "The sound a goat makes.",
           "Carpet": "Goes on the floor.", "Dab": "A small amount."}
for key in webster:
    print webster[key]

for ele in webster:
    print ele

# zip
list_a = [3, 9, 17, 15, 19]
list_b = [2, 10, 4, 16, 17, 40]

for a, b in zip(list_a, list_b):
    print 'max(%d, %d) = %d' % (a, b, max(a, b))
    if a > 10:
        break
else:
    print "end for"

itera = iter(list_a)
while True:
    try:
        print(next(itera))
    except StopIteration:
        break
else:
    print "end while"

print sum(i for i in list_a)

print sum([i*2 for i in list_a])

name_list = ["aa_bb", "cc_dd"]
print list(ele.split("_") for ele in name_list)[0]

nus = [2, 34, 0, 4]

for n in nus:
    try:
        print (54 / n)
    except ArithmeticError:
        pass
