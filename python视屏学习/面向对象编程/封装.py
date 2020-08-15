#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

'''
1.什么是封装：
  装:往容器/名称空间里存入名字
  封:代表将存放于名称空间中的名字给藏起来，折中隐藏对外不对类

2.为何要封装


3.如何封装


'''

# class Foo:
#     __x=111
#     __y=222
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def __func(self):
#         print('func')
#     def get_info(self):
#         print(self.__name,self.__age,self.__x,self.__y,self._Foo__y)
#
# obj=Foo('fyt',18)
# obj.get_info()
# obj.__x=333
# print(obj.__dict__)


# class Foo:
#     def __f1(self):
#         print("Foo .f1")
#     def f2(self):
#         print('Foo.f2')
#         self.__f1()
# class Bar(Foo):
#     def __f1(self):
#         print('Bar.f1')
# obj=Bar()
# obj.f2()


# class People:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def tell_info(self):
#         print(('<name %s age：%s>'%(self.__name,self.__age)))
#     def set_info(self,name,age):
#         if type(name)  is not str or type(age) is not int:
#             print("名字或者年龄不是特定类型")
#             return
#         else:
#          self.__name=name
#          self.__age=age
#
#
#封装数据属性:将数据属性隐藏起来,类外就无法直接操作属性,需要类内开辟一个接口来外部的使用可以间接地操作属性,可以在接口内定义任意的控制逻辑,
# 从而严格控制使用对属性的操作
# obj=People('fyt',18)
# obj.tell_info()
# obj.set_info('zsp',"18")
# obj.tell_info()

#封装隔离函数
# class ATM:
#     def __card(self):
#         print('插卡')
#     def __auth(self):
#         print('用户认证')
#     def __input(self):
#         print('输入取款金额')
#     def __print_bill(self):
#         print('打印账单')
#     def __take_money(self):
#         print('取款')
#
#     def withdraw(self):
#         self.__card()
#         self.__auth()
#         self.__input()
#         self.__print_bill()
#         self.__take_money()
# obj=ATM()
# obj.withdraw()