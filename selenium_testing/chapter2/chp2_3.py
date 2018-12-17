# -*- coding: utf-8 -*-
# @Time       : 2018/12/15 18:23
# @Author     : Philly
# @File       : chp2_3.py
# @Description: 
"""
TestSuite
TestLoader
TestRunner
"""
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get("XXX")

    def test_search_field(self):
        # check search field exists on Home page
        self.assertTrue(self.is_element_present(By.NAME))

    def test_language_option(self):
        # check language options dropdown on Home page
        self.assertTrue(self.is_element_present(By.ID, 'language'))

    def test_shopping_cart_empty_message(self):
        # check content of My Shopping Cart block on Home page
        shopping_cart_icon = \
        self.driver.find_element_by_css_selector("XX")
        shopping_cart_icon.click()
        shopping_car_status = self.driver.find_element_by_css_selector("XX")
        self.assertEqual("XX", shopping_car_status)

        close_button = self.driver.find_element_by_css_selector("XX")
        close_button.click()

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :param how: By locator type
        :param what: locator value
        :return:
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity=2)

