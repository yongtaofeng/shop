#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
import os

standard_format = '[%(asctime)s] - [task:%(name)s] - [%(filename)s]:[%(lineno)d] -' \
                  ' [%(levelname)s] : [%(message)s]'

simple_format = '%(filename)s:%(lineno)d - %(levelname)s : [%(message)s]'

base_path=os.path.dirname(os.path.dirname(__file__))
fh1_path =os.path.join(base_path,'log','a.log')
fh2_path =os.path.join(base_path,'log','b.log')

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'ch': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到终端
            'formatter': 'simple'
        },
        #打印到a1.log文件的日志
        'fh1': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': fh1_path,  # 日志文件的路径
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        # 打印到a2.log文件的日志
        'fh2': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'simple',
            'filename': fh2_path,  # 日志文件的路径
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },

    },
    'loggers': {
        '': {
            'handlers': ['fh1', 'fh2', 'ch'],
            'level': 'DEBUG',
        },
    },
}
