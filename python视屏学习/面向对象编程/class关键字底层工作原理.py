#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt


#调用元类实例化得到自定义的类：OldboyTeacher=type(...)





#自定义类的三个关键组成部分
#1.类名
#2.类的基类们
#3.类的名称空间

# class_name="OldboyTeache"
# class_base=(object,)
# class_dic={}
# class_boy="""
# school="Oldboy"
# def __init__(self,name,age,sex):
#    self.name=name
#    self.age=age
#    self.sex=sex
# def score(self):
#   print("%s is score" %self.name)
# """
# exec(class_boy,{},class_dic)
# print(class_dic)
# OldboyTeache=type(class_name,class_base,class_dic)
# print(OldboyTeache)
class Person(object):
  def __init__(self,name,gender):
      self.name=name
      self.gender=gender

  def __call__(self, *args, **kwargs):
      print("name:%s  gender:%s"%(self.name,self.gender))


obj=Person('fyt','nn')
obj('fyt')