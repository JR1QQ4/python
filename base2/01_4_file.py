#!/usr/bin/python
# -*- coding:utf-8 -*-

# fin = open("data/words.txt")
# print(fin)
# print(fin.readline())
# fin.close()

# def is_palindrome(word):
#     i = 0
#     j = len(word) - 1
#     while i < j:
#         print(i, j)
#         if word[i] != word[j]:
#             return False
#         i += 1
#         j -= 1
#     return True
# print(is_palindrome('abadba'))

import os

# print(os.getcwd())  # 当前目录
# print(os.path.abspath('data/words.txt'))  # 绝对路径
# print(os.path.isdir('data/words.txt'))  # false
# print(os.listdir(os.getcwd()))

# def walk(dirname):
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname, name)
#         if os.path.isfile(path):
#             print(path)
#         else:
#             walk(path)
# walk('.')

# import urllib3
# res = urllib3.PoolManager().request('GET', 'http://www.baidu.com')
# print(res.data.decode())


