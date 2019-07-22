# -*- coding: utf-8 -*-
# @Time       : 2019/5/30 13:26
# @Author     : Philly
# @File       : NipTest.py
# @Description: 
from ui_framework.Base.BaseRunner import ParameterizedTestCase
import os
import sys
from ui_framework.PageObject.Nip.LoginPage import LoginPage


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class NipTest(ParameterizedTestCase):
    # def test_login_success(self):
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/nip/Login.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = LoginPage(app)
    #     page.operate()
    #     page.check_point()

    # 样本录入
    def test_sample_add(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/nip/SampleAdd.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginPage(app)
        page.operate()
        page.check_point()

    @classmethod
    def setUpClass(cls):
        super(NipTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(NipTest, cls).tearDownClass()

