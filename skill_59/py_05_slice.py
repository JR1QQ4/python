#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 5 条: 了解切割序列的办法

# 不要写多余的代码，当 start 索引为0，或 end 索引为序列长度时，应将其省略
# 切片操作不会计较 start 与 end 索引是否越界，这使得很容易就能从序列的前端或后端开始，如a[:20]或a[-20:]
# 对 list 赋值的时候，如果使用切片操作，就会把原列表中处在相关范围内的值替换成新值，即便它们的长度不同也依然会替换

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])  # ['a', 'b', 'c', 'd']
print('Last four:', a[-4:])  # ['e', 'f', 'g', 'h']
print('Middle two:', a[3:-3])  # ['d', 'e']

assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]

print(a[:20])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# print(a[20])  # IndexError: list index out of range

# print("Before:", a)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# a[2:7] = [99, 22, 14]
# print("After:", a)  # ['a', 'b', 99, 22, 14, 'h']

b = a[:]
assert b == a and b is not a

b = a
print('Before:', a) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[:] = [101, 102, 103]
assert a is b
print('After', a) # [101, 102, 103]



