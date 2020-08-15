#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#语法：
# if 条件：
#     代码1
#     代码2
#     代码3
#if嵌套
cls="human"
sex="female"
age=18
success=False
if cls=="human" and sex=="female" and age >16 and age <20:
    print("开始表白")
    if success:
        print("在一起")
    else:
        print("从新找下家")
else:
    print("阿姨好")
print("end ....")

# if 条件：
#     代码1
#     代码2
#     代码3
# elif 条件：
#     代码1
#     代码2
# else:
#     代码1
#     代码2
# if cls=="human" and sex=="female" and age >16 and age <20:
#     print("开始表白")
# else:
#     print("阿姨好")

# today=input('>>>:')
# if today in ['Saturday','Sunday']:
#     print("出去浪")
# elif today in ['Monday','Tuesday','Wednesday','Thursday','Friday']:
#     print("上班")
# else:
#     print('''必须输入其中的一个
#     Monday
#     Tuesday
#     Wednesday
#     Thursday
#     Friday
#     Saturday
#     Sunday
#     ''')