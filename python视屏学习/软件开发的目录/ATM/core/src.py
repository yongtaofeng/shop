#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
import time
from  lib import  common

def register():
    print("注册")


def login():
    print('denglu')


def shopping():
    print("购物")


def pay():
    print("支付")

def transfer():
    print('转账')
    common.logger('alex给egion装了100亿')
func_dic={
    '1':register,
    '2':login,
    '3':shopping,
    '4':pay,
    '5':transfer
}

def run():
    while True:
        print('''
        0 退出
        1 注册
        2 登录
        3 购物
        4 支付
        5 转账
        ''')
        choicok=input("请输入你的操作:".strip())
        if choicok=='0':break
        if choicok not in func_dic:
            print("此功能没有开发")
        else:
            func_dic[choicok]()
