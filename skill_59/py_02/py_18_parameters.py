#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 18 条: 用数量可变的位置参数减少视觉砸讯

# 在 def 语句中使用 *args，即可令函数接受数量可变的位置参数
# 调用函数时，可以采用 * 操作符，把序列中的元素当成位置参数，传给该函数
# 对生成器使用 * 操作符，可能导致程序耗尽内存并崩溃
# 在已经接受 * args 参数的函数上面继续添加位置参数，可能会产生难以排查的 bug


def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


log('My numbers are', [1, 2])  # My numbers are: 1, 2
log('Hi there', [])  # Hi there


def log1(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


favorites = [7, 33, 99]
log1('Favorite colors', *favorites)  # Favorite colors: 7, 33, 99


def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


def log2(sequence, message, *values):
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, values_str))


log2(0, 'Favorites')  # 0: Favorites
log2(1, 'Favorites', 7, 33)  # 1: Favorites: 7, 33
log2('Favorite numbers', 7, 33)  # Favorite numbers: 7: 33


















