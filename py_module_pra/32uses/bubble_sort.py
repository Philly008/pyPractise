# -*- coding: utf-8 -*-
# @Time       : 2019/1/22 9:46
# @Author     : Philly
# @File       : bubble_sort.py
# @Description: 冒泡排序
import os
import random, string


# 冒泡排序
def bubble_sort(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
    return lis


# 计算x的n次方
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 计算a*a+b*b+c*c+...
def calc(*numbers):
    sum1 = 0
    for n in numbers:
        sum1 = sum1 + n*n
    return sum1


# 计算阶乘 n!
def fac():
    num = int(input("请输入一个数字："))
    factorial = 1
    # 查看数字是负数、0或者正数
    if num < 0:
        print("抱歉，负数没有阶乘")
    elif num == 0:
        print("0 的阶乘为 1")
    else:
        for i in range(1, num+1):
            factorial = factorial * i
        print("%d 的阶乘为 %d" % (num, factorial))


# 输出某个路径下的所有文件和文件夹路径
def print_dir():
    filepath = input("请输入一个路径：")
    if filepath == "":
        print("请输入正确的路径")
    else:
        for i in os.listdir(filepath):  # 获取目录汇总的文件及子目录列表
            print(os.path.join(filepath, i))    # 把路径组合起来


# 输出某个路径及其子目录下的所有文件路径
def show_dir(filepath):
    for i in os.listdir(filepath):
        path = (os.path.join(filepath, i))
        print(path)
        if os.path.isdir(path):
            show_dir(path)      # 如果是目录，递归


# 输出某个路径及其子目录下所有以.html为后缀的文件
def print_dir2(filepath):
    for i in os.listdir(filepath):
        path = os.path.join(filepath, i)
        if os.path.isdir(path):
            print_dir2(path)
        if path.endswith(".html"):
            print(path)









if __name__ == '__main__':
    """
    lis0 = [12, 9, 88, 6, 55, 21]
    bubble_sort(lis0)
    print(lis0)

    print(power(2, 4))

    print(calc(1, 2, 3))

    # fac()

    # 列出当前目录下的所有文件和文件名
    al = [d for d in os.listdir('.')]
    print(al)

    L = ['Hello', 'World', 'IBM']
    for s in L:
        s = s.lower()
        print(s)
    

    print(print_dir())

    show_dir("C:\\Users\\hasee\\Desktop\\resources")

    print_dir2("C:\\Users\\hasee\\Desktop\\resources")

    # 把原字典的键值对颠倒并生成新的字典
    dict1 = {"A": "a", "B": "b", "C": "c"}
    dict2 = {y: x for x, y in dict1.items()}
    print(dict2)

    # 打印九九乘法表
    for i in range(1, 10):
        for j in range(1, i+1):
            print('%d x %d = %d  ' % (j, i, i * j), end='')     # end指定分隔符
        print()

    # 替换列表中所有的3为3a
    num = ["haa", "lamp", 3, 34, 3, 38, 73]
    print(num.count(3))
    print(num.index(3))
    for i in range(num.count(3)):   # 获取3出现的次数
        ele_index = num.index(3)    # 获取首次出现3的坐标
        num[ele_index] = "3a"
    print(num)

    # 打印每个名字
    L = ["James", "Liu", "Xin"]
    for i in range(len(L)):
        print("Hello, %s" % L[i])

    # 合并去重
    list1 = [2, 3, 8, 9, 6]
    list2 = [6, 3, 8, 1]
    list3 = list1 + list2
    print(list3)    # 不去重，只进行两个列表的组合
    print(set(list3))   # 去重，类型为set，需转换成list
    print(list(set(list3)))

    # 随机生成验证码（数字字母）
    str1 = "0123456789"
    str2 = string.ascii_letters     # 包含所有字母（大写或小写）的字符串
    str3 = str1 + str2
    ma1 = random.sample(str3, 6)    # 多个字符中选取特定数量的字符
    ma1 = ''.join(ma1)      # 拼接成字符串
    print(ma1)

    # 随机数字小游戏
    i = 1
    a = random.randint(0, 100)
    b = int(input('请输入0-100中的一个数字：'))
    while a != b:
        if a > b:
            print('你第%d次输入的数字偏小' % i)
            b = int(input('请再次输入数字：'))
        else:
            print('你第%d次输入的数字偏大' % i)
            b = int(input('请再次输入数字：'))
        i += 1
    else:
        print('恭喜你，你第%d次输入的数字%d对了' % (i, b))

    # 计算平方根
    num = float(input('请输入一个数字：'))
    num_sqrt = num ** 0.5
    print('%0.2f的平方根为%0.2f' % (num, num_sqrt))

    # 判断字符串是否只由数字组成
    t = "123"
    print(t.isdigit())

    # 判断奇偶数
    num = int(input('请输入一个数字：'))
    if (num % 2) == 0:
        print("{0}是偶数".format(num))
    else:
        print("{0}是奇数".format(num))

    # 判断闰年
    year = int(input('请输入一个年份：'))
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        print("{0}是闰年".format(year))
    else:
        print("{0}不是闰年".format(year))

    # 获取最大值
    N = int(input('输入需要对比大小的数字个数：'))
    print('请输入需要对比的数字：')
    num = []
    for i in range(1, N+1):
        temp = int(input('请输入第%d个数字：' % i))
        num.append(temp)
    print('您输入的数字为：', num)
    print('最大值为：', max(num))
"""
    # 斐波那契数列
    nterms = input('输入数字：')
    if nterms <= 0:
        print('请输入一个正整数。')
    elif nterms == 1:
        print('')






