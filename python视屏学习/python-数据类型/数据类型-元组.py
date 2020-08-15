#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
#1.元组：tuple：记录多个值，当多个值没有该的需求，此时用元组更合适
#2.定义方式：（）内用逗号分隔开多个任意类型的值
t=(1,2,3,4,('a','b'),[1,2],'hello',1)
# print(t,type(t))
#
# #2.元组常用操作+内置方法 元组是不可变的
# #1.按照索引取值（正向和反向取值）：只能取，不能改
# t[5][0]='A'
# print(t)

#1.切片
print(t[0:5])
print(t[::])

#2.长度
print(len(t))
#3.in not in
print(('a','b') not in t)

#4.循环
for i in t:
    print(i)


#二.元组需要掌握的方法
#1.index(寻找元素的索引)
print(t.index(2))
print(t.count(1))

#元组的总结
#1.存取多个值，元组是不可变的
#2.元组是有序的
#3.元组是不可变的