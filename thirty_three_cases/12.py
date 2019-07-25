# -*- coding: utf-8 -*-
# @Time       : 2019/7/24 14:54
# @Author     : Philly
# @File       : 12.py
# @Description: 12 lines: Classes


class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.banlance = initial_balance

    def deposit(self, amount):
        self.banlance += amount

    def withdraw(self, amount):
        self.banlance -= amount

    def overdrawn(self):
        return self.banlance < 0

my_account = BankAccount(15)
my_account.withdraw(5)
print(my_account.banlance)
my_account.deposit(50)
print(my_account.banlance)
my_account.withdraw(100)
print(my_account.banlance)
print(my_account.overdrawn())

