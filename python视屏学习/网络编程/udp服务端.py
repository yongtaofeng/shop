#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',9000))
while True:
    data,clent_addr=server.recvfrom(1024)
    print(data)
    msg=input('server>>:').strip()
    server.sendto(msg.encode('utf-8'),clent_addr)
