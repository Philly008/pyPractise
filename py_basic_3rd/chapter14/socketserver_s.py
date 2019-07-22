# -*- coding: utf-8 -*-
# @Time       : 2019/4/18 16:12
# @Author     : Philly
# @File       : socketserver_s.py
# @Description: 基于SocketServer的极简服务器
from socketserver import TCPServer, StreamRequestHandler


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from ', addr)
        self.wfile.write('Thank you for connectiong')

server = TCPServer(('', 1234), Handler)
server.serve_forever()


