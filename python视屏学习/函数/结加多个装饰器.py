# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28


import time



def outter1(func1): #func1=wrapper2
    print('outter1')
    def wrapper1(*args,**kwargs):
        print('wrapper1')
        res1=func1(*args,**kwargs) #res1=wrapper2(*args,**kwargs)
        return res1
    return wrapper1

def outter2(func2): #func2=最原始的那个index的内存地址
    print('outter2')
    def wrapper2(*args,**kwargs):
        print('wrapper2')
        res2=func2(*args,**kwargs)
        return res2
    return wrapper2


@outter1 # index=outter1(wrapper2) #index=wrapper1
@outter2 #outter2(最原始的那个index的内存地址) ===> wrapper2
def index():
    print('welcome to index page')
    time.sleep(3)

index()  #wrapper1()

'''
outter2
outter1
wrapper1
wrapper2

'''