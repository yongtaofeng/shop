#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

import os
import sys

DIR_path = os.path.dirname(__file__)
sys.path.append(DIR_path)
from  core import src

if __name__ == '__main__':
    src.run()