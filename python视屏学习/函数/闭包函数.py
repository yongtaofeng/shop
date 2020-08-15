#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#闭包函数
#1.什么是闭包函数
    #闭：是定义在一个函数内部的函数
    #包：该内部函数包含对外层函数作用域名字的应用

#
# def outter():
#     x=1
#     y=2
#     def func():
#         print(x+y)
#     return func
# f=outter()
# f()
# f()
# f()


#闭包：闭包函数提供一种为函数体传值的解决方案

b=eval(input(">>>"))
print(type(b))