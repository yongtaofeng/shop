# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28

import sys
import os
base_path=os.path.dirname(__file__)
sys.path.append(base_path)
from  core import src
if '__main__' == __name__:
   src.run()