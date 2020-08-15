# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28
import  struct
import os
# obj1=struct.pack('i',123456)
# print(obj1)
# res1=struct.unpack('i',obj1)
# print(res1)

file_size=os.stat('./test_client.py').st_size
print(file_size)

def put(path,filename):
    file_path=os.stat(os.path.join(path,filename)).st_size
    print(file_path)

put('./','test_client.py')