import os
import sys

print sys.argv[3]

print os.getcwd()

file_list = os.listdir(os.getcwd())

for _file in file_list:
    if os.path.isdir(_file):
        print os.path.join(os.getcwd(), _file)
        print os.path.exists(_file)
        print os.path.dirname(os.path.join(os.getcwd(), _file))
        print os.path.basename(os.path.join(os.getcwd(), _file))
    else:
        print os.path.isfile(_file)
        print os.path.splitext(_file)[1]

print os.curdir
print os.pardir
print os.extsep
print os.pathsep
print os.defpath
print os.altsep

dir_ = os.getcwd()+os.altsep+os.pardir+os.altsep+'utils'

file_list2 = os.listdir(dir_)
for file_ in file_list2:
    print file_
