# -*- coding: utf-8 -*-
# @Time       : 2019/7/19 11:35
# @Author     : Philly
# @File       : granted_or_denied.py
# @Description: Demonstrates an else clause
print("Welcome to System Security Inc.")
print("-- where security is our middle name\n")

password = input("Enter your password: ")

if password == "secret":
    print("Access Granted")
else:
    print("Access Denied")

input("\n\nPress the enter key to exit.")


