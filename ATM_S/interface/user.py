# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28
from db import db_handler


def register_interface(name, password, balnace=15000):
    user = db_handler.select(name)
    if user:
        return False, "用户已经存在"
    user_dic = {'name': name, 'password': password, 'balance': balnace, 'credit': balnace, 'locked': False,
                'bankflow': [], 'shoppingcart': {}}
    db_handler.save(user_dic)
    return True, "注册成功"


def login_interface(name, password):
    user_dic = db_handler.select(name)
    if user_dic:
        if user_dic["password"] == password and not user_dic['locked']:

            return True, "登录成功"
        else:
            return False, "密码错误或者账户被锁定"

    else:
        return False, "用户不存在"


def lock_user(name):
    user_dic = db_handler.select(name)
    if user_dic:
        user_dic['locked'] = True
        db_handler.save(user_dic)


def unlock_user(name):
    user_dic = db_handler.select(name)
    if user_dic:
        user_dic['locked'] = True
        db_handler.save(user_dic)
        return True, "账户解锁成功"
    else:
        return False, "用户不存在"
