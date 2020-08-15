#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
import socketserver
from  socket  import  *

#来自定义类来处理通信循环
class MyTCPhandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:

            try:
                data = self.request.recv(1024)
                if len(data) == 0: break  # 针对linux系统
                print('-->收到客户端的消息: ', data)
                self.request.send(data.upper())
            except ConnectionResetError:
                break

        self.request.close()
if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',9008),MyTCPhandler)
    server.serve_forever()