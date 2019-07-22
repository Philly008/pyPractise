# -*- coding: utf-8 -*-
# @Time       : 2019/4/18 16:53
# @Author     : Philly
# @File       : twisted_s.py
# @Description: 使用协议LineReceiver改进后的日志服务器
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver


class SimpleLogger(LineReceiver):
    def connectionMade(self):
        print('Got connectiion from ', self.transport.client)

    def connectionLost(self, reason):
        print(self.transport.client, 'disconnected')

    def lineReceived(self, line):
        print(line)

factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234, factory)
reactor.run()



