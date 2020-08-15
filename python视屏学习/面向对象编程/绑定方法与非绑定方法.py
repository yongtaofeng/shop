#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

'''
绑定方法： 绑定给谁就应该由谁来调用，谁来调用就会将谁当做第一个参数传入
    1.绑定给对象的方法：类中定义的函数默认就是绑定给对象的
    2.绑定给类的方法：为类定义的函数加上一个装饰器classmethod
非绑定方法：即不与类绑定，又不与对象绑定，以为着对象和类都可以来调用，无论谁来调用都是一个普通的函数，没有自动传值的效果

# '''
# class Foo:
#     def f1(self):
#         print(self)
#
#     @classmethod
#     def  f2(cls):
#         print(cls)
#
#     @staticmethod
#     def f3():
#         pass
#
# obj=Foo()
# print(obj.f1())
# print(Foo.f2())
# print(obj.f3())
# print(Foo.f3())
#
# import settings
#
# class MySql:
#     def __init__(self, ip, port):
#         self.id = self.create_id()
#         self.ip = ip
#         self.port = port
#
#     def tell_info(self):
#         print('<id:%s ip:%s port:%s>' % (self.id, self.ip, self.port))
#
#     @classmethod
#     def from_conf(cls):
#         return cls(settings.IP, settings.PORT)
#
#     @staticmethod
#     def create_id():
#         import uuid
#         return uuid.uuid4()
# obj2 = MySql.from_conf()
# obj2.tell_info()
# class DemoClass:
#     @classmethod  #修饰类的方法，只能类来调用
#     def classPrint(cls):
#        print("class method")
#     def objPrint(self):
#        print("obj method")
#
# obj = DemoClass()
# obj.objPrint()
# obj.classPrint()
# DemoClass.classPrint()


# class cal:
#     cal_name = '计算器'
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     @property           #在cal_add函数前加上@property，使得该函数可直接调用，封装起来
#     def cal_add(self):
#         return self.x + self.y
#
#                         #在cal_info函数前加上@classmethon，则该函数变为类方法，
#     @classmethod        #该函数只能访问到类的数据属性，不能获取实例的数据属性
#     def cal_info(cls):  #python自动传入位置参数cls就是类本身
#         print('这是一个%s'%cls.cal_name)   #cls.cal_name调用类自己的数据属性
#
#     @staticmethod       #静态方法 类或实例均可调用
#     def cal_test(a,b,c): #改静态方法函数里不传入self 或 cls
#         print(a,b,c)
# obj=cal(1,2)
# print(obj.cal_add)
#
# cal.cal_info()
#
# obj.cal_test(1,2,3)
# cal.cal_test(3,2,1)