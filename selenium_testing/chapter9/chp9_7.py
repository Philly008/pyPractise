# -*- coding: utf-8 -*-
# @Time       : 2018/12/20 13:51
# @Author     : Philly
# @File       : chp9_7.py
# @Description: 屏幕录制
"""
Castro是基于跨平台录制工具Pyvnc2swf开发的。它使用VNC协议录制屏幕并生成SWF视频文件
pip install PyGame
pip install Castro      # 只使用到Python2
"""
import unittest
from selenium import webdriver
from castro import Castro


class SearchProductTest(unittest.TestCase):
    def setUp(self):
        # create an instance of Castro and provide name for the output file
        self.screenCapture = Castro(filename="testSe.swf")
        # start the recording of movie
        self.screenCapture.start()

        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("http://www.baidu.com")

    def test_search_by_category(self):
        # get the search textbox
        search_field = self.driver.find_element_by_name("q")
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys("phones")
        search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("")

        # check count of products shown in results
        self.assertEqual(2, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.quit()
        # Stop the recording
        self.screenCapture.stop()

if __name__ == '__main__':
    unittest.main(verbosity=2)

