# -*- coding: utf-8 -*-
# @Time       : 2019/7/24 14:00
# @Author     : Philly
# @File       : 07.py
# @Description: 7 lines: Dictionaries, generator expressions
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6
}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)

