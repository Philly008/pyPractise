# -*- coding: utf-8 -*-
# @Time       : 2019/3/7 14:54
# @Author     : Philly
# @File       : mysql_te.py
# @Description: 测试PyMySQL驱动
import pymysql.cursors


# Connect to the database
connection = pymysql.connect(host='192.168.68.132',
                             user='root',
                             password='123456',
                             db='guest',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id, create_time) VALUES ("alen", 18888888888,"alen@mail.com",0,1,NOW());'
        cursor.execute(sql)
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT realname,phone,email,sign FROM sign_guest WHERE phone=%s"
        cursor.execute(sql, ('18888888888',))
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()















