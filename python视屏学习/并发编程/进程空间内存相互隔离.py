#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
from multiprocessing import Process,current_process
import time
import os

# n=100
# def task():
#     global n
#     n=0
# if __name__ == "__main__":
#     p=Process(target=task)
#     p.start()
#     p.join()#子进程运行完毕，主进程查看n=100,
#     #所以进程空间内存相互隔离
#     print(n)

#每个进程在操作系统中都有一个唯一的id号，称之为pid

def task():
    print("%s is running"%current_process().pid)
    time.sleep(2)
    print('%s is done'%current_process().pid)

if __name__ == '__main__':
    p=Process(target=task)
    p.start()
    p.terminate()
    p.join()
    print('主%s is running '%current_process().pid)
    print(os.getpid())
    print(os.getppid())
    print(p.name)

#进程名