# -*- coding: utf-8 -*-
# @Time       : 2019/5/29 15:53
# @Author     : Philly
# @File       : LoginFailPage.py
# @Description: 
from ui_framework.PageObject import Pages
from ui_framework.Base.BaseYaml import getYam


class LoginFailPage:
    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "test_msg": getYam(kwargs["path"]),
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

    def operate(self):  # 操作步骤
        self.page.operate()

    def checkPoint(self):  # 检查点
        self.page.checkPoint()


if __name__ == "__main__":
    pass

