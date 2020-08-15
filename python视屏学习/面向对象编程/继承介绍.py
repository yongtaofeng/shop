#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt


'''
1.什么是继承
  继承是一种新建类的方式，新建的类称之为子类/派生类，被继承的类称之为父类\超类
  继承的特性：子类可以遗传/重用父类的属性

  python中继承的特点
      1.子类可以遗传/重用父类的属性
      2.python中一个子类可以同时继承多个父类
      3.在继承背景下去说，python中的类分为两种，新是类，经典类
          新式类：但凡继承了object的类Foo,以及该类的子类..都是新式类
             在python3中一个类即便没有显示的继承任何类，默认就会继承object
             即python3中所有类都是新式类
          金典类：没有继承object的类，以及该类的子类，。。都是经典类
             在python2中才区分新式类和金典类
             在pyhton2中一个类如果没有显示的继承任何类，也不会继承object

2.为何要用继承
   减少类与类之间的代码冗余

3.如和用继承
'''

# class Parent:
#     pass
#
# class Parent2:
#     pass
#
# class FOO(Parent,Parent2):
#     pass
#
# print(FOO.__bases__) #查看类的继承类


#利用继承来解决类与类之间的代码冗余问题
#在子类派出的新方法中重用父类功能的方式一
#指名道姓应用某一个类中的函数
#总结：
#1.与继承无关
#2.访问时类的函数，没有自动传值效果
#
# class OldboyPeople:
#     school='oldboy'
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
# class OldboyStudent(OldboyPeople):
#
#     def __init__(self,name,age,sex,score=0):
#         OldboyPeople.__init__(self,name,age,sex)
#
#         self.score=score
#     def choose_course(self):
#         print('%s choose course'%self.name)
#
#
# class OldboyTeachr(OldboyStudent):
#     def sorce(self,num):
#         stu.score=num
# stu=OldboyStudent('fyt',18,'f',)
# print(stu.__dict__)
# stu.choose_course()
# tea=OldboyTeachr('admin',22,'n')
# tea.sorce(100)

# #在单继承下的属性查找
# class Foo:
#     def f1(self):
#         print("foo.f1")
#     def f2(self):
#         print("foo.f2")
#         self.f1()
# class bar(Foo):
#     def f1(self):
#         print("bar.f1")
# obj=bar()
# obj.f2()

# 第四层:
# class G:
#    # x = 'G' 7
#     pass
#
# # 第三层
# class E(G):
#    # x = 'E' 3
#     pass
#
# class F:
#     # x = 'F' 5
#     pass
#
# # 第二层
# class B(E):
#    # x = 'B' 2
#     pass
#
# class C(F):
#    # x = 'C' 4
#     pass
#
# class D(G):
#    # x = 'D' 6
#     pass
#
# # 第一层
# class A(B, C, D):
#   #  x = 'A' #1
#     pass
#
# obj = A()
#
# #
# print(A.mro())

#新式类 : 广度优先查找,从左往右一个分支一个分支的查找,在最后一个分支才去查找顶级类
#经典类：深度优先查找,从左往右一个分支一个分支的查找,在第一个分支就查找顶级类

#在子类派生出的新方法中重用父类功能的方式二 super()
# 在子类派生出的新方法中重用父类功能的方式二:super()必须在类中用
# 在python2中:super(自己的类名,自己的对象)
# 在python3中:super()
# 调用该函数会得到一个特殊的对象,该对象专门用来访问父类中的属性,!!!完全参照mro列表!!!!
# 总结:
# 1. 严格依赖继承的mro列表
# # 2. 访问是绑定方法,有自动传值的效果
# class A:
#   def m(self):
#     print('A')
# class B(A):
#   def m(self):
#     print('B')
#     super().m()
# print(B.mro())
# B().m()

class OldboyPeople:
    school = 'Oldboy'

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

class OldboyStudent(OldboyPeople):
    def __init__(self, name, age, sex, score=0):
        super(OldboyStudent,self).__init__(name,age,sex)
        self.score = score

    def choose_course(self):
        print('%s choosing course' % self.name)

class OldboyTeacher(OldboyPeople):
    def __init__(self,name,age,sex,level):
        super().__init__(name,age,sex)
        self.level=level

    def score(self,num):
        self.score=num
        print(self.score)



stu1=OldboyStudent('刘二蛋',38,'male')
# print(stu1.__dict__)

tea1=OldboyTeacher('egon',18,'male',10)
# print(tea1.__dict__)
tea1.score(20)
stu1.choose_course()