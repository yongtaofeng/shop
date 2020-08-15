#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

'''
1.什么是组合：
   组合指的是某一个对象拥有一个属性，该属性的值是另一个类的对象
'''
class OldboyPeople:
    school = 'Oldboy'

    def __init__(self,name,age,sex,):
        self.name = name
        self.age = age
        self.sex = sex

class OldboyStudent(OldboyPeople):
    def __init__(self, name, age, sex,score=0):
        OldboyPeople.__init__(self,name,age,sex)
        self.score = score
        self.courses=[]

    def choose_course(self):
        print('%s choosing course' % self.name)

    def tell_all_course(self):
        print(('学生[%s]选修的课程如下' %self.name).center(50,'='))
        for obj in self.courses:
            obj.tell_info()
        print('='*60)
    def tell_course(self):
        for obj in self.courses:

              obj.tell_info()


class OldboyTeacher(OldboyPeople):
    def __init__(self,name,age,sex,level):
        OldboyPeople.__init__(self,name,age,sex)
        self.level=level
        self.courses=[]

    def score(self,stu,num):
        stu.score=num

    def tell_all_course(self):
        print(('老师[%s]教授的课程如下' %self.name).center(50,'*'))
        for obj in self.courses:
            obj.tell_info()
        print('*'*70)


class Course:
    def __init__(self,c_name,c_price,c_period):
        self.c_name = c_name
        self.c_price = c_price
        self.c_period = c_period

    def tell_info(self):
        print('\t<课程名:%s 价钱:%s 周期:%s>' %(self.c_name,self.c_price,self.c_period))

class Bj():
    def __init__(self,stu_name,stu_bj,sk_teacher):
        self.name=stu_name
        self.bj=stu_bj
        self.teacher=sk_teacher

    def tell_info(self):
        print('%s属于%s,班主任是%s,选的课程如下：'%(self.name.name,self.bj,self.teacher.name))
        self.name.tell_course()

# 创建课程对象
python=Course('python全栈开发',1900,'5mons')
linux=Course('linux架构师',900,'3mons')


stu1=OldboyStudent('刘二蛋',38,'male')
stu1.courses.append(python)
stu1.courses.append(linux)

# print(stu1.courses)
stu1.tell_all_course()


tea1=OldboyTeacher('egon',18,'male',10)
tea1.courses.append(python)
# print(tea1.courses)
tea1.tell_all_course()
bj=Bj(stu1,"2班",tea1)

bj.tell_info()