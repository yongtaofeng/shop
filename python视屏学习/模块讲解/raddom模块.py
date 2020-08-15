#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
'''
  random随机模块

'''
import random
print(random.random()) #得到一个浮点数
print(random.randint(1,3))#在指定的数字类随机得到一个
print(random.randrange(1,3))#在指定的范围类随机得到一个数，不包含最后一个数字
print(random.choice([1,2,3])) #在指定的容器中，随机获取一个值
print(random.sample([1,2,3],2))#在指定的容器中，随机获取几个值
l=[1,2,3,4,5]
print(random.shuffle(l)) #随机打乱一个容器中的排序
print(l)
for i in range(10):
   print(random.uniform(1,10))#获取指定数字中的一个随机浮点数
