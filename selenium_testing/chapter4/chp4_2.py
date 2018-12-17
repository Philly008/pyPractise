# -*- coding: utf-8 -*-
# @Time       : 2018/12/17 22:55
# @Author     : Philly
# @File       : chp4_2.py
# @Description: alert class
from selenium import webdriver
import unittest


class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.FireFox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("")

    def test_compare_products_removal_alert(self):
        # get the search textbox
        search_field = self.driver.find_element_by_name("")
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys("phones")
        search_field.submit()

        # click the Add to compare link
        self.driver.find_element_by_link_text("").click()

        # click on Remove this item link, this will display an lert to the user
        self.driver.find_element_by_link_text("").click()

        # switch to the alert
        alert = self.driver.switch_to_alert()

        # get the text from alert
        alert_text = alert.text

        # check alert text
        self.assertEqual("Are you", alert_text)

        # click on OK button
        alert.accept()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
