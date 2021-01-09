#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 16 条: 考虑用生成器来改写直接返回列表的函数

# 使用生成器比把收集到的结果放入列表里返回给调用者更加清晰
# 由生成器函数所返回的那个迭代器，可以把生成器函数体中，传给 yield 表达式的那些值，逐次产生出来
# 无论输入量由多大，生成器能产生一系列输出，因为这些输入量和输出量，都不会影响它在执行时所耗的内存


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


address = 'Four score and seven year ago...'

result = index_words(address)
print(result)  # [0, 5, 11, 15, 21, 26]

result1 = list(index_words_iter(address))
print(result1)  # [0, 5, 11, 15, 21, 26]


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset
from itertools import islice
with open('./address.txt', 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 3)
    print(list(results))  # [0, 5, 11]














