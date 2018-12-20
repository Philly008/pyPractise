# -*- coding: utf-8 -*-
# @Time       : 2018/12/20 14:18
# @Author     : Philly
# @File       : chp9_8.py
# @Description: 弹出窗的处理
from selenium import webdriver
import unittest


class PopupWindowTest(unittest.TestCase):
    URL = "http://www.baidu.com"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def test_popup_window(self):
        driver = self.driver

        # save the WindowHandle of Parent Browser Window
        parent_window_id = driver.current_window_handle

        # clicking News link will open News Page in a new Popup Browser Window
        help_button = driver.find_element_by_link_text("新闻")
        help_button.click()
        driver.switch_to.window("百度新闻——全球最大的中文新闻平台")
        driver.close()
        driver.switch_to.window(parent_window_id)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)

