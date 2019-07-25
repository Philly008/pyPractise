# -*- coding: utf-8 -*-
# @Time       : 2019/7/25 10:18
# @Author     : Philly
# @File       : 18.py
# @Description: 20 lines: Prime numbers sieve w/fancy generators
import itertools


def iter_primes():
    # an iterator of all numbers between 2 and +infinity
    numbers = itertools.count(2)
    # generate primes forever
    while True:
        # get the first number from the iterator (always a prime)
        prime = numbers.__next__()
        yield prime
        # this code iteratively builds up a chain of filters...slightly tricky,
        # but ponder it a bit
        numbers = filter(prime.__rmod__, numbers)
for p in iter_primes():
    if p > 100:
        break
    print(p)

