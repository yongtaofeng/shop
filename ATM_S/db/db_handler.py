# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28

import json,os
from conf import settings

def save(user_dic):
    path = os.path.join(settings.DIR_DB, '%s.json' %user_dic['name'])
    with open(path, mode='w', encoding='utf-8') as f:
       json.dump(user_dic, f)
def select(name):
    path = os.path.join(settings.DIR_DB, '%s.json' %name)
    if os.path.exists(path):
        with open(path,mode='r',encoding='utf-8') as f:
            user_dic=json.load(f)
            return user_dic
    else:
        return False
