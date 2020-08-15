#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

import  time
current_user={'name':None}

def login(engine='file'):
    def outter2(func):
        def wapper2(*args,**kwargs):
            while True:
                if current_user['name']:
                    print("已经登录过了,无需再次登陆")
                    res=func(*args,**kwargs)
                    return res
                if engine=='file':
                     username=input("请输入姓名>>>".strip())
                     passwd=input("请输入密码>>>".strip())
                     if username=='egon' and passwd=='123':
                       print("login success")
                       current_user['name']=username#登录成功记录状态
                       res=func(*args,**kwargs)
                       #return res
                     else:
                         print("用户名密码错误")
                elif engine=='mysql':
                    print("基于mysql进行认证")
                elif engine=='ladp':
                   print("基于ladp进行的认证")
                else:
                    print("无法识别认证方式")
        return wapper2
    return outter2
@login('file') #先运行login('mysql')#@outter2(index#最原始的那个index的内存地址)
def index():
    print('welocome to page')
    time.sleep(3)

@login('file')
def home(name):
    print("welocom to %s"%name)
    time.sleep(2)

f=index()
#home('egon')
#有参数的装饰器模板
# def outter1(x,y,z):
#     def outter2(func):
#         def wrapper(*args,**kwargs):
#            res=func(*args,**kwargs)
#            return res
#
#         return wrapper
#     return outter2
#
#
# #五参数的装饰器模板
# def outter(func):
#     def watter(*args,**kwargs):
#         res1=func(*args,**kwargs)
#         return res1
#     return watter

#所有的数据类型的值自带布尔值，可以当做条件去用，只需氩气记住布尔值为假的哪一些值即可(0,空,None）