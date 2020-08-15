#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

import sys
sys.path.append('E:\python视屏学习\包的使用\dir1\dir2')
import p
# p.f1()


'''
包的使用注意两点：
   1.导入包就是在导包下的__init__.py文件
   2.使用绝对导入，绝对导入的其实位置都是以包的紧急目录为起点
   3.但是包内部模块的导入通常使用相对导入，用.代表当前所在文件(而非执行文件)...代表上一级
   #强调：相对导入只能包内部的模块之间的相互导入
   #..上一级不能超出顶级包
'''
p.m2()