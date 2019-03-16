# -*- coding: utf-8 -*-
# @Time       : 2019/3/8 17:22
# @Author     : Philly
# @File       : count.py
# @Description: 实现简单计算器


class Calculator():
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    # 加法
    def add(self):
        return self.a + self.b

    # 减法
    def sub(self):
        return self.a - self.b

    # 乘法
    def mul(self):
        return self.a * self.b

    # 除法
    def div(self):
        return self.a / self.b


