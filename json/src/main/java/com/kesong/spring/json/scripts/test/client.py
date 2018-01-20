# -*- coding: utf-8 -*-
"""
Created on 2017/11/30.

@author: kesong
"""
import socket               # 导入 socket 模块

import sys

client = socket.socket()         # 创建 socket 对象
server_config = (socket.gethostname(), 11111)

try:
    client.connect(server_config)
except BaseException as e:
    print '连接服务器失败...'
    sys.exit(0)

client.send("kesong")
print client.recv(1024)
