#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
#
# class OldboyStudent:
#     #相同的特征
#     school="oldboy"
#     #相同的技能
#     def choose_course(self):
#         print("choosing course")
#
# #2.调用类来产生对象
# #调用类的过程称之为类的实例化，调用类的返回值称之为类的一个对象/实例
#
# #1.调用类发生了
# #1.会产生一个对象，然后返回
# stu1=OldboyStudent() #对象实例化
# print(stu1.school)
# stu1.choose_course()


#__init__方法的使用

#调用类发生了
#1.产生一个空对像，然后返回
#2.触发类中的函数__init__的执行，将对象连通调用类括号指定的参数一同传入__init__（stu1,'fyt',18,'f')
#__init__ 不能有返回值
class OldboyStudnet:
    yyy=33
    count=0
    def __init__(self,name,age,sex):
        OldboyStudnet.count+=1
        self.name=name
        self.age=age
        self.sex=sex


    def choose_coures(self):
        print("choose_course")
        print(self.name)
        print(self.yyy)
student=OldboyStudnet('fyt',18,'f')
student1=OldboyStudnet('fyt',19,'z')
# print(student.count)
# print(student1.count)
# student.choose_coures()
# print(student.__dict__)
# student.ccc=888
# print(student.__dict__)
# #属性查找的顺序
# #先从对象自己的名称空间找，没有就去类的名称空间找
# print(student.name)

#类中定义的变量是所有对象共享的，对象可以来用，类也可以来使用,类一旦改变自己的数据属性方面，所有对象都能感知到


#类中定义的变量是类的数据属性,类可以用,对象也可以用,大家都指向同一个内存地址,类变量值一旦改变所有对象都跟着变

#类中定义的函数是类的函数属性,类可以用,类来调用就是一个普通的函数,但其实类中定义的函数是给对象用的,而且是绑定给对象用的

#绑定法法:指向类的函数，特殊之处是绑定给谁就应该有谁来调用，谁来调用就会将谁当做第一个参数自动传入

OldboyStudnet.choose_coures(student1)


#总结
list.append()