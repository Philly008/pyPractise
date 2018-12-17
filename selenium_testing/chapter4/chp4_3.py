# -*- coding: utf-8 -*-
# @Time       : 2018/12/17 23:04
# @Author     : Philly
# @File       : chp4_3.py
# @Description: navigation
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class NavigationTest(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("")

    def testBrowserNavigation(self):
        driver = self.driver
        # get the search textbox
        search_field = driver.find_element_by_name("")
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys("selenium")
        search_field.submit()

        se_wd_link = driver.find_element_by_link_text("")
        se_wd_link.click()
        self.assertEqual("", driver.title)

        driver.back()

        self.assertTrue(WebDriverWait(self.driver, 10).until(
            expected_conditions.title_is("selenium")
        ))

        driver.forward()

        self.assertTrue(WebDriverWait(self.driver, 10).until(
            expected_conditions.title_is("haha")
        ))

        driver.refresh()

        self.assertTrue(WebDriverWait(self.driver, 10).until(
            expected_conditions.title_is("lll")
        ))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



