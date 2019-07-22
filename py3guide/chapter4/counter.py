# -*- coding: utf-8 -*-
# @Time       : 2019/7/19 15:30
# @Author     : Philly
# @File       : counter.py
# @Description: Demonstrates the range() function
print("Counting: ")
for i in range(10):
    print(i, end=" ")

print("\n\nCounting by fives: ")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nCounting backwards: ")
for i in range(10, 0, -1):
    print(i, end=" ")

input("\n\nPress the enter key to exit.\n")

