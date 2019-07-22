# -*- coding: utf-8 -*-
# @Time       : 2019/4/18 16:05
# @Author     : Philly
# @File       : socket_client.py
# @Description: 最简单的客户端
import socket


s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
print(s.recv(1024))

