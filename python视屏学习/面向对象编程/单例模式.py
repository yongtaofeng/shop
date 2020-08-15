#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

import setttings
# # 单例模式：多次实例化的结果指向同一个实例
# class MySql:
#     __instances = None
#
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#
#     @classmethod
#     def from_conf(cls):
#         if cls.__instances is None:
#             cls.__instances=cls(setttings.IP,setttings.PORT)
#         return cls.__instances
#
# obj=MySql.from_conf()
# obj1=MySql.from_conf()
#
# print(obj)
# print(obj1)
#
# import setttings
#
# class MySQL:
#     __instance=None
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#
#     @classmethod
#     def from_conf(cls):
#         if cls.__instance is None:
#             cls.__instance=cls(setttings.IP, setttings.PORT)
#         return cls.__instance
# obj1=MySQL.from_conf()
# obj2=MySQL.from_conf()
# obj3=MySQL.from_conf()
# # obj4=MySQL('1.1.1.3',3302)
# print(obj1)
# print(obj2)
# print(obj3)
#单实例二
# def singleton(cls):
#     __instance=cls(setttings.IP,setttings.PORT)
#     def wrapper(*args,**kwargs):
#         if args or kwargs:
#          inst=cls(*args,**kwargs)
#          return inst
#         return __instance
#     return wrapper
#
# @singleton
# class MySql:
#     def __init__(self, ip, port):
#         self.ip = ip
#         self.port = port
#
# # obj=MySql('1.1.1.1',3306)
# # print(obj.__dict__)
# obj1=MySql()
# obj2=MySql()
# obj3=MySql()
# print(obj1)
# print(obj2)
# print(obj3)

#单例方式3
