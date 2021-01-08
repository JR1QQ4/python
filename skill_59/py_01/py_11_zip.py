#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 11 条: 用 zip 函数同时遍历两个迭代器

# 内置的 zip 函数可以平行地遍历多个迭代器
# Python3 中的 zip 相当于生成器，会在遍历过程中逐次产生元组，而 Python2 中则直接把这些元组生成好并一次性返回整份列表
# 如果提供的迭代器长度不等，那么 zip 就会自动提前终止
# itertools 内置模块中的 zip_longest 函数可以平行地遍历多个迭代器，而不用在乎它们地长度是否相等

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]
print(letters)  # [7, 4, 5]

longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
print(longest_name)  # Cecilia
print(max_letters)  # 7

for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)  # Cecilia
print(max_letters)  # 7

for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)  # Cecilia
print(max_letters)  # 7

print('*' * 50)
names.append('Rosalind')
for name, count in zip(names, letters):
    print(name, count)  # Rosalind 并不会出现在遍历结果中

print('*' * 50)
import itertools
for name, count in itertools.zip_longest(names, letters):
    print(name, count)  # Rosalind 会出现在遍历结果中，没有的为 None
