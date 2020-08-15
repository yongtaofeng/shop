#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#模板
# class Mymeta(type): #但凡继承了type的类才能称之为自定义的元类,否则就是只是一个普通的类
#     def __init__(self,class_name,class_bases,class_dic):
#         print(self)
#         print(class_name)
#         print(class_bases)
#         print(class_dic)
#
# class OldboyTeacher(object,metaclass=Mymeta): #OldboyTeacher=Mymeta('OldboyTeacher',(object,),{...})
#     school = 'Oldboy'
#
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#     def score(self):
#         print('%s is scoring' %self.name)

class Mymeta(type): #但凡继承了type的类才能称之为自定义的元类,否则就是只是一个普通的类
    def __init__(self,class_name,class_bases,class_dic):
        if class_name.islower():
            raise TypeError('类名必须使用驼峰体')

        doc=class_dic.get('__doc__')
        if doc is None or len(doc) == 0 or len(doc.strip('\n ')) == 0:
            raise TypeError('类体中必须有文档注释,且文档注释不能为空')
        print(class_dic.get('__doc__'))

class OldboyTeacher(object,metaclass=Mymeta): #OldboyTeacher=Mymeta('OldboyTeacher',(object,),{...})
    '''
    冯永涛
    '''
    school = 'Oldboy'

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def score(self):
        print('%s is scoring' %self.name)
