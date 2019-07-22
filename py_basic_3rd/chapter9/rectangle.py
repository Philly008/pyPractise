# -*- coding: utf-8 -*-
# @Time       : 2019/3/27 13:16
# @Author     : Philly
# @File       : rectangle.py
# @Description: 

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)


if __name__ == '__main__':
    r = Rectangle()
    r.width = 10
    r.height = 5
    print(r.size)
    r.size = 150, 100
    print(r.width)
