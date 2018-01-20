# coding=utf-8
"""
Created on 2017/11/24.

@author: kesong
"""
import os
import sys

print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
print sys.path

dbfile_dir = 'F:/project/python/datacompare/files'

filelist = os.listdir(dbfile_dir)

for _file in filelist:
    reader = open('%s/%s' % (dbfile_dir, _file), 'r')
    print _file
    # for line in reader.readlines():
    #     print line.replace('\n', '').strip()

