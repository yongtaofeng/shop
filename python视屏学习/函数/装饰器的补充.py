# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28

import time
from functools import  wraps #用来使用帮助信息

def deco(func):
   @wraps(func)
   def outter2(func2):
        print('outter2')
        def wrapper2(*args,**kwargs):
            print('wrapper2')
            res2=func2(*args,**kwargs)
            return res2
        return wrapper2




def index():
    '''
    登录页面的首页
    author：fyt
    啊哈哈哈
    :return:
    '''
    print('welcome to index page')
    time.sleep(3)

print(index.__name__)
print(index.__doc__)
index()