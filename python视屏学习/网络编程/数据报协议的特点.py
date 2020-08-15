#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

from  socket import  *
server=socket(AF_INET,SOCK_DGRAM)
server.bind(('127.0.0.1',9001))
print(server.recvfrom(1024))
print(server.recvfrom(1024))
print(server.recvfrom(1024))