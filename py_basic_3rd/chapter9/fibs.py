# -*- coding: utf-8 -*-
# @Time       : 2019/3/27 17:35
# @Author     : Philly
# @File       : fibs.py
# @Description: 斐波那契数列
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


if __name__ == '__main__':
    fibs = Fibs()
    # 找出第一个大于1000的斐波那契数
    for f in fibs:
        if f > 1000:
            print(f)
            break
