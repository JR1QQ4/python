#!/usr/bin/python
# -*- coding:utf-8 -*-

# 第一部分 Python 基础

print('********* 第 1 章 Python 基础 ***********')

num_01 = 2 ** 3
num_02 = 22 % 8
num_03 = 22 // 8
num_04 = 22 / 8
print(str(num_01), str(num_02), str(num_03), str(num_04))

# print('Hello world!)  #  SyntaxError: EOL while scanning string literal
# print('Alice' * 5.0)  # TypeError: can't multiply sequence by non-int of type 'float'
# print('Alice' * 'Bob')  # TypeError: can't multiply sequence by non-int of type 'str'

print(str(-3.14), str(29))
print(float('3.14'))
print(int(1.25))
# print(int('99.99'))  # ValueError: invalid literal for int() with base 10: '99.99'

print(42 == '42')  # False
print(42 == 42.0)  # True
print(42.0 == 0042.000)  # True

# 100 = 1  # can't assign to literal

print('********* 第 2 章 控制流 ***********')

print('dog' != 'cat')
print(not not not not True)
print((4 < 5) and (5 < 6))

total = 0
for num in range(101):
    total += num
print(total)

list0 = []
for i in range(12, 16):  # [12, 16)
    list0.append(i)
print(list0)

list1 = []
for j in range(1, 10, 2):
    list1.append(j)
print(list1)  # [1, 3, 5, 7, 9]

# import random
# list2 = []
# for i in range(5):
#     list2.append(random.randint(1, 10))  # [1, 10]
# print(list2)

# import sys
# while True:  # Ctrl + F2  或者 Ctrl + D
#     print('Type exit to exit:')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')

print('********* 第 3 章 函数 ***********')

print('cats', 'dogs', 'mice', sep=',')


# def spam():
#     eggs = 31337
# spam()
# print(eggs)  # NameError: name 'eggs' is not defined

# def bacon():
#     ham = 101
#     eggs = 0
# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)  # 99
# spam()

# def spam():
#     print(eggs)
# eggs = 42
# spam()
# print(eggs)

# def spam():
#     global eggs
#     eggs = 'spam'
# eggs = 'global'
# spam()
# print(eggs)  # spam

# def spam():
#     print(eggs)  # UnboundLocalError: local variable 'eggs' referenced before assignment
#     eggs = 'spam local'
# eggs = 'global'
# spam()

# import random
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')
# for guessesTaken in range(1, 7):
#     print('Take a guess.')
#     flag = True
#     guess = None
#     while flag:
#         try:
#             guess = int(input())
#             flag = False
#         except Exception:
#             print('Input error!! Please input again.')
#     if guess < secretNumber:
#         print('Your guess is too low.')
#     elif guess > secretNumber:
#         print('Your guess is too high.')
#     else:
#         break
# if guess == secretNumber:
#     print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
# else:
#     print('Nope. The number I was thinking of was ' + str(secretNumber))

# def collatz(number):
#     result = None
#     if number % 2 == 0:
#         result = number // 2
#         print(result)
#     elif number % 2 == 1:
#         result = 3 * number + 1
#         print(result)
#     return result
# while True:
#     print('Please input a number.')
#     try:
#         num = int(input())
#     except ValueError:
#         print('ValueError!!Please input again.')
#         continue
#     result = collatz(num)
#     if result == 1:
#         break

print('********* 第 4 章 列表 ***********')

