#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
from core import  admin,student,teacher

func_dic={
   "1":admin.func_view,
   "2":teacher.func_view,
   "3":student.func_view
}
def run():
    print('欢迎使用oldboy选课系统,请选择你的角色:！')
    while True:
     print('''
1.管理员
2.老师
3.学生
q.退出
    ''')
     num=input("请选择你的角色>>>:").strip()
     if num == 'q':break
     if num not in  func_dic:
         print("输入不正确，请重新输入...")
         continue
     func_dic[num]()
