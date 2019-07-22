# -*- coding: utf-8 -*-
# @Time       : 2019/5/28 11:19
# @Author     : Philly
# @File       : BasePickle.py
# @Description: 
import pickle
import os


def write(data, path="data.pickle"):
    with open(path, 'wb') as f:
        pickle.dump(data, f, 0)


def read(path):
    data = {}
    with open(path, 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = {}
    return data


def readInfo(path):
    data = []
    with open(path, 'rb') as f:
        try:
            data = pickle.load(f)
            print(data)
        except EOFError:
            data = []
    return data


def writeInfo(data="", path="data.pickle"):
    _read = readInfo(path)
    result = []
    if _read:
        _read.append(data)
        result = _read
    else:
        result.append(data)
    with open(path, 'wb') as f:
        pickle.dump(result, f)


if __name__ == "__main__":
    write("用例失败重连过一次，失败原因：", "../Log/connect64dd15b8-ca91-11e7-87ae-38c98647adce.pickle")


