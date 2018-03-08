# -*- coding: utf-8 -*-
"""
Created on 2017/11/25.

@author: kesong
"""
import re

print re.match('WWW', 'www.baidu.com')
print re.match('WWW', 'www.baidu.com', re.IGNORECASE)
match_obj = re.match('WWW', 'www.baidu.com', re.IGNORECASE)
if match_obj:
    print 'success'
    print match_obj.group()
else:
    print 'error'


line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*) .*', line, re.M | re.I)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
    print matchObj.end(1)
    print matchObj.end(2)
else:
    print "No match!!"


line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print "match --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print "search --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"


# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

print re.sub('(?P<value>\d+)', lambda matcher: str(int(matcher.group('value'))*2), s)
print re.sub('(?P<value>\d+)', lambda matcher: str(int(matcher.group('value'))*3), s)



