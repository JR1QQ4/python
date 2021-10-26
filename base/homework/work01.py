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

# number = 100
# def func():
#     # print(number + 100)
#     global number
#     number = number + 100  # 没有global声明时，会报“在声明之前对变量引用”的错误
#     print(number)
# print(number)
# func()

# lis1 = [1, 2]
# lis2 = [11, 22]
# lis3 = [111, 222, 333]
# print(list(zip(lis1, lis2, lis3)))

# lis1 = [88, 23, 66, 435, 123, 576]
# res = filter(lambda x: x > 80, lis1)
# print(list(res))

# lis1 = [(11, 22, 33), (22, 33, 11), (33, 11, 22)]
# lis1.sort(key=lambda x: x[1])  # 以第二个元素排序
# print(lis1)

# from base.homework import pack
# print(pack.name)
# print(pack.test01.name)

# try:
#     pass
# except NameError:
#     pass
# else:
#     pass  # try的代码没有执行错误时执行
# finally:
#     pass

# self的方法：实例方法
# _变量：不成文的规定，伪声明表示私有化，外部可以调用；
# __变量：私有属性
# delattr(MyClass, attr)  # 动态删除属性

def login_check(username=None, password=None):
    if username is not None and password is not None:
        if username == 'admin' and password == 'pwd':
            return {'code': 0, 'msg': '登录成功'}
        else:
            return {'code': 1, 'msg': '账号或密码不正确'}
    else:
        return {'code': 1, 'msg': '所有的参数不能为空'}








