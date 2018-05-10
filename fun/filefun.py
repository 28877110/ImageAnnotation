#coding: utf-8
import json
import os

def saveJsonToFile(filename,jsondata):
    with open(filename,'w',encoding='utf-8') as f:
        json.dump(jsondata,f)
        print("保存成功")


def readJsonInFile(filename):
    if os.path.exists(filename) :
        with open(filename, 'r',encoding="utf-8") as load_f:
            load_dict = json.load(load_f)
            print(load_dict)
            return load_dict
    else:
        return {}


def filetypetojson(filepath):
    if filepath is not None:
        type = os.path.splitext(filepath)[1]
        filename = os.path.splitext(filepath)[0]
        newname = os.path.join(filename + '.json')
        print('最后的文件名字',newname)
    return newname