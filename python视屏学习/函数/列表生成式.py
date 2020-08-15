# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28

# names=['alex_sb','lqh_sb','yhh']
# l=[]
# # for i in names:
# #     res=i+'_dsb'
# #     l.append(res)
# # print(l)

# l=[name+'_dsb' for name in names] #列表生成数
# print(l)

# for name in names:
#     if name.endswith('sb'):
#         l.append(name)
# print(l)

# l=[name for name in names if name.endswith('sb')]
# print(l)
#
# 1、将names=['egon','alex_sb','wupeiqi','yuanhao']中的名字全部变大写
#
# 2、将names=['egon','alex_sb','wupeiqi','yuanhao']中以sb结尾的名字过滤掉，然后保存剩下的名字长度
#
# 3、求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
#


# names=['egon','alex_sb','wupeiqi','yuanhao']
# l=[name.upper() for name in names ]
# print(l)
# names=['egon','alex_sb','wupeiqi','yuanhao']
# l=[len(name) for name in names  if not name.endswith('sb')]
# print(l)


# with open('a.txt',encoding='utf-8') as f:
#     l=[len(line) for line in f]
# print(l)

#字典生成数
keys=['name','age']
vals=['fyt',18]
# dic={}
# for i,k in enumerate(keys):
#     dic[k]=vals[i]
#
# print(dic)

# dic={k:vals[i] for i,k in enumerate(keys)}
# print(dic)
#集合生成式
l={i for i in range(10)}
print(l)
