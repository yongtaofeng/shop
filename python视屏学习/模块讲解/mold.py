#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

# def f1():
#     print("f1")
# def f2():
#     print("f2")
# #当文件被执行是 name==main
# #当文件被导入时：
# print(__name__)
#
# # if "__name__"=="__main__":
# #     f1()
# #     f2()
# if __name__ == '__main__':
#     f1()
#     f2()

#模块的绝对导入和模块的相对导入
#相对导入：参照当前所在文件夹为起始开始查找哦，称之为相对导入
       #缺点：只能在被导入的模块中使用，不能在执行文件中用
       #优点：导入更加简单