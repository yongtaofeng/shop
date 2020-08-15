#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
"""
#subprocess模块
   sub 子  process 进程
   什么是进程：
     正在进行中的程序， 每当打开一个程序就会开启一个进程，每个进程包含运行程序所需要的所有资源

     正常情况下，不可以跨进程访问数据
     但是有些情况写就需要访问别的进程数据，一共一个叫做管道的对象， 专门用于跨进程通讯

   作用：用于执行系统命令

"""
import subprocess
import os
# re=subprocess.run('tasklist',shell=True)
# print(re.stdout)
# print(re.stderr)
# print(re)

# res1=subprocess.call("tasklist",shell=True)
# print(res1)
#
# # 常用方法：
# #    run: 返回一个表示执行结果
# #    call()
# res1 = subprocess.Popen("tasklist",stdout=subprocess.PIPE,shell=True,stderr=subprocess.PIPE)
# print("hello")
# print(res1.stdout.read().decode("gbk"))
# print(res1.stderr.read().decode("gbk"))
# res2 = subprocess.Popen("findstr cmd",stdout=subprocess.PIPE,shell=True,stderr=subprocess.PIPE,stdin=res1.stdout)
# print(res2.stdout.read().decode("gbk"))


cmd=input("请输入一个你要执行的linux命令: ")
res=subprocess.run(cmd,stdout=subprocess.PIPE,shell=True,stderr=subprocess.PIPE)
callback=subprocess.call(cmd,stdout=subprocess.PIPE,shell=True,stderr=subprocess.PIPE)
if callback == 0:
    print(res.stdout.decode('gbk'))
else:
    print("青虫性输入")