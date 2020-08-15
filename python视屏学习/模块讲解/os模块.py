
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

'''
OS模块：OS表示操作系统相关
        第一大块功能就是围绕文件目录的操作：
'''
import os
print(os.path.dirname(os.path.dirname(__file__)))
print(os.path.join(os.getcwd(),os.path.pardir))
print(os.getcwd())