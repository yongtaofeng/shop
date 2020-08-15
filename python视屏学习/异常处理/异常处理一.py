#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

'''
1.什么是异常处理
     异常错误发出的信号，一旦程序出错就会产生一个异常,如果该异常没有被应用程序处理，那么该异常就会抛出来，程序的执行也随之终止

     异常包含三个部分
     1.traceback异常的追踪者
     2.异常的类型
     3.异常的信息

     错误分为两种：
       1.语法上的错误，在程序运行前就应该立即修正
       2.逻辑上错误


2.为何要使用异常处理
    避免程序因为异常而崩溃，所以在应用程序中应该对异常进行处理，从而曾强程序的健壮性

3.如何异常处理


#语法
try:
     代码1，
     代码2，
     ....
except NameError:
    #当做异常是NameError时执行的子代码块

'''
'''
try:
    print('=======1')
    l=[1,2,3]
    l[100]
    print('=========2')
    d={'x':1,'y':2}
    d['z']
except IndexError:
    print("IndexError")
print('other code')
'''
#异常多分支
# try:
#     print('=======1')
#     l=[1,2,3]
#     l[100]
#     print('=========2')
#     d={'x':1,'y':2}
#     d['z']
#     print('=======3')
# except IndexError as e:
#     print("IndexError",e)
# except KeyError as e:
#     print("KeyError",e)
#
# print('other code')
#万能异常
# s1='hello'
# try:
#     int(s1)
# except Exception as e:
#     print(e)


# #异常与else连用
# s1='hello'
# try:
#     int(s1)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else:
#     print("try代码类没有异常")
# finally:
#     print('无论异常与否,都会执行该模块,通常是进行清理工作')

#自定义异常
# class EgonException(BaseException):
#     def __int__(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return self.msg
#
# class People:
#     def __inti__(self,name,age):
#         self.__name=name
#         self.__age=age
#
#     def tell_info(self):
#         print(self.__name,self.__age)
#
#     def set_info(self,name,age):
#         if not isinstance(name,str):
#            try:
#                raise EgonException("name不是字符串")
#            except EgonException as e:
#                 print(e)
#         self.__name=name
#         self.__age=age
#
#
#
# # try:
# #      raise  EgonException('类型错误')
# # except EgonException as e:
# #     print(e)
#
# obj=People()
# obj.set_info(111,111)

#断言
#
# l=[1,2,3,4,5]
# if len(l) != 5:
#       raise  TypeError('列表长队必须为5')
#       breal
# print("下半部分执行开始")
# # assert  len(l) != 5
# # print("下班部分运行")