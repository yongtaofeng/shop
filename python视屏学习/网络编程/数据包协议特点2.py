#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt


from  socket import  *


client=socket(AF_INET,SOCK_DGRAM)

client.sendto(b'hello',('127.0.0.1',9001))
client.sendto(b'world',('127.0.0.1',9001))

client.sendto(b'worldff',('127.0.0.1',9001))