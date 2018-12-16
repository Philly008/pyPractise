# -*- coding: utf-8 -*-
# @Time       : 2018/12/15 18:23
# @Author     : Philly
# @File       : chp2_1.py
# @Description: 
"""
setUpClass() and tearDownClass() methods an using the @classmethod
decorator allow us to initialize values at the class level
"""
import unittest
from selenium import webdriver


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get("http://www.baidu.com")
        cls.driver.title

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()

        # get all the anchor elements which have product names
        # displayed currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("")
        self.assertEqual(2, len(products))

    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()

        # get all the anchor elements which have product names
        # displayed currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("")
        self.assertEqual(2, len(products))

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
