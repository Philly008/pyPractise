# -*- coding: utf-8 -*-
# @Time       : 2018/12/19 11:18
# @Author     : Philly
# @File       : homepage.py
# @Description: 
from selenium_testing.chapter8.base import BasePage
from selenium_testing.chapter8.base import InvalidPageException


class HomePage(BasePage):
    _home_page_slideshow_locator = 'div.slideshow-container'

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def _validate_page(self, driver):
        try:
            driver.find_element_by_class_name(self._home_page_slideshow_locator)
        except:
            raise InvalidPageException("Home Page not loaded")
