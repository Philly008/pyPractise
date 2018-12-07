# -*- coding: utf-8 -*-
# @Time       : 2018/12/5 16:29
# @Author     : Philly
# @File       : mul_threads.py
# @Description: 多线程
import threading, time


def fun(var):
    time.sleep(1)
    print(var)

for i in range(10):
    t = threading.Thread(target=fun, args=(i,))  # 创建一个多线程对象，指定函数名和参数
    t.start()   # 启动线程
print('end')

