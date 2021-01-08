#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 9 条: 用生成器表达式来改写数据较大的列表推导

# 当输入的数据量较大时，列表推导可能会因为占用太多内存而出问题
# 由生成器表达式所返回的迭代器，可以逐次产生输出值，从而避免了内存用量问题
# 把某个生成器表达式所返回的迭代器，放在另一个生成器表达式的 for 子表达式中，即可将两者组合起来
# 串在一起的生成器表达式执行速度很快

# value = [len(x) for x in open('./my_file.txt')]  # 只适合少量的输入值
# print(value)

it = (len(x) for x in open('my_file.txt'))
print(it)  # <generator object <genexpr> at 0x00000200BE7FBA48>
print(next(it))
print(next(it))

roots = ((x, x**0.5) for x in it)
print(next(roots))
print(next(roots))



