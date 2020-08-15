#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

from  multiprocessing import  Process

import time
# class Myprocess(Process):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#     def run(self):
#         print('%s is running' %self.name)
#         time.sleep(3)
#         print("%s is done"%self.name)
#
#
# #只有操作系统才能开进程，
# #在windows系统上，开启子进程操作必须放到if__name__ == __main__ 中
# if __name__ == '__main__':
#     #Process(target=task,kwargs={'name':'egon'})
#     #p=Process(target=task,args=('egon',))
#     p=Myprocess('egon')
#     p.start() #只是向操作系统发送了一个开启子进程的信号
#     print('zhu')

#join方法

def task(name,n):
        print('%s is running' %name)
        time.sleep(n)
        print("%s is done"%name)
#
# if __name__ == '__main__':
#     #Process(target=task,kwargs={'name':'egon'})
#     p=Process(target=task,args=('字1',1))
#     p1=Process(target=task,args=('字2',2))
#     p2=Process(target=task,args=('字3',3))
#     #p=Myprocess('egon')
#     p.start() #只是向操作系统发送了一个开启子进程的信号
#     p1.start()
#     p2.start()
#     #time.sleep(4)
#     p2.join()
#     p1.join()
#     p.join()
#     print('zhu')
if __name__ == '__main__':
    p_l=[]
    for i in range(1,4):
        p=Process(target=task,args=('字%s' %i,i))
        p_l.append(p)
        p.start()

    for p in p_l:
        p.join()
    print("主")