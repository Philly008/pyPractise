# -*- coding: utf-8 -*-
# @Time       : 2019/5/28 10:32
# @Author     : Philly
# @File       : BaseInit.py
# @Description: 
from ui_framework.Base.BaseFile import *
from ui_framework.Base.BaseElementEnum import Element
from ui_framework.Base.BasePickle import *
import datetime


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def mk_file():
    destroy()
    mkdir_file(PATH("../Log/" + Element.INFO_FILE))
    mkdir_file(PATH("../Log/" + Element.SUM_FILE))

    data = read(PATH("../Log/" + Element.INFO_FILE))

    data["version"] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    data["sum"] = 0
    data["pass"] = 0
    data["fail"] = 0
    write(data=data, path=PATH("../Log/" + Element.SUM_FILE))


def destroy():
    remove_file(PATH("../Log/" + Element.INFO_FILE))
    remove_file(PATH("../Log/" + Element.SUM_FILE))
    # remove_file(PATH("../Log/" + Element.DEVICES_FILE))


if __name__ == '__main__':
    print(destroy())
    print(mk_file())
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))