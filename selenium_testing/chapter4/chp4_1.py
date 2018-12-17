# -*- coding: utf-8 -*-
# @Time       : 2018/12/17 16:37
# @Author     : Philly
# @File       : chp4_1.py
# @Description: 
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select


class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("")

    def test_register_new_user(self):
        driver = self.driver
        # click on Log In link to open Login page
        driver.find_element_by_link_text("").click()

        # get the Create Account button
        create_account_button = driver.find_element_by_xpath("")
        # check Create Account button is displayed and enabled
        self.assertTrue(create_account_button.is_displayed()) and create_account_button.is_enabled()

        # click on Create Account button. This will display new account
        create_account_button.click()
        # check title
        self.assertEquals("Create", driver.title)

        # get all the fields from Create an Account form
        first_name = driver.find_element_by_id("")
        last_name = driver.find_element_by_id("")
        email_address = driver.find_element_by_id("")
        news_letter_subscription = driver.find_element_by_id("")
        password = driver.find_element_by_id("")
        confirm_password = driver.find_element_by_id("")
        submit_button = driver.find_element_by_xpath("")

        # check maxlength of first name and last name textbox
        self.assertEqual("255", first_name.get_attribute("maxlength"))
        self.assertEqual("255", last_name.get_attribute("maxlength"))

        # check all fields are enabled
        self.assertTrue(first_name.is_enabled() and last_name.is_enabled())

        # check Sign Up for Newsletter is unchecked
        self.assertFalse(news_letter_subscription.is_selected())

        # fill out all the fields
        first_name.send_keys("Test")
        news_letter_subscription.click()

        # check new user is registered
        self.assertEqual("Hello,", driver.find_element_by_css_selector("").text)
        self.assertTrue(driver.find_element_by_link_text("").is_displayed())

    def test_language_options(self):
        # list of expected values in Language dropdown
        exp_options = ["ENGLISH", "FRENCH", "GERMAN"]
        # empty list for capturing actual options displayed in th dropdown
        act_options = []

        # get the Your language dropdown as instance of Select class
        select_language = Select(self.driver.find_element_by_id(""))
        # check number of options in dropdown
        self.assertEqual(2, len(select_language.options))

        # get options in a list
        for option in select_language.options:
            act_options.append(option.text)

        # check expected options list with actual options list
        self.assertListEqual(exp_options, act_options)

        # check default selected option is English
        self.assertEqual("ENGLISH", select_language.first_selected_option.text)

        # select an option using select_by_visible_text
        select_language.select_by_visible_text("German")

        # check store is now German
        self.assertTrue("store=german" in self.driver.current_url)

        # changing language will refresh the page,
        # we need to get find language dropdown once again
        select_language = \
        Select(self.driver.find_element_by_id("X"))
        select_language.select_by_index(0)






    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':

    unittest.main(verbosity=2)

