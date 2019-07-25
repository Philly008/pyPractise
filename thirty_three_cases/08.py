# -*- coding: utf-8 -*-
# @Time       : 2019/7/24 14:06
# @Author     : Philly
# @File       : 08.py
# @Description: 8 lines: Command line arguments, exception handling
# This program adds up integers in the command line
import sys
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print('sum = ', + total)
except ValueError:
    print('Please supply integer arguments')


