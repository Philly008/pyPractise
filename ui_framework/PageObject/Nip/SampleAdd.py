# -*- coding: utf-8 -*-
# @Time       : 2019/5/30 15:07
# @Author     : Philly
# @File       : SampleAdd.py
# @Description: 
from ui_framework.PageObject import Pages
from ui_framework.Base.BaseYaml import getYam


class SampleAdd:
    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "test_msg": getYam(kwargs["path"]),
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

    def operate(self):
        self.page.operate()

    def check_point(self):
        self.page.checkPoint()
