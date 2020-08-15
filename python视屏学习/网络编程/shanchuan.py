# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28

from socket import *
import subprocess
import struct
import json
import os
# 服务端必须满足三点
#1.绑定一个固定的ip和端口

#2.一直对外提供服务，稳定云心
#3.支持并发
def revc(path,filename):

    server = socket(AF_INET, SOCK_STREAM)

    server.bind(('127.0.0.1', 9001))

    server.listen(5)
    while True:
        conn, client_add = server.accept()
        head_size = struct.unpack('i', conn.recv(4))[0]
        print(head_size)
        header_byte = conn.recv(head_size)
        header_json = header_byte.decode('utf-8')
        header_dic = json.loads(header_json)
        print(header_dic)
        total_size = header_dic['total_size']
        cmd_res = b''
        recv_size = 0
        while recv_size < total_size:
            data = conn.recv(1024)
            recv_size += len(data)
            cmd_res += data
        with open(os.path.join(path,filename), mode='w+',encoding='utf-8') as f:
            f.write(cmd_res.decode('utf-8'))
        conn.close()
    server.close()
revc('E:','a.py')