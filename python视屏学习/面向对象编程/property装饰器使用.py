#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt


#property:


# class People:
#     def __init__(self,name,weight,height):
#         self.name=name
#         self.weight=weight
#         self.height=height
#     @property
#     def bmi(self):
#         return  self.weight /(self.height ** 2)
# bim=People('egon',80,1.83)
# print(bim.bmi)
# bim.weight=100
# bim.height=1.90
# print(bim.bmi)


class People:
    def __init__(self,name):
        self.__name=name
    @property
    def name(self):
        return "<名字：%s>"%self.__name
    @name.setter
    def name(self,obj):
       self.__name=obj
    @name.deleter
    def name(self):
        del self.__name

obj=People('fyt')
print(obj.name)
obj.name='egon'
print(obj.name)
del  obj.name
print(obj.name)