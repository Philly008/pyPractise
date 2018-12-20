# -*- coding: utf-8 -*-
# @Time       : 2018/12/19 10:53
# @Author     : Philly
# @File       : basetestcase.py
# @Description: The page objects pattern
import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("")

    def tearDown(self):
        # close the browser window
        self.driver.quit()

