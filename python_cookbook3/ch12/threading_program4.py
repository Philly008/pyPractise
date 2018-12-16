# -*- coding: utf-8 -*-
# @Time       : 2018/12/11 17:09
# @Author     : Philly
# @File       : threading_program.py
# @Description: 使用 Condition 对象实现了一个周期定时器，每当定时器超时的时候，其他线程都可以监测到
import time
import threading


class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        """
        Run the timer and notify waiting threads after each interval
        :return:
        """
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1     # 异或取值，二进制按位对比，相同取0，不同取1
                self._cv.notify_all()

    def wait_for_tick(self):
        """ Wait for the next tick of the timer"""
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

# Example use of the timer
ptimer = PeriodicTimer(2)
ptimer.start()


# Two threads that synchronize on the timer
def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-minus', nticks)
        nticks -= 1


def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n += 1

threading.Thread(target=countdown, args=(5,)).start()
threading.Thread(target=countup, args=(5,)).start()



