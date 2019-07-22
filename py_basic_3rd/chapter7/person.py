# -*- coding: utf-8 -*-
# @Time       : 2019/3/27 10:02
# @Author     : Philly
# @File       : person.py
# @Description: 
__metaclass__ = type    # 如果是Python2，请包含这行代码


class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm {}.".format(self.name))


class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):   # SPAMFileter是Filter的子类
    def init(self): # 重写超类Filter的方法init
        self.blocked = ['SPAM']


if __name__ == "__main__":
    s = SPAMFilter()
    s.init()
    t = s.filter(['SPAM','eggs','SPAM','bacon'])
    print(t)
    print(s.__dict__)

    foo = Person()
    bar = Person()
    foo.set_name('Luke Skywalker')
    bar.set_name('Anakin Skywalker')
    foo.greet()
    bar.greet()
    print(foo.name)
    print(bar.name)
