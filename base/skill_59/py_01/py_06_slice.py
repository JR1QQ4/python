#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 6 条: 在单次切片操作内，不要同时指定 start、end 和 stride

# 既有 start 和 end，又有 stride 的切割操作，可能会令人费解
# 尽量使用 stride 为正数，且不带 start 或 end 索引的切割操作，尽量避免用负数做 stride
# 在同一个切片操作内，不要同时使用 start、end 和 stride，应该拆解为两条赋值语句，或使用内置 itertools 模块中的 islice

a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)  # ['red', 'yellow', 'blue']
print(evens)  # ['orange', 'green', 'purple']

x = b'mongoose'
y = x[::-1]
print(y)  # b'esoognom'

# w = '谢谢'
# x = w.encode('utf-8')
# y = x[::-1]
# z = y.decode('utf-8')  # UnicodeDecodeError

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[::2])  # ['a', 'c', 'e', 'g']
print(a[::-2])  # ['h', 'f', 'd', 'b']
print(a[2::2])  # ['c', 'e', 'g']
print(a[-2::-2])  # ['g', 'e', 'c', 'a']
print(a[-2:2:-2])  # ['g', 'e']
print(a[2:2:-2])  # []

b = a[::2]
c = b[1:-1]
print(c)  # ['c', 'e']

import itertools
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
b = itertools.islice(a, start=2, stop=-2, step=-2)
print(b)  # ['c', 'e']





