# -*- coding: utf-8 -*-
# @Time       : 2018/12/19 8:00
# @Author     : Philly
# @File       : chp8_1.py
# @Description: 
"""
To create a data-driven test we need to use the @ddt decorator for the test class
and use the @data decorator on the data-driven test methods
For lists, we need to use the @unpack decorator, which unpacks
tuples or lists into multiple arguments
"""
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver


@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("")

    # specify test data using @data decorator
    @data(("phones", 2), ("music", 5))
    @unpack
    def test_search(self, search_value, expected_count):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        # enter search keyword and submit.
        # use search_value argument to pass data
        self.search_field.send_keys(search_value)
        self.search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("")

        # check count of products shown in results
        self.assertEqual(expected_count, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
