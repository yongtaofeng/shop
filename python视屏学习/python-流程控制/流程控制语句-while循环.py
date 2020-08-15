#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#while 循环语法
# while 条件：
#     code1
#     code2
#break "终止掉循环"
#continue "终止掉本次循环，直接进入下一次循环"
# user="egon"
# pwd_db="123"
# while True:
#     inp_user=input("Username>>:")
#     inp_pwd=input("Password>>:")
#     if inp_user==user and inp_pwd==pwd_db:
#         print("Login Success")
#         break
#     else:
#         print("Login faile")
# n=1
# while n<11:
#     if n == 8:
#         n+=1
#         continue
#     else:
#         print(n)
#     n+=1


user="egon"
pwd_db="123"
tag=True
while tag:
    inp_user=input("Username>>:")
    inp_pwd=input("Password>>:")
    if inp_user==user and inp_pwd==pwd_db:
        print("Login Success")
        while tag:
            cmd=input(">>>:")
            if cmd=='quit':
                tag=False
                break
            print("run。。。。。。%s"%cmd)
    else:
        print("Login faile")
else:
    print('end.....')