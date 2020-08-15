#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

'''
    1 先循环打印出商品
    2 用户输入数字选择商品（判断是否是数字，判断输入的数字是否在范围内）
    3 取出商品名，商品价格
    4 判断用户余额是否大于商品价格
    5 余额大于商品价格时，判断此商品是否在购物车里
        5.1 在购物车里，个数加1
        5.1 不在购物车里，拼出字典放入（｛‘car’：｛‘price’：1000，‘count’：2｝,‘iphone’：｛‘price’：10，‘count’：1｝｝）
    6 用户余额减掉商品价格
    7 花费加上商品价格
    8 当输入 q时，购买商品
        8.1 消费为0 ，直接退出
        8.2 打印购物车
        8.3 接受用户输入，是否购买 当输入y，直接调购物接口实现购物
    :return:

'''

def shop():
    good_list = [
        ['coffee', 10],
        ['chicken', 20],
        ['iphone', 8000],
        ['macPro', 15000],
        ['car', 100000]
    ]
    for i, good in enumerate(good_list):
        print(i, good)



shop()

print(16000 - 1500)