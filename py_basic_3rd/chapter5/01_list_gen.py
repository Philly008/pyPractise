# -*- coding: utf-8 -*-
# @Time       : 2019/3/26 17:03
# @Author     : Philly
# @File       : 01_list_gen.py
# @Description: 将名字的首字母相同的男孩和女孩配对。
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

