#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
'''
1. 什么是多态
    多态指的是同一种/类事物的不同形态

2. 为何要用多态
    多态性:在多态的背景下,可以在不用考虑对象具体类型的前提下而直接使用对象
    多态性的精髓:统一

3. 如何用多态


'''
'''
class Animal:
    def speak(self):
        pass

class People(Animal):
    def shuo(self):
        print('say hello')

class Dog(Animal):
    def jiao(self):
        print('汪汪汪')

class Pig(Animal):
    def chang(self):
        print('哼哼哼')


obj1=People()
obj2=Dog()
obj3=Pig()


# obj1.speak()
# obj2.speak()
# obj3.speak()

def speak(animal):
    animal.speak()


speak(obj1)
speak(obj2)
speak(obj3)

s1='hello'
l1=[1,2,3]
t1=(1,2)

# changdu(s1)
# size(l1)
# kuangdu(t1)


print(len(s1)) #s1.__len__()
print(len(l1)) #l1.__len__()
print(len(t1)) #t1.__len__()
'''
import abc

class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def speak(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass

# Animal() # 父类只是用来建立规范的,不能用来实例化的,更无需实现内部的方法

class People(Animal):
    def speak(self):
        print('say hello')

    def run(self):
        pass

class Dog(Animal):
    def speak(self):
        print('汪汪汪')

    def run(self):
        pass

class Pig(Animal):
    def speak(self):
        print('哼哼哼')

    def run(self):
        pass

obj1=People()
obj2=Dog()
obj3=Pig()


# python崇尚鸭子类型
class Disk:
    def read(self):
        print('Disk read')

    def write(self):
        print('Disk write')


class Memory:
    def read(self):
        print('Mem read')

    def write(self):
        print('Mem write')


class Cpu:
    def read(self):
        print('Cpu read')

    def write(self):
        print('Cpu write')


obj1=Disk()
obj2=Memory()
obj3=Cpu()

obj1.read()
obj2.read()
obj3.read()