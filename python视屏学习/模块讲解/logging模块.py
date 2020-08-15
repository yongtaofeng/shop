#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

import logging
# logging.basicConfig(filename='accesss.log',
#                     format='%(asctime)s- %(name)s - %(levelname)s -%(module)s: %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     level=10,
#                     )
#
#
#
#
# logging.debug('debug日志')
# logging.info('info日志')
# logging.warning("警告日志")
# logging.error("错误日志")
# logging.critical("严重日志")

'''
loggger对象：负责生产各种级别的日志
filter对象：
'''

logger1=logging.getLogger('用户交易') #日志名用来标识日志的与什么业务有关
#handler对象，控制日志输出的位置
fh1=logging.FileHandler('a.log',encoding='utf-8')
fh2=logging.FileHandler('b.log',encoding='utf-8')
ch=logging.StreamHandler()


formatter1=logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p'
)
formatter2 = logging.Formatter(
    fmt='%(asctime)s - %(levelname)s :  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p'
)



logger1.addHandler(fh1)
logger1.addHandler(fh2)
logger1.addHandler(ch)

fh1.setFormatter(formatter1)
fh2.setFormatter(formatter1)
ch.setFormatter(formatter2)


logger1.setLevel(10)
fh1.setLevel(10)
fh2.setLevel(10)
ch.setLevel(10)

logger1.info('alex给egon转账1个亿')