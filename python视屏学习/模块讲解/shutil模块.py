#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
'''
  shutil模块：
     用于简化文件操作 （文件的高级操作)

'''
import shutil
#2.shutil.copyfile(文件1，文件2)：不用打开文件，直接用文件名进行覆盖copy
#shutil.copyfile('a.txt','b.txt')

#shutil.copyfileobj(文件1，文件2)：将文件1的数据覆盖copy给文件2
# f1 = open("a.txt",encoding="utf-8")
#
# f2 = open("b.txt","w",encoding="utf-8")
#
# shutil.copyfileobj(f1,f2)
#shutil.copymode(文件1，文件2)：之拷贝权限，内容组，用户，均不变
#shutil.copystat(文件1，文件)：只拷贝了权限。
#shutil.copy(文件1，文件2)：拷贝文件和权限都进行copy
#.shutil.copy2(文件1，文件2)：拷贝了文件和状态信息
#shutil.copytree(源目录，目标目录)：可以递归copy多个目录到指定目录下
#shutil.rmtree(目标目录)：可以递归删除目录下的目录及文件。
#shutil.move(源文件，指定路径)：递归移动一个文件。
#shutil.make_archive()：可以压缩，打包目录
shutil.make_archive("test","zip","E:\python视屏学习\模块讲解")\

#另外也可以用zipfile模块，指定具体要压缩的文件

#_*_coding:utf-8_*_
# 2 #__author__ = "csy"
# 3
# 4 import zipfile
# 5 z = zipfile.ZipFile("5.zip","w")
# 6 z.write("1.txt")
# 7 print("=========~~~~~~~~~~")
# 8 z.write("3.txt")
# 9 z.close()

#解压
# #_*_coding:utf-8_*_
# 2 #__author__ = "csy"
# 3
# 4 import zipfile
# 5 z = zipfile.ZipFile("5.zip","r")
# 6 z.extractall()
# 7 z.close()