# -*- coding: utf-8 -*-
# @Time       : 2019/5/10 17:02
# @Author     : Philly
# @File       : util.py
# @Description: 一个文本块生成器
def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []



