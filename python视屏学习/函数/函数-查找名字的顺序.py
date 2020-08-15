#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
#查找名字的顺序：
     #基于当前所在的位置向上查找
        # 假设当前是局部，查找顺序：局部--》全局————》内置
        #假设当前站全局，查找的顺序：全局--》内置
#
# len=111
# def foo():
#     len=222
#     print(len)
# x=111
# def f1():
#     x=222
#     def f2():
#         x=333
#         def f3():
#             #x=444
#             def f4():
#                 #x=555
#                 print(x)
#             f4()
#         x=777
#         f3()
#     f2()
# f1()

#名字的查找顺序，在函数定义阶段就已经固定死了(即在检测语法是就已经确定了)，与函数的调用位置无关，也就是说无论任何地方调用函数，都必须回到当初
#定义函数的位置去确定名字的查找关系
# x=111
# def outter():
#     def inner():
#         print("from inner",x)
#     return inner
# a=outter()
# print(a)
# a()
#
# x=111
# def outer():
#     def inner():
#         print('for inner',x)
#
#     return inner
# f=outer()
# f()

#作用域
#域指的是范围，作用域指的是作用的范围，分两种
#1.全局作用域：包含的是内置名称与全局名称空间中的名字
#特点：全局有效，全局




#2.局部作用域 ：包含的是局部名称空间的名字



#global：
# nonlocal 申明一个名字是来自当前层外一层作用域，可以用来在局部修改外层函数的不可变类型

x=1
def f():
    x=3
    def foo():
       #nonlocal x #在局部变量声明全局变量
       x=2

    foo()
    print(x)
f()