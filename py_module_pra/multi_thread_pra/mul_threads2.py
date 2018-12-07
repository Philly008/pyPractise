# -*- coding: utf-8 -*-
# @Time       : 2018/12/5 16:29
# @Author     : Philly
# @File       : mul_threads.py
# @Description: join等待线程运行完，才继续往下走
import threading, time


class ThreadTe(object):
    def __init__(self, sleep_time, name):
        self.sleep_time = sleep_time
        self.name = name

    def output(self):
        time.sleep(self.sleep_time)
        print(self.name)

a = ThreadTe(1, 'a')
b = ThreadTe(4, 'b')
c = ThreadTe(2, 'c')
t_list = []
for method in [a, b, c]:
    t = threading.Thread(target=method.output)
    t_list.append(t)
    t.start()

for t in t_list:    # 等待所有子线程都运行完，才往下走。
    t.join()    # join，等待子线程运行完成

print('end')
