# -*- coding: utf-8 -*-
# @Time       : 2018/12/19 15:21
# @Author     : Philly
# @File       : chp9_1.py
# @Description: 键盘事件
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest


class HotkeyTest(unittest.TestCase):
    URL = ""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_hotkey(self):
        driver = self.driver

        shift_n_label = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.ID, "_shift_n"))
        )

        """
        当调用ActionChains类的方法时，它不会立即执行，而是会将所有的操作
        按顺序存放在一个队列里，当调用perform()方法时，队列的事件会依次执行。
        """
        ActionChains(driver).key_down(Keys.SHIFT).send_keys('n').key_up(
            Keys.SHIFT
        ).perform()
        self.assertEqual("rgba(12)", shift_n_label.value_of_css_property("background-color"))

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
