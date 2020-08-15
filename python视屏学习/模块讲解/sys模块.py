#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
import  sys
'''
常用方法：
argv
'''
# print(sys.argv)#获取cmd的参数
# print(sys.exit(0)) #退出程序
# print(sys.path)
# print(sys.platform) #返回文件系统类型
#print(sys.version) #获取python版本
#print(sys.argv[0])#获取脚本的名称
#print(sys.argv[1]) #获取脚本的一个参数
# def progress(percent,width=30):
#     percent = percent if percent <= 1 else 1
#     text = ("\r[%%-%ds]" % width) % ("*" * int((width * percent)))
#     text = text + "%d%%"
#     text = text % (percent * 100)
#     print(  text  , end="")
import  time

from tqdm import tqdm
def jd():
    for i in tqdm(range(1,101)):
        time.sleep(0.5)
file_size = 10240
# 已经下载大小
cur_size = 0
while True:
    time.sleep(0.5)
    cur_size += 1024
    if cur_size >= file_size:
        print("finish")
        break
    jd()
#进度条
