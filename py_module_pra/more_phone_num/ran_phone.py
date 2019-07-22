# -*- coding: utf-8 -*-
# @Time       : 2019/6/27 13:09
# @Author     : Philly
# @File       : ran_phone.py
# @Description: 

# -*- coding: utf-8 -*-
__author__ = 'Administrator'
__time__ = '2018-05-07 下午 4:20'
import string
import random

Mobile = []

for i in range(18018000000, 18018000005, 1):
    Mobile.append(i)
    f = open('phone_num.txt', 'w', encoding='utf-8')
for i in Mobile:
    f.write(str(i) + "\n")

    print(str(i))
f.close()
