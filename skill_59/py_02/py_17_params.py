#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 17 条: 在参数上面迭代时，要多加小心

# 函数在输入的参数上面多次迭代时要当心: 如果参数是迭代器，那么可能会导致奇怪的行为并错失某些值
# Python 的迭代器协议，描述了容器和迭代器应该如何与 iter 和 next 内置函数、for 循环及相关表达式相互配合
# 把 __iter__ 方法实现为生成器，即可定义自己的容器类型
# 想判断某个值是迭代器还是容器，可以拿该值为参数，两次调用 iter 函数，若结果相同，则是迭代器，
#   调用内置的 next 函数，即可令该迭代器前进一步

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)  # [11.538461538461538, 26.923076923076923, 61.53846153846154]


def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits('./my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)


def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


path = './my_numbers.txt'
percentages = normalize_func(lambda x: read_visits(path))


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits(path)
percentages = normalize(visits)


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
normalize_defensive(visits)
visits = ReadVisits(path)
normalize_defensive(visits)
it = iter(visits)
normalize_defensive(it)




