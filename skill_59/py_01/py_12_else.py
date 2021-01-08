#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 12 条: 不要在 for 和 while 循环后面写 else 块

# Python 有特殊语法，可在 for 及 while 循环的内部语句块之后紧跟一个 else 块
# 只有当整个循环主体都没遇到 break 语句时，循环后面的 else 才会执行
# 不要在循环后面使用 else 块，因为这种写法既不直观，又容易引人误解

for i in range(3):
    print('Loop %d' % i)
else:
    print('Else block!')

print('*' * 50)
for i in range(3):
    print('Loop %d' % i)
    if i == 1:
        break
else:
    print('Else block!')  # 不会执行

print('*' * 50)
for x in []:
    print('Never runs')
else:
    print('For Else block!')  # 空序列立刻执行 else 块

print('*' * 50)
while False:
    print('Never runs')
else:
    print('While Else block!')  # 循环条件为 false 的立刻执行 else 块

print('*' * 50)
a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime')


def coprime(a1, b1):
    for i1 in range(2, min(a1, b1) + 1):
        if a1 % i1 == 0 and b1 % i1 == 0:
            return False
    return True


def coprime2(a2, b2):
    is_coprime = True
    for i2 in range(2, min(a2, b2) + 1):
        if a2 % i2 == 0 and b2 % i2 == 0:
            is_coprime = False
            break
    return is_coprime
