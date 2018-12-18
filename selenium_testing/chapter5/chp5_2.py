# -*- coding: utf-8 -*-
# @Time       : 2018/12/18 14:05
# @Author     : Philly
# @File       : chp5_2.py
# @Description: Waiting for alerts
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import unittest


class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("")

    def test_compare_products_removal_alert(self):
        # get the search textbox
        search_field = self.driver.find_element_by_name("q")
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys("phones")
        search_field.submit()

        # click the Add to compare link
        self.driver.find_element_by_link_text("").click()

        # wait for Clear All link to be visible
        clear_all_link = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located == ""
        )

        # click on Clear All link, this will display an alert to the user
        clear_all_link.click()

        # wait for the alert to present
        alert = WebDriverWait(self.driver, 10).until(
            expected_conditions.alert_is_present()
        )

        # get the text from alert
        alert_text = alert.text

        # check alert text
        self.assertEqual("", alert_text)
        # click on Ok button
        alert.accept()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

