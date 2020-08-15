#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
def login():
    pass
def show_course():
    pass
def select_course():
   pass
def show_students():
    pass
def modify_score():
    pass
func_dic={
     "1":login,
     "2":show_course,
     "3":select_course,
     "4":show_students,
     "5":modify_score
}


def func_view():
    print('亲爱的老师，请选择功能!')
    while True:
     print('''

1.登录
2.查看教授课程
3.选择教授课程
4.查看课程下学生
5.修改学生成绩
q.返回上级菜单
    ''')
     num=input("请选择你的角色>>>:").strip()
     if num == 'q':break
     if num not in  func_dic:
         print("输入不正确，请重新输入...")
         continue
     func_dic[num]()
