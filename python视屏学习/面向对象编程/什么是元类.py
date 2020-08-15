#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

'''
1.什么是元类
   #源自一句话：在python中，一切接对象，而对象都是由类实例化得到的
'''

class OldboyTeacher:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def score(self):
        print("%s is scoring"%self.name)

tea1=OldboyTeacher('fyt',18,'f')
print(type(OldboyTeacher))

# 对象tea1是调用OldboyTeacher类得到的,如果说一切皆对象,那么OldboyTeacher也是一个对象,只要是对象
# 都是调用一个类实例化得到的,即OldboyTeacher=元类(...),内置的元类是type