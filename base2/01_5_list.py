#!/usr/bin/python
# -*- coding:utf-8 -*-

# a = [1, 2, 3]
# b = [4, 5]
# print(a + b)  # [1, 2, 3, 4, 5]
# print(a * 2)  # [1, 2, 3, 1, 2, 3]
# print(a.extend(b), a)  # None [1, 2, 3, 4, 5]

# t = ['a', 'b', 'c']
# x = t.pop(1)
# print(x, t)  # b ['a', 'c']

# t = ['a', 'b', 'c']
# del t[1]
# print(t)  # ['a', 'c']

# t = ['a', 'b', 'c']
# t.remove('b')
# print(t)  # ['a', 'c']

# t = ['a', 'b', 'c', 'd', 'e', 'f']
# del t[1:5]
# print(t)  # ['a', 'f']

# t = ['z', 's', 'c', 'a']
# print(t.sort(), t)  # None ['a', 'c', 's', 'z']

# a = "zsca"
# a = sorted(a)
# print(a)  # ['a', 'c', 's', 'z']

# 统计出现相同生日的机率
# import random
# def has_duplicates(t: list):
#     s = t[:]
#     s.sort()
#     for i in range(len(s) - 1):
#         if s[i] == s[i + 1]:
#             return True
#     return False
# def random_bdays(n):
#     t = []
#     for i in range(n):
#         bday = random.randint(1, 365)
#         t.append(bday)
#     return t
# def count_matches(students, samples):
#     count = 0
#     for i in range(samples):
#         t = random_bdays(students)
#         if has_duplicates(t):
#             count += 1
#     return count
# num_students = 23
# num_simulations = 1000
# count = count_matches(num_students, num_simulations)
# print('After %d simulations' % num_simulations)
# print('with %d students' % num_students)
# print('there were %d simulations with at least one match' % count)
