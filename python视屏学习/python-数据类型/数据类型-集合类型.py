#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#集合set
#用途：关系运算
#定义方式：在{}以逗号分开的多个值，每一个值都必须是不可变类型
#集合的三大特性
#1.
# s={1,2,'aa',(1,2)}#s=set({{1,2,'aa',(1,2)})
# print(type(s))


# s1={'a','b','c'}
# s2={'a','b','c','d'}
#集合交集
# print(s1 & s2)
# #集合并集
# print(s1 | s2)
# a=(s1 | s2)
# print(a)
#集合差集
# print(s2 - s1)
#
# #集合的对称差集
# print(s1 ^ s2)

#判断是否是父集
# s3={1,2,3}
# s4={3,1,2,6}
# print(s3==s4)
# #子集
# print(s3<s4)
# print(s3>s4)

#集合需要掌握的方法
#update（更新字典
# s2={'a','b','c','d'}
# s3={'a','b'}
# s2.update('e','f','a')
# print(s2)

#pop(删除) #有返回值
# v=s2.pop()
# print(v)

#remove (删除，没有返回值)
# s2.remove('a')
# print(s2)

#difference_update
#s2.difference_update(s3)
# print(s2)
# print(s3)
#
# #删除 discards 没有返回值，元素不存在报错
# s2.discard('a')
#
# #isdisjoint (如果连个集合没有交集则返回true)
#
# #集合：
# #存取多个值
# #集合是可变类型
# print(id(s2))
# s2.add('fyt')
# print(id(s2))

#集合可以用来去重
names=['fff','fff','zzz','zzz','xxx','xxx']
s=set(names)
print(s)