# -*- coding: utf-8 -*-
# @Time       : 2018/12/27 7:55
# @Author     : Philly
# @File       : fibs.py
# @Description: 斐波那契数列：每个数都是前两个数的和


def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result

# 使用内置函数 callable() 判断某个对象是否可调用
print(callable(fibs(9)))
print(fibs(10))


def square(x):
    """Calculates the square of the number x."""
    return x * x

print(square.__doc__)   # 访问文档字符串
print(help(square))     # 获取有关函数的信息

# 所有的函数都返回值。如果没有return，将返回None




