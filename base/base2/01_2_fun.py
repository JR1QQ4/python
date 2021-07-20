#!/usr/bin/python
# -*- coding:utf-8 -*-

# 类型转换
# print(int('hello'))  # 错误
# print(int('32'))
# print(int(3.99999))
# print(int(-2.3))
# print(float(32))
# print(float('3.14159'))
# print(str(32))
# print(str(3.14159))

# def print_twice(bruce):
#     print(bruce)
#     print(bruce)
# def cat_twice(part1, part2):
#     cat = part1 + part2
#     print_twice(cat)
# cat_twice("Bing tiddle", "tiddle bang")

# def draw_square():
#     for i in range(11):
#         e = f = ''
#         if 0 == i or 5 == i or 10 == i:
#             e = '+'
#             f = '-'
#         else:
#             e = '|'
#             f = ' '
#         print(e + f * 4 + e + f * 4 + e)
# draw_square()


# def check_fermat(a, b, c, n):
#     if n > 2 and a ** n + b ** n == c ** n:
#         print("天哪， 费马弄错了！")
#     else:
#         print("不，那样不行")
# check_fermat(3, 4, 5, 2)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         recurse = factorial(n - 1)
#         result = n * recurse
#         return result
# print(factorial(5))


# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# def factorial(n):
#     space = ' ' * (4 * n)
#     print(space, 'factorial', n)
#     if n == 0:
#         print(space, 'returning 1')
#         return 1
#     else:
#         result = n * factorial(n - 1)
#         print(space, 'returning', result)
#         return result
# factorial(5)

# def gcd(x, y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     hcf_num = 0
#     for i in range(1, smaller + 1):
#         if x % i == 0 and y % i == 0:
#             hcf_num = i
#     print(hcf_num)
# gcd(54, 24)

# 三角函数
import math

# print(3 ** (1 / 2), 2 ** (1 / 2))
# print(math.sin(0), math.sin(math.pi / 6), math.sin(math.pi / 4), math.sin(math.pi / 3), math.sin(math.pi / 2))
# for i in range(1, 10):
#     a = i ** (1 / 2)
#     b = math.sqrt(i)
#     print(float(i), a, b, math.fabs(a - b))
