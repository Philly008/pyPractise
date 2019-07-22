# -*- coding: utf-8 -*-
# @Time       : 2019/7/19 15:14
# @Author     : Philly
# @File       : maitre_d.py
# @Description: Demonstrates treating a value as a condition
print("Welcome to the Chateau D' Food")
print("It seems we are quite full this evening.\n")

money = int(input("How many dollars do you slip the Maitre D'? "))

if money:
    print("Ah, I am reminded of a table. Right this way.")
else:
    print("Please, sit. It may be a while.")

input("\n\nPress the enter key to exit.")

