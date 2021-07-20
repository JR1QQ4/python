#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 23 条: 简单的几口应该接受函数，而不是类的实例

# 对于连接各种 Python 组件的简单接口来说，通常应该给其直接传入函数，而不是先定义某个类，然后再传入该类的实例
# Python 中的函数和方法都可以向一级类那样引用，因此，它们与其他类型的对象一样，也能狗放在表达式里面
# 通过名为 __call__ 的特殊方法，可以使类的实例能够像普通的 Python 函数那样得到调用
# 如果要用函数来保存状态，那就应该定义新的类，并令其实现 __call__ 当打，而不要定义带状态的闭包

from collections import defaultdict

names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)  # ['Plato', 'Socrates', 'Aristotle', 'Archimedes']


def log_missing():
    print('Key added')
    return 0


current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]
result = defaultdict(log_missing, current)
print('Before:', dict(result))  # Before: {'green': 12, 'blue': 3}
for key, amount in increments:
    result[key] += amount
print('After:', dict(result))  # After: {'green': 12, 'blue': 20, 'red': 5, 'orange': 9}

print('*' * 50)


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    return result, added_count


current1 = {'green': 12, 'blue': 3}
increments1 = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]
result, count = increment_with_report(current1, increments1)
print(result, count)
assert count == 2


class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0


current2 = {'green': 12, 'blue': 3}
increments2 = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]
counter = CountMissing()
result = defaultdict(counter.missing, current2)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2


class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


# counter = BetterCountMissing()
# counter()
# assert callable(counter)


current3 = {'green': 12, 'blue': 3}
increments3 = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]
counter = BetterCountMissing()
result = defaultdict(counter, current3)
for key, amount in increments3:
    result[key] += amount
assert counter.added == 2


