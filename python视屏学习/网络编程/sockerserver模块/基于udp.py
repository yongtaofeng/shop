#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

import socketserver

class MyUdphandler(socketserver.BaseRequestHandler):
    def handle(self):
        data,sock=self.request
        print(data)
        sock.sendto(data.upper(),self.client_address)

if __name__ == '__main__':
    server=socketserver.ThreadingUDPServer(('127.0.0.1',7010),MyUdphandler)
    server.serve_forever()