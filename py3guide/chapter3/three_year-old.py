# -*- coding: utf-8 -*-
# @Time       : 2019/7/19 15:27
# @Author     : Philly
# @File       : three_year-old.py
# @Description: Demonstrates the while loop
print("\tWelcome to the 'Three-Year-Old Simulator'\n")
print("This program simulates a conversation with a three-year-old child.")
print("Try to stop the madness.\n")

response = ""
while response != "Because.":
    response = input("Why?\n")

print("Oh. Okay.")

input("\n\nPress the enter key to exit.")

