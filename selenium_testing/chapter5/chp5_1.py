# -*- coding: utf-8 -*-
# @Time       : 2018/12/18 13:38
# @Author     : Philly
# @File       : chp5_1.py
# @Description: WebDriverWait expected_conditions classes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest


class ExplicitWaitTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("")

    def test_account_link(self):
        WebDriverWait(self.driver, 10).until(lambda s:\
            s.find_element_by_id("").get_attribute("") == "3")

        account = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located == ""
        )
        account.click()

    def test_create_new_customer(self):
        # click on Log In link to open Login page
        self.driver.find_element_by_link_text("")

        # wait for My Account link in Menu
        my_account = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located == ""
        )
        my_account.click()

        # get the Create Account button
        create_account_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable == ""
        )

        # click on Create Account button. This will displayed new account
        create_account_button.click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.title_contains("New Customer")
        )



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)

