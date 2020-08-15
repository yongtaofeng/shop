#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt


#守护进程：本质就是一个“子进程",该”子进程"的生命周期<=被守护进程的生命周期
from  multiprocessing import  Process

import time

def task(name):
    print("老太监%s活着"%name)
    time.sleep(3)
    print("老太监%s正常死亡。。。"%name)

if __name__ == '__main__':
    p=Process(target=task,args=('刘清正',))
    p.daemon=True
    p.start()
    time.sleep(1)
    print("皇上：EGON正在四")
