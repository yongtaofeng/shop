#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#字典：用途：用来记录多个值，每一个值有对应的key来描述value的作用
#2.定义方式 在{}内使用逗号隔开多个key:value，其中value可以是任意类型，而key必须是不可变类型
# dic={0:'aaa',1:'bbbb'}
# print(type(dic))
# print(dic[0])
#
# #可变类型：不可hash类型
# #不可变类型：可以hash的类型
# dic1=dict(x=1,y=2)
# print(dic1)

#字典有限掌握的 #字典可以去重
# #1.按key来取值，可存可取
# dic={'name':'egon'}
# print(dic['name'])
# dic['age']=18
# print(dic)
# #2.长度
# print(len(dic))
#
# #3.成员运算
# print('age' not in dic)
#
# #4.删除
# del dic['name']
# print(dic)
#
# #5.清空
# dic.clear()
# print(dic)
#根据key删除值
# res=dic.pop('name')
# print(dic)
# print(res) #返回最后一个值
#
# dic={'name':'egon','age':18}
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# for i in dic.items():
#     print(i)
#
# #字典的循环
# for k in dic.keys():
#     print(k,dic[k])
# for k,v in dic.items():
#     print(k,v)


#字典需要掌握的
#get
# dic={'name':'egon','age':18}
# # print(dic.get('name'))
#
# #
# #fromkeys
# dic1=dic.fromkeys(dic,None)
# print(dic)
#
# #update 更新老的字典更新为新的
# old={'name':'fyt','age':18}
# new={'name':'zsp','age':19,'happty':'ball'}
# old.update(new)
# print(old)

#setdefault 有则不动,返回原值，无则添加，返回新加
# l={'name':'egon','age':18}
# l.setdefault('name','aaa')
# print(l)
#
# l.setdefault('sex')
# print(l)

# res=l.setdefault('name','aaa')
# print(res)


#字典：无需 可变 存取多个值

# #练习
# l=[11,22,33,44,55,66,77,88,99]
# dic={
#     'k1':[],
#     'k2':[]
#
# }
# for i in l:
#     if i > 66:
#         dic['k1'].append(i)
#     else:
#         dic['k2'].append(i)
# print(dic)


s='hello alex alex say hello sb sb'
s1=s.split()
dic={}
#
# for i in s1:
#      if i in dic:
#           dic[i]+=1
#      else:
#         dic[i]=1
# print(dic)

for world in s1:
    dic.setdefault(world,s1.count(world))
print(dic)