#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyf
from socket import *

# 服务端必须满足三点
#1.绑定一个固定的ip和端口

#2.一直对外提供服务，稳定云心
#3.支持并发
server = socket(AF_INET, SOCK_STREAM)

server.bind(('127.0.0.1', 9001))

server.listen(5)

conn, client_add = server.accept()
while True:
    try:
        data=conn.recv(1024)
        if len(data) == 0:
            break
        print(data)
        conn.send(data.upper())
    except ConnectionResetError:
        break
conn.close()

