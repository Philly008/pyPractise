# -*- coding: utf-8 -*-
# @Time       : 2019/7/24 13:52
# @Author     : Philly
# @File       : 04.py
# @Description: 4 lines: Fibonacci, tuple assignment
parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)
