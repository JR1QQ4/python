#!/usr/bin/python
# -*- coding:utf-8 -*-
# 一、哪些不能作为变量？
# 字母、数字、下划线，不属于关键字，不以数字开头的字符串

# 二、修改列表【1，2，3，4，5】为【0，1，2，3，66，5，11，22，33】并排序
# li1 = [1, 2, 3, 4, 5]
# li1[3] = 66
# li1.insert(0, 0)
# li1.extend([11, 22, 33])
# li1.sort(reverse=True)
# print(li1)

# 三、修改{}为{'a':'a','b':'b'}，然后添加元素为{'a':'a','b':'b','c':'c','d':'d'}
# 删除最后一个添加的元素，然后清空
# dict1 = {}
# dict1.update({'a': 'a', 'b': 'b'})
# print(dict1)
# dict1.update({'c': 'c', 'd': 'd'})
# print(dict1)
# dict1.popitem()
# print(dict1)
# dict1.pop('c')
# print(dict1)
# dict1.clear()
# print(dict1)
# dict1['a'] = 'aa'
# print(dict1['a'], dict1.get('a'))

# 四、('a','a')，('b','b')，lis2=[('c','c')]变为字典{'a':'a','b':'b','c':'c'}
# lis2 = [('c', 'c')]
# lis2.append(('a', 'a'))
# lis2.append(('b', 'b'))
# print(dict(lis2))

# 五、实现文字版的剪刀石头布游戏，石头（1）剪刀（2）步（3）退出（4）
# import random
#
#
# li = ['石头', '剪刀', '布']
# while True:
#     c = random.randint(1, 3)
#     a = int(input("请输入你要出，石头（1）剪刀（2）布（3）退出（4）："))
#     if 1 <= a <= 3:
#         print("你出的是【{}】，电脑出的是【{}】。".format(li[a-1], li[c-1]), end='')
#         if (a - c == -1) or (a - c == 2):
#             print("用户胜！")
#         elif a == c:
#             print("平局！")
#         else:
#             print("电脑胜！")
#     elif a == 4:
#         print("退出！")
#         break
#     else:
#         print("输入的内容不正确，请重新输入！")
#     # if a == '1':
#     #     if c == 1:
#     #         print("平局！")
#     #     elif c == 2:
#     #         print("用户胜！")
#     #     elif c == 3:
#     #         print("电脑胜！")
#     # elif a == '2':
#     #     if c == 1:
#     #         print("电脑胜！")
#     #     elif c == 2:
#     #         print("平局！")
#     #     elif c == 3:
#     #         print("用户胜！")
#     # elif a == '3':
#     #     if c == 1:
#     #         print("用户胜！")
#     #     elif c == 2:
#     #         print("电脑胜！")
#     #     elif c == 3:
#     #         print("平局！")
#     # elif a == '4':
#     #     print('游戏退出')
#     #     break
#     # else:
#     #     print("输入的内容不正确，请重新输入！")
#     #     continue

# 六、九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{}*{}={:<4}".format(i, j, i*j), end='')
#     print()





