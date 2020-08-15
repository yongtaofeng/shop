#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#1.买手机
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)# Sock_stream tcp流式协议
print(phone)#用来接收链接请求的

#查手机卡（绑定ip端口)
phone.bind(('127.0.0.1',9000))#端口0-65535

#3.开机 #最大请求数为5个（同一时间)
phone.listen(5)
print("start......")

#4.等待电话请求
conn,client_addr=phone.accept() #(双向链接套接字对象,存放客户端ip和端口的校园组# )
print(conn)#conn代表双向链接，收发消息
print(client_addr)


#收消息，发消息
data=conn.recv(1024)#1024代表接收的最大字节数bytes
print("收到客户端的消息",data)
conn.send(data.upper())

conn.close()