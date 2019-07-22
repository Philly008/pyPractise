# -*- coding: utf-8 -*-
# @Time       : 2019/5/23 14:16
# @Author     : Philly
# @File       : py_mysql.py
# @Description: 操作mysql
import pymysql


# 打开数据库连接
db = pymysql.connect("202.116.104.165", "root", "123456", "test", 3306)

# 使用 cursor() 方法创建一个游标对象
cursor = db.cursor()

# # 使用 execute() 方法执行SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#     FIRST_NAME CHAR(20) NOT NULL,
#     LAST_NAME CHAR(20),
#     AGE INT,
#     SEX CHAR(1),
#     INCOME FLOAT
#     )"""
#
# cursor.execute(sql)

# SQL 插入语句
# sql2 = """INSERT INTO EMPLOYEE(FIRST_NAME,
#     LAST_NAME, AGE, SEX, INCOME)
#     VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

# sql2 = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#     LAST_NAME, AGE, SEX, INCOME) \
#     VALUES ('%s', '%s', %s, '%s', %s)" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)

# 更新语句
# sql4 = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

# 删除语句
sql5 = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
try:
    # 执行sql语句
    cursor.execute(sql5)
    # 提交
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# SQL 查询语句
# sql3 = "SELECT * FROM EMPLOYEE \
#     WHERE INCOME > %s" % (1000)
# try:
#     # 执行SQL语句
#     cursor.execute(sql3)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         # 打印结果
#         print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
#               (fname, lname, age, sex, income))
# except:
#     print("Error: unable to fetch data")


# # 使用 execute() 方法执行SQL查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据
# data = cursor.fetchone()
#
# print("Database version : %s " % data)

# 关闭数据库连接
db.close()

