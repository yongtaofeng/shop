# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28
from socket import *
import subprocess
import struct
import json
# 服务端必须满足三点
#1.绑定一个固定的ip和端口

#2.一直对外提供服务，稳定云心
#3.支持并发
server = socket(AF_INET, SOCK_STREAM)

server.bind(('127.0.0.1', 9001))

server.listen(5)
while True:

    conn, client_add = server.accept()
    while True:
        try:
            cmd=conn.recv(1024)
            if len(cmd) == 0:
                break
            print(cmd)
            obj=subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            stdout=obj.stdout.read()
            stderr=obj.stderr.read()
            header_dic = {
                'filename': 'a.txt',
                'md5': 'asdfasdf123123x1',
                'total_size': len(stdout) + len(stderr)
            }
            header_json=json.dumps(header_dic)
            header_bythe=header_json.encode('utf-8')
            conn.send(struct.pack('i',len(header_bythe)))
            conn.send(header_bythe)
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError:
         break
    conn.close()
server.close()