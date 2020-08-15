#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
# def ipcou(file,mode='r',encoding='utf-8'):
#     ip=[]
#     with open(file,mode=mode,encoding=encoding) as f:
#         for line in f:
#             res=line.split()[0]
#             ip.append(res)
#     ipcount={}
#     for i in ip:
#         a=ip.count(i)
#         ipcount[i]=a
#     for  k in ipcount.keys():
#         if ipcount[k] >20 :
#             print(k,ipcount[k])
#
#
# ipcou('access.log')


'''
1.面向过程编程
    核心是过程二字，过程指的就是解决问题的步骤，即先干什么，在干什么，后干什么
    基于核心思想编写程序就好比在设计一条流水线，是一种机械式的思维方式

    优点：复杂问题流程化，进而简单化


    缺点：可扩展性差
'''
# import random
#
# check=""
# for i in range(0,4):
#     index=random.randint(0,4)
#     if index != i:
#         check+=chr(random.randint(97,122))
#     elif index+1==i:
#         check+=chr(random.randint(65,90))
#     else:
#         check+=str(random.randint(0,9))
# print(check)

# print(10>3 and 'alex'=='sb' or 'abc' <'b') #true or  False or True : 结果True

# print(True or False and False)
# s={6,2,3,4}
# for i in s:
# #     print(i)
#
# num=0
# for i in range(100):
#     if i %2 == 0:
#         num-=i
#     else:
#         num+=i
# print(num)
# msg="hello alex"
# print(msg.replace('alex','sb'))
# a=[11,22,33,44,55,66,77,88,99]
# b={}
# c=[]
# d=[]
# for i in a:
#
#     if i >66:
#
#         c.append(i)
#         b['key1']=c
#     else:
#
#         d.append(i)
#         b['key2']=d
# print(b)
# python={'alex','egon','yuanhao','wupeiqi','cobila','biubiu'}
# linux={'wupeiqi','oldboy','cobila'}
# print(python & linux)
# print(python | linux)
# print(python)
# print(python - linux)

#
# a='你'.encode('utf-8')
# print(a)
# print(a.decode('utf-8'))
# # s = '匆匆'
# # print(s.encode('utf-8'))



