#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

'''
1.什么是迭代器：
  迭代器指的是迭代取值的工具
  迭代是一重复的过程，每一次重复都是基于上一次的结果而来


2,为何要使用迭代器：
 迭代器提供了一种不依赖于索引的迭代取值方式

3.如和使用迭代器：



'''
# #单纯的重复不是迭代
# i=0
# while True:
#     print(i)
#
#迭代：重复+每次重复都是基于上一次结果而进行
# l=['a','b','c','d']
# i=0
# while i<len(l):
#     print(l[i])
#     i+=1

#可迭代对象IT而able：但凡内置有__iter__方法的的对象都称之为可迭代的对象
#可迭代对象：str list dict tuple set 文件对象
#执行可迭代对象下的__iter__方法，返回值就是一个迭代器对象

# doc={'x':1,'y':2}
# iter_dic=doc.__iter__()
# print(iter_dic.__next__())
# print(iter_dic.__next__())

#二.迭代器对象
#1.即内置有__next__方法的对象 执行__next__方法可以不依赖索引取值
#2.又有内置__iter__方法的对象
#ps
#1. :迭代器对象一定是可迭代的，可迭代的不一定是迭代器对象
#2. ：文件对象本身即是一个迭代器对象  执行迭代器，__iter__方法得到的仍然是迭代器本身
# l=[1,2,3,4]
# iter_l=l.__iter__()
# print( iter_l is iter_l.__iter__())

# dic={'x':1,"y":2}
# iter_dic=iter(dic)
# while True: #迭代器只能取完之后
#     try:
#         print(dic[next(iter_dic)])
#     except StopIteration:
#         break

#for的底层原理分析
#for循环的本质称之为迭代器循环
#工作原理
#1.先调用in后面那个对象的__iter__方法，将其变成一个迭代器对象
#2.调用next(迭代器)，将得到的放回值复制给变量k
#3.循环往复直到next(迭代器)抛出异常，for会自动捕捉异常然后结束循环
#ps: 从for角度，可以分辨但凡可以被for循环取值的对象都是可迭代对象

#迭代器总结
#迭代器的优点：
  #1.提供了一种不依赖索引的取值方式
  #2.同一时刻在内存中只存在一个值，更节省内存


#迭代器的缺点：
#  1.取值不如按照索引的方式灵活，（不能取指定某一个值，而且只能往后去)
#  2.无法预测迭代器的长度，
#
#
# l=[1,2,3,3,3,3,5,6,5,5,5,]
# iter_l=iter(l)
# print(iter_l)

names=['egon','alex','yxx']
res=map(lambda x:x+"NB",names)
print(list(res))