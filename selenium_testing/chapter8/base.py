# -*- coding: utf-8 -*-
# @Time       : 2018/12/19 10:56
# @Author     : Philly
# @File       : base.py
# @Description: 
from abc import abstractmethod


class BasePage(object):
    """ All page objects inherit from this """
    def __init__(self, driver):
        self._validate_page(driver)
        self.driver = driver

    @abstractmethod
    def _validate_page(self, driver):
        return

    """
    Regions define functionality available throughall page objects
    """
    @property
    def search(self):
        from selenium_testing.chapter8.search import SearchRegion
        return SearchRegion(self.driver)


class InvalidPageException(Exception):
    """ Throw this exception when you don't find the correct page """
    pass


