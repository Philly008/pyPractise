# -*- coding: utf-8 -*-
# @Time       : 2018/12/20 11:39
# @Author     : Philly
# @File       : chp9_5.py
# @Description: 调用JavaScript
from selenium import webdriver
import unittest


class ExecuteJavaScriptTest(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("")

    def test_search_by_category(self):
        # get the search textbox
        search_field = self.driver.find_element_by_name("q")
        self.highlightElement(search_field)
        search_field.clear()

        # enter search keyword and submit
        self.highlightElement(search_field)
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

    def highlightElement(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style',"
                                   "arguments[1]);",
                                   element, "color: green;"
                                            "border: 2px solid green;")
        self.driver.execute_script("arguments[0].setAttribute('style',"
                                   "arguments[1]);", element , "")

if __name__ == "__main__":
    unittest.main(verbosity=2)
