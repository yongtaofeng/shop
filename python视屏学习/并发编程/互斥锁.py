#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
import  json
import  time,random
from  multiprocessing import  Process,Lock


def search(name):
    with open('db.json',mode='r',encoding='utf-8') as f:
        dic=json.load(f)
    time.sleep(1)
    print('%s 查看到余票为 %s' %(name,dic['count']))

def get(name):
    with open('db.json','r',encoding='utf-8') as f:
        dic=json.load(f)
    if dic['count'] >0:
        dic['count']-=1
        time.sleep(random.randint(1,3))
        with open('db.json','w',encoding='utf-8') as f:
            json.dump(dic,f)
            print('%s 购票成功' %name)
    else:
        print('%s查看到没有票了' %name)

def task(name,mutex):
    search(name) #并发
    mutex.acquire()#获取锁
    get(name)#串行
    mutex.release()#释放锁

if __name__ == '__main__':
    mutex=Lock()
    for i in range(10):
        p=Process(target=task,args=('路人%s'%i,mutex))
        p.start()