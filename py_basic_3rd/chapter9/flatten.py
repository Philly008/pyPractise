# -*- coding: utf-8 -*-
# @Time       : 2019/4/4 9:57
# @Author     : Philly
# @File       : flatten.py
# @Description: 


def flatten(nested):
    try:
        # 不迭代类似于字符串的对象
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


if __name__ == '__main__':
    print(list(flatten(['foo', ['bar', ['baz']]])))

