#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt


class Mymeta(type): #但凡继承了type的类才能称之为自定义的元类,否则就是只是一个普通的类
    pass

class OldboyTeacher(object): #OldboyTeacher=Mymeta('OldboyTeacher',(object,),{...})
    school = 'Oldboy'

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def score(self):
        print('%s is scoring' %self.name)

    def __call__(self, *args, **kwargs):
        print(self)
        print(args)
        print(kwargs)
tea1=OldboyTeacher('egon',18,'male')

tea1(1,2,a=1,b=2) #__call__(tea1,(1,2).{'a':1,'b':2})


#总结:对象之所以可以调用,是因为对象的类中有一个函数__call__
#推导:如果一切皆对象,那么OldboyTeacher也是一个对象,该对象之所可以调用,肯定是这个对象的类中也定义了一个函数__call__
