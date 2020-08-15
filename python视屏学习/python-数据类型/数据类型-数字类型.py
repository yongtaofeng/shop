#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
#1.有序：但凡有索引的数据都是有序的
#2.可变可不变
#可变：在值变了情况下，id不变，证明在改原值
#不可变：在值变了情况下，id也跟这变
#基本使用：int

#定义方式
# age=18
# print(type(age))
# print(int(10.1))
# print(chr(90))
# 进制转换（了解**）
# 其他进制转成十进制
# 二进制：0，1
# 10 #1*(2**1) + 0*(2**0)
# # 十进制：0-9
# 371 #3*(10**2) + 7*(10**1) + 1*(10**0)
# # 八进制：0-7
# 371 #3*(8**2) + 7*(8**1) + 1*(8**0)
# # 十六进制：0-9 A-F
# 371 #3*(16**2) + 7*(16**1) + 1*(8**0)
# print(bin(13))#将10进制转换为2进制
# print(oct(13))#将10进制转换为8进制
# print(hex(10))#将10进制转换为16进制
#
# #3.整型操作+内置方法：int
# x=10
# print(id(x))
# x=11
#
# print(id(x))
#
# #float浮点数：height=18.8
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s*%s=%s"%(i,j,i*j),end=' ')
# #     print()
#     *                            1     4   1
#    ***                           2     3   3
#   *****                          3     2   5
#  *******                         4     1   7
# *********                        5     0   9

level_max=5
for i in range(1,level_max+1):
    for x in range(level_max-i):
        print(' ',end='')
    for y in range(2*i-1):
        print("*",end='')
    print()
