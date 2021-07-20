#!/usr/bin/python
# -*- coding:utf-8 -*-

# {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d
# def print_hist(h):
#     for c in h:
#         print(c, h[c])
# h = histogram('brontosaurus')
# print(h)
# print_hist(h)

# {1: ['b', 'n', 't', 'a'], 2: ['r', 'o', 's', 'u']}
# def invert_dict(d):
#     inverse = dict()
#     for key in d:
#         val = d[key]
#         if val not in inverse:
#             inverse[val] = [key]
#         else:
#             inverse[val].append(key)
#     return inverse
# print(invert_dict({'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}))

# {0: 0, 1: 1, 2: 1, 3: 2, 4: 3}
# known = {0: 0, 1: 1}
# def fibonacci(n):
#     if n in known:
#         return known[n]
#     res = fibonacci(n - 1) + fibonacci(n - 2)
#     known[n] = res
#     print(known)
#     return res
# fibonacci(4)

# been_called = False
# def excample():
#     global been_called
#     been_called = True
# excample()
# print(been_called)  # True
