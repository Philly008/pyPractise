# -*- coding: utf-8 -*-
# @Time       : 2019/7/19 11:25
# @Author     : Philly
# @File       : craps_roller.py
# @Description: Demonstrates random number generation
import random

# generate random numbers 1 - 6
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1

total = die1 + die2

print("You rolled a ", die1, "and a ", die2, "for a total of ", total)

input("\n\nPress the enter key to exit.")

