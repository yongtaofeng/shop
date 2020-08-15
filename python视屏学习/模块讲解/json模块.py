#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
'''
   pickle模块：用于序列化
   序列化就是将内存中的数据持久化到硬盘
   回顾：使用文件读写也能完成吧数据持久化存储
   例如:需要把一个字典存储到硬盘中，先转换成字符串， 写入，读取为字符串，转为原始格式
   所以就有了pickle
     1.能见所有python中的数据序列化， int float str  dic  list   tuple   set bool
     2.反序列化 将之前序列化的数据，在恢复成python的数据格式
   pickle产生的数据 只能有python读取 （跨平台性差)
'''
import  pickle
import json
#序列化
users={'name':'fyt','age':23,'happy':('music','movies')}
# #print(pickle.dumps(users))
# f=open('fyt.txt',mode='wb')
# f.write(pickle.dumps(users))
# f.close()

# #反序列化
# f=open("fyt.txt",mode='rb')
# print(pickle.loads(f.read()))
# f.close()

# #序列化
# pickle.dump(users,open('pp.txt',mode='wb'))
# #反序列化
# print(pickle.load(open('pp.txt',mode='rb')))

'''
  json:是一种轻量级的数据交换格式
       1.用于处理json格式的数据模块
       json格式标准：
            能存储的有 str int  float  dic list  bool
'''
#json序列化
# f=open('zsp.txt',mode='w',encoding='utf-8')
# f.write(json.dumps(users))
# f.close()
#users=json.dumps(users)
#json反序列化
# f=open('zsp.txt',mode='r',encoding='utf-8')
# print(json.loads(f.read()))
# f.close()
# print(json.loads(users))

#son.dump(users,open('cc.txt',mode='w',encoding='utf-8'))
print(json.load(open('cc.txt',mode='r',encoding='utf-8')))