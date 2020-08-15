#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
from  conf import  settings
import time
def logger(msg):
    with open(settings.file,mode='a',encoding='utf-8') as f:
        f.write('%s%s\n'%(time.strftime('%Y-%m-%d %H:%M:%S %p'),msg))