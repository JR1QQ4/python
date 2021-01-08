#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 10 条: 尽量用 enumerate 取代 range

# enumerate 函数提供了一种精简的写法，可以在遍历迭代器时获知某个元素的索引
# 尽量用 enumerate 来改写那种将 range 与下标访问相结合的序列遍历代码
# 可以给 enumerate 提供第二个参数，以指定开始计数时所用的值（默认为0）

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print('%s is delicious' % flavor)

print('-' * 50)
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%s is delicious' % flavor)

print('-' * 50)
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print("%d: %s" % (i + 1, flavor))

print('-' * 50)
for i, flavor in enumerate(flavor_list):
    print("%d: %s" % (i + 1, flavor))

print('-' * 50)
for i, flavor in enumerate(flavor_list, 1):
    print("%d: %s" % (i, flavor))



