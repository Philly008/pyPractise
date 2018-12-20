# -*- coding: utf-8 -*-
# @Time       : 2018/12/19 15:08
# @Author     : Philly
# @File       : searchtest.py
# @Description: 
import unittest
from selenium_testing.chapter8.homepage import HomePage
from selenium_testing.chapter8.basetestcase import BaseTestCase


class SearchProductTest(BaseTestCase):
    def testSearchForProduct(self):
        homepage = HomePage(self.driver)
        search_results = homepage.search.searchFor('earphones')
        self.assertEqual(2, search_results.product_count)
        product = search_results.open_product_page('MADISON')
        self.assertEqual('MADISON', product.name)
        self.assertEqual('$35.00', product.price)
        self.assertEqual('IN STOCK', product.stock_status)

if __name__ == '__main__':
    unittest.main(verbosity=2)
