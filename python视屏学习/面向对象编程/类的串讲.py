#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt


class Foo:
    x=1
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def f1(self):
        print('run')

obj=Foo('egon',18)
obj.f1()