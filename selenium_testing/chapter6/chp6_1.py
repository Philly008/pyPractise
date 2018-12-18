# -*- coding: utf-8 -*-
# @Time       : 2018/12/18 15:15
# @Author     : Philly
# @File       : chp6_1.py
# @Description: 
import sys
import unittest
from selenium import webdriver


class SearchProducts(unittest.TestCase):
    PLATFORM = 'WINDOWS'
    BROWSER = 'firefox'

    # run on Sauce Lab's cloud
    SAUCE_USERNAME = 'AAA'
    SAUCE_KEY = 'mm'

    def setUp(self):
        desired_caps = {}
        desired_caps['platform'] = self.PLATFORM
        desired_caps['browser'] = self.BROWSER
        sauce_string = self.SAUCE_USERNAME + ':' + self.SAUCE_KEY

        # sauce lab 云上执行用例
        self.driver = webdriver.remote('http://' + sauce_string + 'XXx', desired_caps)
        # self.driver = webdriver.remote('http://xxx:4444')
        self.driver.get('')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def testSearchByCategory(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys('phones')
        self.search_field.submit()

        # get all the anchor elements
        products = self.driver.find_elements_by_xpath("")

        # check count of products shown in results
        self.assertEqual(2, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        SearchProducts.BROWSER = sys.argv.pop()
        SearchProducts.PLATFORM = sys.argv.pop()

    unittest.main(verbosity=2)

