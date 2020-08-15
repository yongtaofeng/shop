#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
from db import  modles
from  lib import common
#改模款用来处理admin模块业务逻辑
def admin_register(name,passwd):
    #判断这个管理员是否存在
    file_names=common.get_all_fileName(modles.Admin.__name__.lower())
    if name in file_names:
        return
    admin=modles.Admin(name,passwd)
    #存储到文件 但是存储到文件这个功能大家都需要
    #必须明确存储路径

    return admin