#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np


# 1
# def pySum1():
#     a = [0, 1, 2, 3, 4]
#     b = [9, 8, 7, 6, 5]
#     c = []
#     for i in range(len(a)):
#         c.append(a[i]**2 + b[i]**3)
#     print(c)
# def pySum2():
#     a = np.array([0, 1, 2, 3, 4])
#     b = np.array([9, 8, 7, 6, 5])
#     c = a**2 + b**3
#     print(c)
# pySum1()
# pySum2()

# 2
# print(np.arange(10))
# print(np.ones((3, 6)))
# print(np.zeros((3, 6), dtype=np.int32))
# print(np.eye(5))

# 3
a = np.array([9, 8, 7, 6, 5])
print(a[2])  # 7
print(a[1:4:2])  # [8 6]，[起始编号：终止编号（不含）：步长]

a1 = np.arange(24).reshape((2, 3, 4))
print(a1)
print(a1[1, 2, 3])  # 23
print(a1[0, 1, 2])  # 6
print(a1[-1, -2, -3])  # 17

a2 = np.arange(24).reshape((2, 3, 4))
print(a2[:, 1, -3])
print(a2[:, 1:3, :])
print(a2[:, :, ::2])











