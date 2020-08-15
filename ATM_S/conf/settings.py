# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28
import os
DIR_PATH=os.path.dirname(os.path.dirname(__file__))
DIR_DB=os.path.join(DIR_PATH,'db')
DIR_LOG=os.path.join(DIR_PATH,'log')



standard_format = '[%(asctime)s] - [task:%(name)s] - [%(filename)s]:[%(lineno)d] -' \
                  ' [%(levelname)s] : [%(message)s]'

simple_format = '%(filename)s:%(lineno)d - %(levelname)s : [%(message)s]'


fh1_path =os.path.join(DIR_LOG,'ATM.log')


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
        # #打印到终端的日志
        # 'ch': {
        #     'level': 'DEBUG',
        #     'class': 'logging.StreamHandler',  # 打印到终端
        #     'formatter': 'simple'
        # },
        #打印到a1.log文件的日志
        'fh1': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': fh1_path,  # 日志文件的路径
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        '': {
            'handlers': ['fh1'],
            'level': 'DEBUG',
        },
    },
}

