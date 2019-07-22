# -*- coding: utf-8 -*-
# @Time       : 2019/3/27 11:09
# @Author     : Philly
# @File       : bird.py
# @Description: 
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry = False
        else:
            print('No, thanks!')


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)


if __name__ == "__main__":
    sb = SongBird()
    sb.sing()
    sb.eat()
    sb.eat()
