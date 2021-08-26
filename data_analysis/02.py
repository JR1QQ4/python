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
# a = np.array([9, 8, 7, 6, 5])
# print(a[2])  # 7
# print(a[1:4:2])  # [8 6]，[起始编号：终止编号（不含）：步长]
# a1 = np.arange(24).reshape((2, 3, 4))
# print(a1)
# print(a1[1, 2, 3])  # 23
# print(a1[0, 1, 2])  # 6
# print(a1[-1, -2, -3])  # 17
# a2 = np.arange(24).reshape((2, 3, 4))
# print(a2[:, 1, -3])
# print(a2[:, 1:3, :])
# print(a2[:, :, ::2])

# 4。数组与标量
# a = np.arange(24).reshape((2, 3, 4))
# print(a)
# print(a.mean())  # 11.5
# a = a / a.mean()
# print(a)
# print(np.ceil(a))
# b = np.sqrt(a)
# print(np.maximum(a, b))

# 5
# a = np.arange(100).reshape(5, 20)
# np.savetxt('a.csv', a, fmt='%d', delimiter=',')
# a.tofile("b.dat", format='%s')

# 6
# b = np.random.randint(100, 200, (3, 4))

# 7
# a = np.arange(100).reshape(5, 20)
# np.sum(a)

# 8
# a = np.arange(100).reshape(5, 20)
# np.gradient(a)

# 9、彩色图片灰度变换
from PIL import Image

# a = np.array(Image.open('').convert('L'))
# b = 255 - a  # (100/255)*a+150  255*(a/255)**2
# im = Image.fromarray(b.astype('uint8'))
# im.save('')

# 10
import matplotlib.pyplot as plt

# plt.plot([3, 1, 4, 5, 2])
# plt.ylabel("Grade")
# plt.savefig('test', dpi=600)  # PNG文件
# plt.show()

# 11、引力波
from scipy.io import wavfile

# rate_h, hstrain = wavfile.read(r'H1_Strain.wav')
# rate_l, lstrain = wavfile.read(r'L1_Strain.wav')
# reftime, ref_H1 = np.genfromtxt('wf_template.txt').transpose()
# # ------------------------------------------------------------
# htime_interval = 1/rate_h
# ltime_inrterval = 1/rate_l
# htime_len = hstrain.shape[0]/rate_h
# htime = np.arange(-htime_len/2, htime_len/2, htime_interval)
# ltime_len = lstrain.shape[0]/rate_l
# ltime = np.arange(-ltime_len/2, ltime_len/2, ltime_inrterval)
# # ------------------------------------------------------------
# fig = plt.figure(figsize=(12, 6))
# plth = fig.add_subplot(221)
# plth.plot(htime, hstrain, 'y')
# plth.set_xlabel('Time (seconds)')
# plth.set_ylabel('H1 Strain')
# plth.set_title('H1 train')
# # ------------------------------------------------------------
# plt1 = fig.add_subplot(222)
# plt1.plot(ltime, lstrain, 'g')
# plt1.set_xlabel('Time (seconds)')
# plt1.set_ylabel('L1 Strain')
# plt1.set_title('L1 train')
# # ------------------------------------------------------------
# pltref = fig.add_subplot(212)
# pltref.plot(reftime, ref_H1)
# pltref.set_xlabel('Time (seconds)')
# pltref.set_ylabel('Template Strain')
# pltref.set_title('Template')
# # ------------------------------------------------------------
# fig.tight_layout()
# # plt.savefig("Gravitational_Waves_Original.png")
# plt.show()
# plt.close(fig)

# 12
import pandas as pd

# d = pd.Series(range(20))
# print(d)
# print('*' * 50)
# print(d.cumsum())

# 13
# Series 类型
# a = pd.Series([9, 8, 7, 6])
# print(a)
# b = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
# print(b)
# s = pd.Series(25, index=['a', 'b', 'c'])
# print(s)
# d = pd.Series({'a': 9, "b": 8, "c": 7})
# print(d)
# e = pd.Series({'a': 9, "b": 8, "c": 7}, index=['a', 'b', 'c', 'd'])
# print(e)
# 使用 ndarray 创建
# n = pd.Series(np.arange(5))
# print(n)
# f = pd.Series(np.arange(5), index=np.arange(9, 4, -1))
# print(f)
# 索引
# g = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
# print(g.index)
# print(g.values)
# print(g['b'])
# print(g[1])
# # print(g[['c', 'd', 0]])
# print(g[['c', 'b', 'a']])
# 基本操作
# h = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
# print(h[:3])
# print(h[h > h.median()])
# print(np.exp(h))
# print('c' in h)  # True
# print(0 in h)  # False
# print(h.get('f', 100))
# j = pd.Series([1, 2, 3], index=['c', 'd', 'e'])
# # print(h + j)
# # print(j.name)
# # j.name = 'Series对象'
# # j.index.name = '索引列'
# # print(j)
# j['c'] = 15
# print(j)
# j[['d', 'e']] = 20
# print(j)
