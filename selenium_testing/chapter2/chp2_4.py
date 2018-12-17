# -*- coding: utf-8 -*-
# @Time       : 2018/12/15 18:23
# @Author     : Philly
# @File       : chp2_4.py
# @Description:
"""
TestSuite
HTMLTestRunner
"""
import unittest
import os
from selenium_testing.chapter2 import HTMLTestRunner
from selenium_testing.chapter2.chp2_2 import SearchTests
from selenium_testing.chapter2.chp2_3 import HomePageTest


# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# open the report file
outfile = open(dir + "SmokeTestReport.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title='Test Report',
    description='Smoke Tests'
)

# run the suite using HTMLTestRunner
runner.run(smoke_tests)

# run the suite
# unittest.TextTestRunner(verbosity=2).run(smoke_tests)
