# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28

import struct
from socket import *
import json

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 9001))
while True:
    cmd = input(">>>").strip()
    client.send(cmd.encode('utf-8'))
    head_size = struct.unpack('i', client.recv(4))[0]
    print(head_size)
    header_byte = client.recv(head_size)
    header_json = header_byte.decode('utf-8')
    header_dic = json.loads(header_json)
    print(header_dic)
    total_size = header_dic['total_size']
    cmd_res = b''
    recv_size = 0
    while recv_size < total_size:
        data = client.recv(1024)
        recv_size += len(data)
        cmd_res += data
    print(cmd_res.decode('gbk'))

client.close()
