#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#1.列表：是存放多个值，可以根据索引存取值
#2.列表的定义方式，在[]中一个，分隔开
##l=list([1,2,3,4])#list相当调用了一个for循环一次取出'1,2,3,4的值放入list功能

#3.优先掌握列表的常用方法
#1.切片
l=['egon','lxx','yxx']
# print(l[0])
# l[0]='fengyongtao'
# print(l[0])
# print(l[-1])
# print(l[::])#只能根据已经存在的索引取值

#2.想列表中追加值
# l.append('zsp')
# print(l)
#
# #3.inser往指定索引前插入值
# l.insert(2,'sss') #在第二个索引前面插入值
# print(l)
#
# #4.删除值
# del l[0] #通用的
# print(l)

#删除方式二
#print(l.pop(1))#按照索引删除,不指定默认删除末尾的

# #5.长度len
# print(len(l))
#
# #6.成员运算 in not in
# print('lxx' in l)
# print('lxx' not in l)


#二.列表需要掌握的方法
#1.count统计列表中元素的个数
# print(l.count('lxx'))
# print(l.index('lxx',0,2)) #查找指定字符在列表中的索引
# l.clear() #清空列表
# print(l)
#
# l.extend(['a','b','c']) #批量向列表中插入值
# print(l)
#
# l.reverse() #翻转
# print(l)

nums=[7,8,10,6,3]
nums.sort(reverse=True) #默认从小到达,加上resverse=True表示从大到小
print(nums)

#列表总结：
#列表可以存取多个值，列表是有序的，列表是可变的



