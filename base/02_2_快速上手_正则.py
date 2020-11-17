#!/usr/bin/python
# -*- coding:utf-8 -*-

# 第二部分 自动化任务

print('********* 第 7 章 模式匹配与正则表达式 ***********')

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True
# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneNumber('Moshi moshi'))
# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
# print('Done')

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo)
print(mo.group())
print(mo.groups())    # ()

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo)
print(mo.group())     # 415-555-4242
print(mo.group(0))    # 415-555-4242
print(mo.group(1))    # 415
print(mo.group(2))    # 555-4242
# print(mo.group(3))    # IndexError: no such group
print(mo.groups())    # ('415', '555-4242')

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))  # (415)

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())  # Batman

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group(1))  # mobile

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())  # Batman
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group(1))  # wo

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())  # Batman
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())  # Batwoman
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())  # Batwowowowoman

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 is None)  # True

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 is None)  # True

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())  # HaHaHaHaHa

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())  # HaHaHa

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())  # 415-555-9999

# reg.findall
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# \d \D除0到9的数字以外的任何字符
# \w任何字母数字或下划线字符（可认为匹配'单词'） \W除字母数字和下划线以外的任意字符
# \s \S除空格制表符和换行符以外的任何字符
# .除换行符以外的

xmasRegex = re.compile(r'\d+\s\w+')
res = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 '
                        'swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(res)

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('12345xyz67890') is None)
print(wholeStringIsNum.search('12 34567890') is None)

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.groups())  # ('Al', 'Sweigart')

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())  # <To serve man>

nongreedyRegex = re.compile(r'<.*>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())  # <To serve man> for dinner.>

noNewlineRegex = re.compile('.*')
res = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\n'
                            'Uphold the law.').group()
print(res)  # Serve the public trust.

newlineRegex = re.compile('.*', flags=re.DOTALL)
res = newlineRegex.search('Serve the public trust.\nProtect the innocent.\n'
                          'Uphold the law.').group()
print(res)

robocop = re.compile(r'robocop', re.I)
res = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(res)  # RoboCop

namesRegex = re.compile(r'Agent \w+')
res = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(res)  # CENSORED gave the secret documents to CENSORED.

# phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}'
#                         r'(\s*(ext|x|ext.)\s*\d{2,5})?)')
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?              # area code
#     (\s|-|\.)?                      # separator
#     \d{3}                           # first 3 digits
#     (\s|-|\.)                       # separator
#     \d{4}                           # last 4 digits
#     (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
#     )''', re.VERBOSE)  # 编写注释

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# import pyperclip
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?             # area code
#     (\s|-|\.)?                     # separator
#     (\d{3})                        # first 3 digits
#     (\s|-|\.)                      # separator
#     (\d{4})                        # last 4 digits
#     (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
#     )''', re.VERBOSE)
# emailRegex = re.compile(r'''(
#     [a-zA-Z0-9._%+-]+ # username
#     @                 # @ symbol
#     [a-zA-Z0-9.-]+    # domain name
#     (\.[a-zA-Z]{2,4}) # dot-something
#     )''', re.VERBOSE)
# text = str(pyperclip.paste())
# matches = []
# for groups in phoneRegex.findall(text):
#     phoneNum = '-'.join([groups[1], groups[3], groups[5]])
#     if groups[8] != '':
#         phoneNum += ' x' + groups[8]
#     matches.append(phoneNum)
# for groups in emailRegex.findall(text):
#     matches.append(groups[0])
# if len(matches) > 0:
#     pyperclip.copy('\n'.join(matches))
#     print('Copied to clipboard:')
#     print('\n'.join(matches))
# else:
#     print('No phone numbers or email addresses found.')

numRegex = re.compile(r'\d+')
print(numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens'))
