# -*- coding: utf-8 -*-
"""
Created on 2017/11/30.

@author: kesong
"""
import socket               # 导入 socket 模块

server_socket = socket.socket()         # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 11111                # 设置端口
server_socket.bind((host, port))        # 绑定端口

server_socket.listen(5)                 # 并发客户端连接 超过进入等待
print "服务器启动..."

while True:
    print "等待请求..."
    client_socket, addr = server_socket.accept()     # 建立客户端连接。
    print '客户端连接地址：', addr
    param = client_socket.recv(1024)
    client_socket.send('欢迎访问菜鸟教程！'+ param)
    client_socket.close()                # 关闭连接