# -*- coding: utf-8 -*-
# @Time       : 2018/12/6 17:14
# @Author     : Philly
# @File       : lock_threading.py
# @Description:
"""
threading 锁同步机制
self.lock.acquire() 和 self.lock.release() 锁机制保证了并发
"""
import threading
from threading import Thread


class LockThread(Thread):
    count = 0

    def __init__(self, name=None, lock=None):
        Thread.__init__(self, name=name)
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print('thread is ' + threading.current_thread().getName()+', lock acquired!')
        for i in range(0, 1000):
            LockThread.count += 1
        print('thread is ' + threading.current_thread().getName()+', pre lock release!')
        self.lock.release()

if __name__ == '__main__':
    threads = list()
    lock = threading.Lock()
    for i in range(0, 10):
        thread = LockThread(name=str(i), lock=lock)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print('Main Thread finish, LockThread.count is: ' + str(LockThread.count))

