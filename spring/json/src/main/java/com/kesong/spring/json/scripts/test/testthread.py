# -*- coding: utf-8 -*-
"""
Created on 2017/11/30.

@author: kesong
"""
import thread
import time
import threading

# 为线程定义一个函数
def run(name, delay, _lock):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (name, time.localtime(time.time()))
    _lock.release()

lock = thread.allocate_lock()
lock.acquire()
# 创建两个线程
try:
    thread.start_new_thread(run, ("run_1", 3, lock))
except Exception as e:
    print "Error: unable to start thread", e

while not lock.locked():
    pass
