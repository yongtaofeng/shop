#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

def register():
    pass
def login():
    pass
def select_school():
    pass
def select_course():
    pass
def show_score():
    pass
func_dic={
     "1":register,
     "2":login,
     "3":select_school,
     "4":select_course,
     "5":show_score
}

def func_view():
    print('亲爱的学生，请选择功能!')
    while True:
     print('''
1.注册
2.登录
3.查询学校
4.查询课程
5.查询成绩
q.返回上级菜单
    ''')
     num=input("请选择你的角色>>>:").strip()
     if num == 'q':break
     if num not in  func_dic:
         print("输入不正确，请重新输入...")
         continue
     func_dic[num]()
