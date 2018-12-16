# -*- coding: utf-8 -*-
# @Time       : 2018/12/11 17:09
# @Author     : Philly
# @File       : threading_program.py
# @Description: 使用 Event 来协调线程的启动
import time
from threading import Thread, Event


# Code to execute in an independent thread
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)

# Create the event object that will be used to signal startup
started_evt = Event()

# Launch the thread and pass the startup event
print('Launching countdown')
t = Thread(target=countdown, args=(10, started_evt))
t.start()
# Wait for the thread to start
started_evt.wait()
print('countdown is running')
