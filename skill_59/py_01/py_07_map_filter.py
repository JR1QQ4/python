#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 7 条: 用列表推导来取代 map 和 filter

# 列表推导要比内置的 map 和 filter 函数清晰，因为它无需额外编写 lambda 表达式
# 列表推导可以跳过输入列表中的某些元素，如果改用 map 来做，那就必须辅以 filter 方能实现
# 字典与集也支持推导表达式

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x ** 2 for x in a]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares = map(lambda x: x ** 2, a)
print(list(squares))  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)

chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)  # {1: 'ghost', 2: 'habanero', 3: 'cayenne'}
print(chile_len_set)  # {8, 5, 7}


