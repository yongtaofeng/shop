#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
#模块搜索路径的优先级
#1.内存中已经加载过的
#sys.path #第一个值是当前执行文件所在的文件夹

import sys
sys.path.append(r'E:\python视屏学习\文件处理-1')
import n
print(n.head)

#模块的绝对路径
#所有被导入的模块参照环境变量sys.path都是以执行文件为准的
