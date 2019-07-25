# -*- coding: utf-8 -*-
# @Time       : 2019/7/24 14:50
# @Author     : Philly
# @File       : 11.py
# @Description: 11 lines: Triple-quoted strings, while loop
REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''
bottles_of_beer = 3
while bottles_of_beer > 1:
    print(REFRAIN % (bottles_of_beer, bottles_of_beer, bottles_of_beer - 1))
    bottles_of_beer -= 1

