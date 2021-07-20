#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 19 条: 用关键字参数来表达可选的行为

# 函数参数可以按位置或关键字来指定
# 只使用位置参数来调用函数，可能会导致这些参数值的含义不够明确，而关键字参数则能够阐明每个参数的意图
# 给函数添加新的行为时，可以使用带默认值的关键字参数，以便与原有的函数调用代码保持兼容
# 可选的关键字参数，总是应该以关键字形式来指定，而不应该以位置参数的形式来指定


def remainder(number, divisor):
    return number % divisor


assert remainder(20, 7) == 6
print(remainder(20, 7))
print(remainder(20, divisor=7))
print(remainder(number=20, divisor=7))
print(remainder(divisor=7, number=20))


# print(remainder(number=20, 7))  # SyntaxError: positional argument follows keyword argument
# print(remainder(20, number=7))  # SyntaxError: positional argument follows keyword argument


def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print('%.3f kg per second' % flow)  # 0.167 kg per second


def flow_rate1(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period


def flow_rate2(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


def flow_rate3(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period
