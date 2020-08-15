#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
from  interface import admin_interface
def register():
    #输入用户名密码，用户名不能为空，密码不能为空，两次密码必须相同， 传递给接口
    #接口层返回处理结果
    while True:
      name=input("请输入用户名(q退出):").strip()
      if name == "q":
          break
      if not name:
          print("用户名不能为空")
          continue
      passwd=input("请输入密码：").strip()
      enter_passwd=input("请确认你的密码:").strip()
      if passwd != enter_passwd:
          print("两次密码不一致，请重试")
          continue
      if not passwd:
          print("密码不能为空")
      admin=admin_interface.admin_register(name,passwd)
      if admin:
          print("注册成功")
          break
      else:
          print("用户名已存在，请重试")

def login():
    pass
def create_school():
    pass

def create_teacher():
    pass

def create_course():
    pass

func_dic={
     "1":register,
     "2":login,
     "3":create_school,
     "4":create_teacher,
     "5":create_course


}

def func_view():
    print('亲爱的管理员，请选择功能!')
    while True:
     print('''
1.注册
2.登录
3.创建学校
4.创建老师
5.创建课程
q.返回上级菜单
    ''')
     num=input("请选择你的角色>>>:").strip()
     if num == 'q':break
     if num not in  func_dic:
         print("输入不正确，请重新输入...")
         continue
     func_dic[num]()


