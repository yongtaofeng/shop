#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt
from  conf import settings
import os
import pickle

#讲对象存储到文件
#存储在db文件夹下，每个不同的类，放在对应文件夹，文件夹的名字就是类名

def save_obj_file(obj):
    #先得到一个存储路径
    #先得到一个文件的路径

    path=os.path.join(settings.DB_DIR,obj.__class__.__name__.lower())
    if not os.path.exists(path):
        os.mkdir(path)
    file_path=os.path.join(path,obj.name)
    f=open(file_path,mode='wb')
    pickle.dump(obj,f)
    f.flush()
    f.close()


def load_obj_from_file(class_name,objName):
    #得到文件路径
    file_path=os.path.join(settings.DB_DIR,class_name.lower(),objName)
    if os.path.exists(file_path):
        f=open(file_path,mode='rb')
        obj=pickle.load(f)
        f.flush()
        f.close()
        return  obj
#用于在文件夹中查找文件名
def get_all_fileName(dirName):
    dir_path=os.path.join(settings.DB_DIR,dirName)
    if os.path.exists(dir_path):
        return os.listdir(dir_path)

if __name__ == '__main__':
    # import db.modles
    # ad=load_obj_from_file(db.modles.Admin.__name__,'zsp')
    # print(ad)
    # admin=db.modles.Admin('zsp','123')
    # save_obj_file(admin)
    a=get_all_fileName("admin")
    print(a)