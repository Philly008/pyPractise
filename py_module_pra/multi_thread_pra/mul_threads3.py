# -*- coding: utf-8 -*-
# @Time       : 2018/12/5 16:29
# @Author     : Philly
# @File       : mul_threads.py
# @Description: join等待线程运行完，才继续往下走
import requests, threading, time


res_times = []  # 用list存放所有的响应时间


class ThreadTe2(object):
    def __init__(self, url):
        self.url = url

    def send_re(self):
        start_time = time.time()
        r = requests.get(self.url).text
        # print(r)
        end_time = time.time()
        res_times.append(end_time-start_time)

url = 'http://202.116.104.161/NIP/home.action'
bfs = 1000
te2 = ThreadTe2(url)
t_list = []
for i in range(bfs):
    t = threading.Thread(target=te2.send_re())
    t_list.append(t)
    t.start()

for t in t_list:
    t.join()

avg = sum(res_times)/len(res_times)
print(avg)

