# -*- coding: utf-8 -*-
# @Time       : 2019/5/28 14:47
# @Author     : Philly
# @File       : BaseRunner.py
# @Description: 
from ui_framework.Base.BaseLog import myLog
import unittest
from selenium import webdriver
import os
from ui_framework.Base.BaseYaml import getYam


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def get_driver():
    # chromedriver = PATH("../exe/chromedriver.exe")
    # os.environ["webdriver.chrome.driver"] = chromedriver
    # driver = webdriver.Chrome(chromedriver)

    chromedriver = r"C:\Program Files (x86)\Google\68.0.3440.84gugelvse\Google Chrome\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chromedriver)

    driver.maximize_window()
    openurl = getYam(PATH("../Yamls/config.yaml"))[1]["url"]
    driver.get(openurl)
    return driver


class ParameterizedTestCase(unittest.TestCase):
    """
    TestCase classes that want to be parameterized should inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
       super(ParameterizedTestCase, self).__init__(methodName)

    @classmethod
    def setUpClass(cls):
        pass
        cls.driver = get_driver()
        cls.logTest = myLog().getLog("chrome")  # 每个设备实例化一个日志记录器

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        pass

    def tearDown(self):
        pass

    @staticmethod
    def parameterize(testcase_klass, param=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite






