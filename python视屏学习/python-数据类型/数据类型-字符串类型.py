#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#1.基本使用
#记录名字，地址，爱好
#2.定义方式在"",""""""内包含一系列的字符

# msg="hello"
# res1=str(1)
# print(res1)
# print(type(res1))

#3.字符串操作+内置方法
#1.优先掌握的
# msg='hello world'
# msg1='    helloworld    '
# print(msg[4])
# print(msg[-1])
# #2.切片（顾头不顾尾)
# print(msg[0:5])
# print(msg[0:5:1])
# print(msg[5:0:-1])
# print(msg[:])
# print(msg[::-1])
# #3.长度
# print(len(msg))
#
# #4.in,not in (成员运算)判断一个子字符串是否存在一个大字符串
# print('h' not  in msg)
#
# #5.移除空白两边的空格strip
# print(msg1.strip()) #默认是空格
# msg2="***+****/***egon  ****-***a****"
# print(msg2.strip("* + / - a"))
#
# #6.切分split 切分完后是一个列表（针对某个有规律的字符串)
# msg3="roo:sss:sex:sss:ccc:66"
# print(msg3.split(":"))
#
# #7.循环
# msg5='hello'
# for i in msg5:
#     print(i)

#二.需要掌握的
#1.strip,lstrip,rstrip
# print('****egon****'.lstrip('*')) #去左
# print('****egon*****'.rstrip('*'))#去右
#
# #2.lower,upper
# msg='AAAAbbbb'
# print(msg.lower()) #变小
# print(msg.upper())#变大
# print(msg)
#
# #3.startswith，endswith
# a='aaabbbccc'
# print(a.startswith('a')) #以什么为开头
# print(a.endswith('c')) #以哪个字符串结尾
#
# #4.formart（格式化字符串）三种玩法
# print("my is name {x},age {y}".format(x='fyt',y=18))
# print("my is name %s,age %s"%('fyt',18))
# print("my is name {},age {}".format('fyt',18))
# print("my is name {name},age {age}".format(name='fyt',age=19))

# #5.split,rsplit
# msg1='gety|aa|bb|cc'
# print(msg1.split('|')) #从左往右切
# print(msg1.rsplit('|'))#从右往左切
#
# #6.join 链接
# a="1234"
# print('|'.join(a)) #将字符串使用特定字符链接
# #7.replace
# msg2='alex say i have one tesla,alex is alex hahahah' #替换指定字符串
# msg2=msg2.replace('alex','fyt',1) #指定替换几次
# print(msg2)
#
# #8.isdigit 判断字符串是否为纯数字
# print('dsfd10'.isdigit())

#需要了解的
#字符串是不可变类型
#find rfind index rindex count
msg='hello alex is sb'
print(msg.find('alex'))
print(msg.find('alex',0,3)) #fing找不到不会报错，返回-1
print(msg.rfind('alex'))
#寻找字符串的索引，找不到报错
# print(msg.index('alex'))
# print(msg.index('alex',0,3)) #找不到会报错
#count 统计字符串在打的字符串中的个数
print(msg.count('a'))

#center
print('egon'.center(50,'*'))#中间对题
print('egon'.ljust(50,'*')) #左对题
print('egon'.rjust(50,'*'))#右对题

#expandtabs #指定tab建的空格数
print('a\tb'.expandtabs(1))
#captalize,swapcase,title
print('hello'.capitalize())#将小写转换为大写
print('HEEO'.swapcase())#将大写转换为小写
print('egon'.title())#首字母大写


#is数字系列
print('1'.isnumeric())
print('1'.isdecimal())
print('1'.isdigit())


#在python3中
num1=b'4' #bytes
num2=u'4' #unicode,python3中无需加u就是unicode
num3='壹' #中文数字
num4='Ⅳ' #罗马数字

#''.isnumeric(): unicode,中文数字，罗马数字
print(num2.isnumeric())
print(num3.isnumeric())
print(num4.isnumeric())

#''.isdecimal(): unicode
print(num2.isdecimal())
print(num3.isdecimal())
print(num4.isdecimal())

# ''.isdigit() :bytes,unicode
print(num1.isdigit())
print(num2.isdigit())
print(num3.isdigit())
print(num4.isdigit())
