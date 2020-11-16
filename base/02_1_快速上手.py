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

spam = [1, 2, 3]
spam += ['A', 'B', 'C']
print(spam)

spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)  # ['cat', 'bat', 'elephant']

cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(size, color, disposition)

spam = ['hello', 'hi', 'howdy', 'heyas', 'hello']
print(spam.index('hello'))
# print(spam.index('hello hello'))  # ValueError: 'hello hello' is not in list

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)  # ['cat', 'chicken', 'dog', 'bat']

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
print(spam)  # ['bat', 'rat', 'cat', 'hat', 'cat']

# spam = [1, 3, 2, 4, 'Alice', 'Bob']
# spam.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'
spam = ['a', 'z', 'A', 'Z']
spam.sort()
print(spam)  # ['A', 'Z', 'a', 'z']
spam.sort(key=str.lower)
print(spam)  # ['A', 'a', 'Z', 'z']

# import random
# messages = ['It is certain',
#             'It is decidedly so',
#             'Yes definitely',
#             'Reply hazy try again',
#             'Ask again later',
#             'Concentrate and ask again',
#             'My reply is no',
#             'Outlook not so good',
#             'Very doubtful']
# print(messages[random.randint(0, len(messages) - 1)])

print('Four score and seven '
      'year ago...')

# name = 'Zophie a cat'
# name[7] = 'the'  # TypeError: 'str' object does not support item assignment

print(type('hello'), type(('hello',)))

# def eggs(someParameter=[]):
#     someParameter.append('Hello')
# spam = [1, 2, 3]
# eggs(spam)
# print(spam)

# import copy
# spam = ['A', 'B', 'C', 'D']
# cheese = copy.copy(spam)
# cheese[1] = 42
# print(spam)  # ['A', 'B', 'C', 'D']
# print(cheese)  # ['A', 42, 'C', 'D']
#
# spam = ['A', 'B', ['C', 'D']]
# cheese = copy.copy(spam)
# cheese[2][0] = 42
# print(spam)  # ['A', 'B', [42, 'D']]
# print(cheese)  # ['A', 'B', [42, 'D']]
#
# spam = ['A', 'B', ['C', 'D']]
# cheese = copy.deepcopy(spam)
# cheese[2][0] = 42
# print(spam)  # ['A', 'B', ['C', 'D']]
# print(cheese)  # ['A', 'B', [42, 'D']]

# spam = ['apples', 'bananas', 'tofu', 'cats']
# def listToString(list=[]):
#     return ', '.join(spam[:-1]) + ', and ' + spam[-1]
# print(listToString(spam))

# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
# for j in range(len(grid[0])):
#     for i in range(len(grid)):
#         print(grid[i][j], end='')
#     print()

print('********* 第 5 章 字典和结构化数据 ***********')

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)

spam = {'color': 'red', 'age': 42}
print(spam.keys())
print(spam.values())
print(spam.items())

picnicItems = {'apples': 5, 'cups': 2}
print(picnicItems.get('cups', 0))  # 存在直接返回，2
print(picnicItems.get('hello', 1))  # 不存在返回备用值，1
print(picnicItems.get('hello'))  # None，有的版本会报错

spam = {'name': 'Pooka', 'age': 5}
print(spam.setdefault('color', 'black'))  # black
print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}
print(spam.setdefault('color', 'white'))  # black
print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}

# 用于统计每个字符出现的次数
# import pprint  # 漂亮打印，格式化打印
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1
# pprint.pprint(count)

# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': '', 'mid-R': ' ', 'low-L': ' ',
#             'low-M': ' ', 'low-R': ' '}
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'

# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# def displayInventory(inventory):
#     print("Inventory:")
#     item_total = 0
#     for k, v in inventory.items():
#         print(str(v) + ' ' + k)
#         item_total += v
#     print("Total number of items: " + str(item_total))
# displayInventory(stuff)

# def func(arg: arg_type, optarg: arg_type = default) -> return_type:    ...

# def addToInventory(inventory: dict, addedItems: list):
#     for k in addedItems:
#         inventory.setdefault(k, 0)
#         inventory[k] += 1
#     return inventory
# def displayInventory(inventory):
#     print("Inventory:")
#     item_total = 0
#     for k, v in inventory.items():
#         print(str(v) + ' ' + k)
#         item_total += v
#     print("Total number of items: " + str(item_total))
# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)

print('********* 第 6 章 字符串操作 ***********')

print(r'That is Carol\'s cat.')  # That is Carol\'s cat.

print('Hello' in 'Hello world!')

print('12345'.islower(), '12345'.isupper())  # False False

print('NOT'.istitle(), 'Not'.istitle())  # False True

print('My name is Simon'.split())  # ['My', 'name', 'is', 'Simon']

print('Hello'.rjust(3))

# PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
#              'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
#              'luggage': '12345'}
# import sys
# print(sys.argv)
# if len(sys.argv) < 2:
#     print('Usage: python pw.py [account] - copy account password')
#     sys.exit()
# account = sys.argv[1]

# Lists of animals
# Lists of aquarium life
# Lists of biologists by author abbreviation
# Lists of cultivars
# * Lists of animals
# * Lists of aquarium life
# * Lists of biologists by author abbreviation
# * Lists of cultivars
# import pyperclip
# text = pyperclip.paste()
# lines = text.split('\n')
# for i in range(len(lines)):
#     lines[i] = '* ' + lines[i]
# text = '\n'.join(lines)
# pyperclip.copy(text)

# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#             ['Alice', 'Bob', 'Carol', 'David'],
#             ['dogs', 'cats', 'moose', 'goose']]
# def printTable(table: list) -> None:
#     colWidths = [0] * len(table)
#     for k, i in enumerate(table):
#         for j in i:
#             if len(j) > colWidths[k]:
#                 colWidths[k] = len(j)
#     temp = max(colWidths)
#     for i in range(len(table[0])):
#         for j in range(len(table)):
#             print(table[j][i].rjust(temp, ' '), end='')
#         print()
# printTable(tableData)
