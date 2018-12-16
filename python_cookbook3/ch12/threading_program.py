# -*- coding: utf-8 -*-
# @Time       : 2018/12/11 17:09
# @Author     : Philly
# @File       : threading_program.py
# @Description: 并发编程
import time
from threading import Thread


# Code to execute in an independent thread
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)

# Create and launch a thread
t = Thread(target=countdown, args=(10,), daemon=True)   # daemon=True 设置为后台线程
t.start()   # 启动线程
t.join()    # 将一个线程加入到当前线程，并等待它终止

if t.is_alive():
    print('Still running')
else:
    print('Completed')


