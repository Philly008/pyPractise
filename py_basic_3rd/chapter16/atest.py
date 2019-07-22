# -*- coding: utf-8 -*-
# @Time       : 2019/5/5 13:47
# @Author     : Philly
# @File       : atest.py
# @Description: 一个使用框架unittest的简单测试
import unittest, py_basic_3rd.chapter16.my_math as my_math


class ProductTestCase(unittest.TestCase):

    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = my_math.product(x, y)
                self.assertEqual(p, x * y, 'Integer multiplication failed')

    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x / 10
                y = y / 10
                p = my_math.product(x, y)
                self.assertEqual(p, x * y, 'Float multiplication failed')

if __name__ == '__main__': unittest.main()



