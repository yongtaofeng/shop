# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28

import struct
from socket import *
import json
import os
def send(path,filename):
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 9001))
    while True:
        try:
            file_size = os.stat(os.path.join(path, filename)).st_size
            header_dic = {
                'filename': 'a.txt',
                'total_size': file_size
            }

            header_json = json.dumps(header_dic)
            header_bythe = header_json.encode('utf-8')
            client.send(struct.pack('i', len(header_bythe)))
            client.send(header_bythe)
            with open(os.path.join(path,filename), mode='rb') as f:
                data = f.read()
            client.send(data)


        except ConnectionResetError:
            break

    client.close()

send('./','test_client.py')