#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
import  sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(sys.path)

from  core import  src
import logging.config

if __name__ == '__main__':
    src.run()
