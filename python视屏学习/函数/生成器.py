#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#大前提：生成器就是一种自定义的迭代器，本质就是迭代器

#但凡函数内包含yield关键字，调用函数不会执行函数体代码，会得到一个返回值，该返回值就是生成器对象
# def func():
#     print('frist')
#     yield 1
#     print('second')
#     yield 2
# a=func()
# # print(a)
# # for i in a:
# #     print(i)
# print(a.__iter__().__iter__())
# res1=next(a) #出发函数的执行，知道碰到一个yield停下来，并且将yield后的值当做本次next的结果返回
# res2=next(a)


#练习
# #实现range函数功能
# def r(start,end,step=1):
#     while start <end:
#         yield start
#         start+=step
# boj=r(1,5,2)
# print(next(boj))
# print(next(boj))
# print(next(boj))

#了解知识：yield表达式的应用：x=yield
#强调：针对表形式的yield的使用，第一步必须让函数先暂停到一个yield位置，才能进行传值操作
# def dog(name):
#     food_list=[]
#     while True:
#         foo=yield  food_list
#         print('%s吃了%s'%(name,foo))
#         food_list.append(foo)
# g=dog('alex')
# a=next(g)
#
# res1=g.send('是包子') #1.纤维当前暂停位置的yield赋值，2.next(生成器)知道碰到一个yield停下来，然后其的值当做本次next的结果
# print(res1)
# res2=g.send('肉包子')
# print(res2)
# g.send('泔水')

#总结yield:只能在函数类使用
#1.yield提供了一种自定义迭代器的解决方案
#2.yield可以保存函数的暂停状态
#3.yield对比return
   #1.都可以返回值，值的类型与个数都没有限制
   #2.yield可以返回多个值，而return只能返回一次值函数就结束了

#生成器表达式
# l=[i**2 for i in range(1,6) if i>3]
# print(list(l))
#
# g=(i**2 for i in range(1,6) if i>3)
# print(g)
# print(next(g))
# print(next(g))

g=(i for i in range(101))
print(sum(g))

for i in range(4):
    print(i)