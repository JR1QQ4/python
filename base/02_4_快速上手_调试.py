#!/usr/bin/python
# -*- coding:utf-8 -*-

# 第二部分 自动化任务

print('********* 第 10 章 调试 ***********')

# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol must be a single character string.')
#     if width <= 2:
#         raise Exception('Width must be greater than 2.')
#     if height <= 2:
#         raise Exception('Height must be greater than 2.')
#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(symbol * width)
# for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
#     try:
#         boxPrint(sym, w, h)
#     except Exception as err:
#         print('An exception happened: ' + str(err))

# 取得反向跟踪的字符串
# 把打印输出到文件
# import traceback
# try:
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('data\\errorInfo.txt', 'w')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written to errorInfo.txt.')

# 断言
# assert 断言的条件, 断言失败时的提示信息
# podBayDoorStatus = 'open'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
# podBayDoorStatus = "I'm sorry, Dave. I'm afraid I can't do that."
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

# market_2nd = {'ns': 'green', 'ew': 'red'}
# mission_16th = {'ns': 'red', 'ew': 'green'}
# def switchLights(stoplight):
#     for key in stoplight.keys():
#         if stoplight[key] == 'green':
#             stoplight[key] = 'yellow'
#         elif stoplight[key] == 'yellow':
#             stoplight[key] = 'red'
#         elif stoplight[key] == 'red':
#             stoplight[key] = 'green'
#     assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
#     print(stoplight)
# switchLights(market_2nd)

# 日志
# import logging
#
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s '
#                                                 '- %(message)s')
# logging.debug('Start of program')
#
#
# def factorial(n):
#     logging.debug('Start of factorial(%s)' % n)
#     total = 1
#     for i in range(1, n + 1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(%s)' % n)
#     return total
#
#
# print(factorial(5))
# logging.debug('End of program')

# 日志级别：
# - DEBUG  最低级别，用于小细节，通常只有在诊断问题时，你才会关心这些消息
# - INFO   用于记录程序中一般事件的信息，或确认一切工作正常
# - WARNING  用于表示可能的问题，它不会阻止程序的工作，但将来可能会
# - ERROR  用于记录错误，它导致程序做某事失败
# - CRITICAL  最高级别，用于表示致命的错误，它导致或将要导致程序完全停止工作
# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - '
#                                                 '%(levelname)s - %(message)s')
# logging.debug('Some debugging details.')
# logging.info('The logging module is working.')
# logging.warning('An error message is about to be logged.')
# logging.error('An error has occurred.')
# logging.critical('The program is unable to recover!')

# 禁用日志
# import logging
# logging.basicConfig(level=logging.INFO, format=' %(asctime)s - '
#                                                '%(levelname)s - %(message)s')
# logging.critical('Critical error! Critical error!')
# logging.disable(logging.CRITICAL)
# logging.critical('Critical error! Critical error!')  # 禁用之后无输出
# logging.error('Error! Error!')

# 将日志记录到文件
# import logging
# logging.basicConfig(filename='data\\myProgramLog.txt', level=logging.INFO,
#                     format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.error('Error! Error!')

# spam = 5
# assert spam >= 10, 'spam lower 10'

# eggs = 'hello'
# bacon = 'Hello'
# assert eggs.lower() != bacon.lower(), 'eggs equal bacon'

# import random
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input()
#     toss = random.randint(0, 1)  # 0 is tails, 1 is heads
#     if toss == int(guess):
#         print('You got it!')
#     else:
#         print('Nope! Guess again!')
#         guesss = input()
#         if toss == int(guesss):
#             print('You got it!')
#         else:
#             print('Nope. You are really bad at this game.')
