#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt



import logging.config
from conf import  settings

def logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger1=logging.getLogger(name)
    return  logger1