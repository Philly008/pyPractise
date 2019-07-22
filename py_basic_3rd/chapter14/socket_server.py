# -*- coding: utf-8 -*-
# @Time       : 2019/4/18 16:05
# @Author     : Philly
# @File       : socket_server.py
# @Description: 最简单的服务器
import socket


s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from ', addr)
    c.send('Thank you for connecting')
    c.close()


