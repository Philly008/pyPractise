# -*- coding: utf-8 -*-
# @Time       : 2019/5/28 10:21
# @Author     : Philly
# @File       : runner.py
# @Description:
import sys
sys.path.append("..")
from ui_framework.Base.BaseInit import mk_file
from ui_framework.Base.BaseStatistics import countDate, writeExcel
from datetime import datetime
import unittest
from ui_framework.Base.BaseRunner import ParameterizedTestCase
# 如果from ui_framework.TestCase import HomeTest会无法执行到用例
from ui_framework.TestCase.HomeTest import HomeTest
from ui_framework.TestCase.NipTest import NipTest


def runnerCaseApp():
    start_time = datetime.now()
    suite = unittest.TestSuite()
    # suite.addTest(ParameterizedTestCase.parameterize(HomeTest))
    suite.addTest(ParameterizedTestCase.parameterize(NipTest))
    unittest.TextTestRunner(verbosity=2).run(suite)
    end_time = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((end_time - start_time).seconds) + "秒")


if __name__ == '__main__':
    mk_file()
    runnerCaseApp()
    writeExcel()
