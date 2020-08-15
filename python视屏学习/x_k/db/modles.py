#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
#基类
#我们每个类都有存储和读取文件的方法
from lib import common
class BaseClass:
    def save(self):
        common.save_obj_file(self)
    @classmethod
    def get_obj_for_name(cls,name):
        return common.load_obj_from_file(cls.__name__,name)

class Admin(BaseClass):
    def __init__(self,name,passwd):
        self.name=name
        self.passwd=passwd
        self.save()

    def __str__(self):
        return "name:%s passwd:%s"%(self.name,self.passwd)