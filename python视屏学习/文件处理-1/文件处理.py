#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#1.什么是文件
#     文件是操作系统为用户/应用程序提供的一种操作硬盘的抽象单位

#2.为何要使用文件
   # 用户/应用程序对文件的读写操作会有操作系统转换成具体的硬盘操作
   #所以用户/应用程序可以通过简单的读\写文件来间接的控制复杂的硬盘的存取操作，
   #实现将内存中的数据永久保存到磁盘中
#3.如和使用文件
#open(r'文件路径)

# f=open(r'a.txt',encoding='utf-8')
# #print(f) #f的值是一个文件对象
# res=f.read()
# print(res)
# f.close() #向操作系统发送请求，要求操作系统关闭打开文件
#强调：一定要在程序结束之前关闭打开文件

#上下文管理文件
# with open(r'a.txt',encoding='utf-8') as f,\
#      open(r'b.txt',encoding='utf-8') as f2: #打开多个文件，并且不需要f.close()
#     print(f.read())#读写文件，向操作系统发送读写文件指令
#     print(f2.read())



#文件详细操作
'''
1.文件的打开模式
 #r:只读模式，默认模式
 #w：只写模式
 #a：追加写
 控制读写文件单位的方式
 1.t:以文本为单位(默认的必须以r|a|w联合使用) 优点：操作系统会将硬盘中二进制数字解码成unicode然后返回
  强调:只针对文本文件
 2.b:以bytes为单位 ，（二进制模式)使用bytes是不用解码,也就是不用指定encoding参数

'''
# with open('a.txt',mode='r',encoding='utf-8') as f:
#     print(f.read())
#
#
# with open('a.txt',mode='w',encoding='utf-8')as f1:
#     f1.write('zsp')

#可读可写模式
'''
r+t:
w+t:
a+t:
'''
# with open('a.txt',mode='r+',encoding='utf-8') as f:
#     # print(f.readable())
#     # print(f.writable())
#     msg=f.readline()
#     print(msg)
#     f.write('xxxxx\n')

#控制文件内的指针移动 f.seek
#文件内指针移动，只有在t模式下的read(n）,n代表的字符的个数，
#其余的都是以字节为单位
# with open('a.txt',mode='r',encoding='utf-8') as f:
#     msg=f.read(1)

#f.seek有两个参数：
#  1.offset:代表指针移动的字节数
#  2.代表的是参照那个位置进行移动
#whence有三个值：
#  0：代表参照文件开头（默认的) #都可以在b和t模式下
#  1：代表参照当前所在的位置 #都必须是在b模式下
#  2：代表参照文件末尾 #都必须在b模式下

# with open('a.txt',mode='r',encoding='utf-8') as f:
#     f.seek(2,0)
#     res=f.read(1)
#     print(res)

# with open('a.txt',mode='rb') as f:
#     f.seek(3,0)
#     res=f.read(3)
#     print(res.decode('utf-8'))

# with open('a.txt',mode='rt',encoding='utf-8') as f:
#      f.seek(6,0)
#      print(f.tell())
#      print(f.read(1))

# with open('a.txt',mode='rb') as f:
#      #f.seek(6,0)
#      print(f.tell())
#      f.seek(3,1)
#      print(f.tell())
#      print(f.read(3))

# with open('a.txt',mode='rb') as f:
#      f.seek(0,2)
#      print(f.tell())
#      f.seek(-6,2)
#      print(f.tell())
#      msg=f.read(6)
#      print(msg.decode('utf-8'))

#文件截断
# with open('a.txt',mode='r+',encoding='utf-8') as f:
#       f.truncate(2)

#修改文件的两种方式
# with open('a.txt',mode='r+',encoding='utf-8') as f :
#     f.seek(1,0)
#     f.write('fyt')
#修改文件方式一：将文件内容有硬盘全部读入内存
#在内存中完成修改
#将内存修改的结果覆盖写回硬盘

#错误的做法
# with open('a.txt',mode='r',encoding='utf-8') as f:
#     all_date=f.read()
# with open('a.txt',mode='w',encoding='utf-8') as f1:
#     f1.write(all_date.replace('Alex','fyt'))
#方式一缺点：占用内存过多，不适用于大文件
#优点：在文件修改过程中硬盘始终一份数据
#正确做法
#方式二
#有点：同一时刻在内存中只存在源文件的一行内容，不会过多的占用内存
#缺点：在文件修改的过程中会出现源文件与临时文件在硬盘上同一时刻会有两份数据，即在修改的过程中会过多的占用硬盘
# import os
#
# with open('a.txt',mode='r',encoding='utf-8') as old_f,open('d.txt',mode='w',encoding='utf-8') as new_f:
#     for line in old_f:
#         new_f.write(line.replace('fyt','Alex'))
# os.remove('a.txt')
# os.rename('d.txt','a.txt')