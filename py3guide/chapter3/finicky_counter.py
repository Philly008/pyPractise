# -*- coding: utf-8 -*-
# @Time       : 2019/7/19 11:33
# @Author     : Philly
# @File       : finicky_counter.py
# @Description: Demonstrates the break and continue statements
count = 0
while True:
    count += 1
    # end loop if count greater then 10
    if count > 10:
        break
    # skip 5
    if count == 5:
        continue
    print(count)

input("\n\nPress the enter key to exit.")

