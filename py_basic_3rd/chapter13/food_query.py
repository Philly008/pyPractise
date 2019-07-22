# -*- coding: utf-8 -*-
# @Time       : 2019/4/18 15:59
# @Author     : Philly
# @File       : food_query.py
# @Description: 食品数据库查询程序
import sqlite3, sys


conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE ' + sys.argv[1]
print(query)
curs.execute(query)
names = [f(0) for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print('{}: {}'.format(*pair))
    print()









