#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#函数是第一类对象：指的是函数名指向的值（函数)可以被当做数据去使用
# #函数可以当做一个参数传给另外一个函数
# def func(): #func=函数的内存地址
#     print('from func')
#
#
#
# #3.可以当做一个函数的返回值
# def bar(x):
#     return x
#
# a=bar(func)
# print(a())
#
#
# #4.可以当做容器类型的元素
# age=10
# l=[age,func,func()]
# print(l)
#
# def get():
#     print('from get')
# func_dic={
#     'get':get
# }
#
# a=func_dic.get('get')()
# def login():
#     print("login")
# def regist():
#     print("regist")
#
#
# zd={
#    '0':'break',
#    '1':login,
#    '2':regist,
# }
#
# while True:
#     choice=input("请输入你需要事项的额功能:>>>")
#     if choice=='0':break
#     if choice in zd:
#         zd[choice]()
#     else:
#         print("这个功能暂时换没上线")
#函数的嵌套：在调用一个函数过程中，其内部代码又调用了其他函数
# def max2(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# def max4(a,b,c,d):
#      res=max2(a,b)
#      res1=max2(res,c)
#      res2=max2(res1,d)
#      return  res2
# result=max4(1,2,3,4)
# print(result)

# def outter():
#     x=1
#     def inner():
#         print("ineer")
#     print(x)
#     inner()
#
# a=outter()

#
# from  math import pi
# def circle(r,action=0):
#     '''
#
#     :param r:半径
#     :param action:0代表求面积，1代表求周长
#     :return:面积或这周长
#     '''
#     def area(r):
#         res=pi*r**2
#         return res
#     def zc(r):
#         res=2*pi*r**2
#         return  res
#     if action==0:
#         res1=area(r)
#     elif action==1:
#         res1=zc(r)
#     return res1
#
#
#
# c=circle(10,0)
# print(c)


#命名空间
#什么是命名空间：命名空间是用来存放名字与值内存地址绑定关系的地方(内存空间)


#2.名称空间分为三类
 #1.内置名称空间：存放的是python解释器自带的名称空间
    #len   max
 #2.全局名称空间：存放文件级别的名字
     #x=1 y=2
     # if x==1:
     #     z=3

 #3.局部名称空间：在函数内的变量就是局部名称空间
     # def foo(x):
     #     y=2
     #     print(x,y)
 #生命周期：
      #内置名称空间：在解释器启动时则生效，解释器关闭则失效
      #全局名称空间：在解释器解释执行python文件时则生效，文件执行完毕后则失效
      #局部名称空间：只在调用函数时临时产生该函数的局部名称空间，该函数调用完毕后则失效

 #加载顺序： 内置-->全局--->局部







