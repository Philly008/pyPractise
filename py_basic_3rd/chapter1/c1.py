# -*- coding: utf-8 -*-
# @Time       : 2019/3/26 11:49
# @Author     : Philly
# @File       : c1.py
# @Description: 
x = bytearray(b"Hello!")
x[1] = ord(b"u")    # ord获取序数值（ordinal value）
print(x)
