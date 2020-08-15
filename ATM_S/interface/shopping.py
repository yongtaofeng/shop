# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28

from  db import  db_handler
from  interface import  bank
from  lib import common
shopping_log=common.get_logger('购物')
def shooping_interface(name,cost,shoppingcart):
    flag,msg=bank.consume_interface(name,cost)
    if flag:
       user_dic=db_handler.select(name)
       user_dic['shoppingcart']=shoppingcart
       db_handler.save(user_dic)
       return True,"购买成功"
    else:
        return False,msg
def check_shoppingcart_interface(name):
    user_dic=db_handler.select(name)
    shopping_car=user_dic['shoppingcart']
    shopping_log.info("您都购买了%s"%shopping_car)
    print("您都购买了%s"%shopping_car)
