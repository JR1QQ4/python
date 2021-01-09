#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 15 条: 了解如何在闭包里使用外围作用域中的变量

# 对于定义在某作用域内的闭包来说，它可以引用这些作用域中的变量
# 使用默认方式对闭包内的变量赋值，不会影响外围作用域中的同名变量
# 在 Python3 中，程序可以在闭包内用 nonlocal 语句来修饰某个名称，使该闭包能够修改外围作用域中的同名变量
# 在 Python2 中，程序可以使用可变值（例如，包含单个元素的列表）来实现与 nonlocal 语句相仿的机制
# 除了那种比较简单的函数，尽量不要用 nonlocal 语句


def sort_priority(values, group):
    def helper(x):
        """ 如果元素在 group 中，先把它放到 0 集合中，再按照升序排序；否则，放到 1 集合中，再按照升序排列 """
        if x in group:
            return 0, x
        return 1, x
    values.sort(key=helper)
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)  # [2, 3, 5, 7, 1, 4, 6, 8]

# 在表达式中引用变量时，Python 解释器将按如下顺序遍历各作用域，一解析该引用:
# 1)当前函数的作用域
# 2)任何外围作用域（例如，包含当前函数的其他函数）
# 3)包含当前代码的那个模块的作用域（也叫全局作用域，global scope）
# 4)内置作用域（也就是包含 len 及 str 等函数的那个作用域）
# 如果这些地方都没有定义过名称相符的变量，那就抛出 NameError 异常


def sort_priority2(numbers, group):
    found = False  # Scope: 'sort_priority2'
    def helper(x):
        if x in group:
            found = True  # Scope: 'helper'
            return 0, x
        return 1, x
    numbers.sort(key=helper)
    return found
numbers1 = [8, 3, 1, 2, 5, 4, 7, 6]
group1 = {2, 3, 5, 7}
found = sort_priority2(numbers1, group1)
print('Found:', found)  # Found: False
print(numbers1)  # [2, 3, 5, 7, 1, 4, 6, 8]


def sort_priority3(numbers, group):
    found = False
    def helper(x):
        # nonlocal 如果在闭包内给该变量赋值，那么修改的其实是闭包外那个作用域的变量
        # 这与 global 语句互为补充，global 用来表示对该变量的赋值操作，将会直接修改模块作用域里的那个变量
        nonlocal found
        if x in group:
            found = True
            return 0, x
        return 1, x
    numbers.sort(key=helper)
    return found

class Sorter(object):
    def __init__(self, groups):
        self.groups = groups
        self.found = False
    def __call__(self, x):
        if x in self.groups:
            self.found = True
            return 0, x
        return 1, x
numbers2 = [8, 3, 1, 2, 5, 4, 7, 6]
group2 = {2, 3, 5, 7}
sorter = Sorter(group2)
numbers2.sort(key=sorter)
assert sorter.found is True
print(numbers2)  # [2, 3, 5, 7, 1, 4, 6, 8]





