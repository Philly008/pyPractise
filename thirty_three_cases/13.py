# -*- coding: utf-8 -*-
# @Time       : 2019/7/24 14:58
# @Author     : Philly
# @File       : 13.py
# @Description: 13 lines: Unit testing with unittest
import unittest


def median(pool):
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        """
         list indices must be integers or slices, not float
        When you do x / y, an integer is returned in Python 2.x because the decimal is truncated
        (floor division).However in 3.x, the / operator performs 'true' division,resulting in a float
         instead of an integer (e.g. 1 / 2 = 0.5).Therefore you may first want to try using
          middle = (first + last) // 2, adjusting so that the result returns what you expect.
        """
        return copy[(size - 1) // 2]
    else:
        return (copy[size // 2 - 1] + copy[size // 2]) // 2


class TestMedian(unittest.TestCase):
    def testMedian(self):
        self.assertEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)

if __name__ == '__main__':
    unittest.main()

