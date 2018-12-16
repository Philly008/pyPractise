# -*- coding: utf-8 -*-
# @Time       : 2018/12/11 17:09
# @Author     : Philly
# @File       : threading_program.py
# @Description: 并发编程
import time
from threading import Thread

class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(2)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate()   # Signal termination
t.join()    # Wait for actual termination
