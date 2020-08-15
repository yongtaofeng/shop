#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt


import hashlib
#
# m=hashlib.md5() #构造一个hashlib对象
# m.update('hello'.encode('utf-8')) #update对指定字符串进行加密
# print(m.hexdigest()) #
#
# m.update('alvin'.encode('utf-8'))
# print(m.hexdigest())
#
# m2=hashlib.md5()
# m2.update('helloalvin'.encode('utf-8'))
# print(m2.hexdigest()) #hexdigest打印出加密后的结果
# '''
# 注意：把一段很长的数据update多次，与一次update这段长数据，得到的结果一样
# 但是update多次为校验大文件提供了可能。
# '''

password = [
    'alex3714',
    'alex1313',
    'alex94139413',
    'alex123456',
    '123456alex',
    'a123lex',
]

#
# def make_passwd_dic(passwd):
#     dic = {}
#     for passwd in passwd:
#         m = hashlib.md5()
#         m.update(passwd.encode('utf-8'))
#         dic[passwd] = m.hexdigest()
#
#     return dic
#
#
# def break_code(cry, passwd_dic):
#     for k, v in passwd_dic.items():
#         if v == cry:
#             print('密码是====》%s' % k)
#
#
# cry = 'aee949757a2e698417463d47acac93df'
# break_code(cry, make_passwd_dic(password))

import hmac

h1 = hmac.new('hello'.encode('utf-8'), digestmod='md5')
h1.update('world'.encode('utf-8'))

print(h1.hexdigest())

h2 = hmac.new('hello'.encode('utf-8'), digestmod='md5')
h2.update('orld'.encode('utf-8'))
h2.update('w'.encode('utf-8'))
h2.update('fyt'.encode('utf-8'))
print(h2.hexdigest())