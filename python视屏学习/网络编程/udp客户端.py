#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg=input(">>>:").strip()
    client.sendto(msg.encode('utf-8'),('127.0.0.1',7010))
    data,server_addr=client.recvfrom(1024)

    print(data)