#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#1.买手机
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)# Sock_stream tcp流式协议


#直接拨号
phone.connect(('127.0.0.1',9000))


phone.send("hello".encode('utf-8'))#只能发bytes类型
data=phone.recv(1024)
print("收到服务器数据",data)


phone.close()
