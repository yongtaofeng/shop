#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

'''
1.什么是装饰器
   器指具备某一个功能的工具，装饰指的是被装饰对象添加新功能
   装饰器就是用来为被装饰对象添加新功能
   注意：装饰器本身可以是任意可调用对象，被装饰器的对象也可以是任意调用对象
2.为什么要使用装饰器
   开放封闭原则：封闭指的是对修改封闭，对扩展开放
   装饰器的实现必须遵循两大原则
      1.不修改被装饰对象的源代码
      2.不修改被装饰器对象的调用方式
      装饰器的目标：就是在遵循1和2原则的前提下为被装饰对象添加上新功能

3.怎么用装饰器


'''
# import time
#
# def index():
#     print("welcome to baoji ")
#     time.sleep(3)
#
# start_time=time.time()
# index()
# stop_time=time.time()
# print(stop_time - start_time)
import time

# #装饰器简单实现
# def index():
#   print("welcome to index page")
#   time.sleep(3)
# def outter(func): #func=最原始的那个index内存地址
#     def wrapper():
#         start=time.time()
#         func() #index函数的内存地址
#         end=time.time()
#         print("run time is %s"%(end-start))
#     return wrapper
#
# index=outter(index)
# index()
#装饰器升级版

def outter1(func): #func=最原始的那个index内存地址
    def wrapper1(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs) #index函数的内存地址 #func是wapper2
        end=time.time()
        cruurt=end-start
        return cruurt,res
    return wrapper1
@outter1#outter1(index)=index=wrapper1()
def index():
  print("welcome to index page")
  time.sleep(3)

print(index())
# @outter
# def home(name):
#     print("welocom to %s"%name)
#     time.sleep(2)
#
# #
# # home=outter(home)
# # home('egon')
# a=index()
# b=home('fyt')
# print(a)
# print(b)


# user='fyt'
# password='123'
# def outter2(func):
#     def wapper2(*args,**kwargs):
#          username=input("请输入姓名>>>")
#          passwd=input("请输入密码>>>")
#          if username==user and passwd==password:
#            print("login success")
#            res=func(*args,**kwargs)
#            return res
#          else:
#              print("用户名密码错误")
#     return wapper2
# @outter1#index=outter1(wrappper2) #index=warpper1
# @outter2 #indexauth(最原始的那个index的内存你地址) indxe=wrapper2
# def index():
#     print('welocome to page')
#     time.sleep(3)
#     return 'success'
# #解释语法的时候是自下而上运行
#
# #而执行装饰的时候是自下而上
# f=index()
# print(f)





