#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
'''
    time模块：
       与时间相关的功能
    在python中 时间分为3中
       1.时间戳： timestamp 从1970 1月 1日 到现在的描述，主要用于计算两个时间的差
       2.localtime 本地时间， 表示的是计算机当前所在位置
       3.UTC 世界协调时间
'''
import  time
# print(time.time())#获取时间戳
# print(time.localtime()) #获取元组时间，返回的是结构化时间，获取当地时间
# #获取UTC时间,返回的换是结构化时间，比中国时间少8小时
# print(time.gmtime())
# #将获取的时间转换为我们期望的时间
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
#
# #将格式化字符串的时间转换为结构化时间 注意：格式必须匹配
# print(time.strptime("2020-05-28 14:38:30","%Y-%m-%d %H:%M:%S"))
# #时间戳结构化
# print(time.localtime(10))
#
# #结构化转为时间戳
# print(time.mktime(time.localtime()))
#
# #sleep 让计算及睡
# time.sleep(2)
#
# #不太常用的时间格式
# print(time.asctime())

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
