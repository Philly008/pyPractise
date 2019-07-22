# -*- coding: utf-8 -*-
# @Time       : 2019/3/26 17:24
# @Author     : Philly
# @File       : 01.py
# @Description: 


# 阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 幂
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * pow(x, n - 1)


# 二分查找
def search(sequence, number, lower=0, upper=None):
    if upper is None: upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


if __name__ == '__main__':
    print(factorial(3))
    print(pow(3, 2))
    seq = [34, 67, 8, 123, 4, 100, 95]
    seq.sort()
    print(seq)
    print(search(seq, 34))
    print(search(seq, 100))

