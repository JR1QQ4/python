#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 3 条: 了解 bytes、str 与 unicode 的区别

# Python3 有两种表示序列的类型 bytes 和 str，前者的实例包含原始的 8 位值，后者的实例包含 Unicode 字符
# Python2 有两种表示字符序列的类型 str 和 unicode，str 的实例包含原始的 8 位值，而 Unicode 的实例包含 Unicode 字符
# Python3 的 str 实例和 Python2 的 unicode 实例都没有和特定的二进制编码相关联，要把 Unicode 转换成二进制必须使用 encode

# 程序的核心部分应该使用 Unicode 字符类型(Python3中的str、Python2中的unicode)，而且不要对字符编码做任何假设
# 这种办法既可以领程序接受多种类型的文本编码(如Latin-l、Shift JIS 和 Big5)，又可以保证输出的文本信息只采用一种编码形式(UTF-8)

# 由于字符类型有别，所以 Python 代码中经常会出现两种常见的使用情境:
# 1.开发者需要原始 8 位值，这些 8 位值表示以 UTF-8 格式(或其他编码形式)来编码的字符
# 2.开发者需要操作没有特定编码形式的 Unicode 字符

# Python 3 中向文件中写入一些二进制数据，需要添加 encoding 的参数
# 写入二进制数据，不添加 encoding 可以采用二进制写入模式('wb')
import os
with open('/tmp/random.bin', 'w', encoding='utf-8') as f:
    f.write(os.urandom(10))
with open('/tmp/random.bin', 'wb') as f:
    f.write(os.urandom(10))


def to_str(bytes_or_str):
    """Python 3 中 bytes 转为 str"""
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    """Python 3 中 str 转为 bytes"""
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


print('hello'.encode('utf-8'))  # b'hello'
print(to_str('hello'.encode('utf-8')))  # hello
print(to_bytes('hello'))  # b'hello'


# def to_unicode(unicode_or_str):
#     """Python 2 中 str 转为 unicode"""
#     if isinstance(unicode_or_str, str):
#         value = unicode_or_str.decode('utf-8')
#     else:
#         value = unicode_or_str
#     return value
# 
# 
# def to_str(unicode_or_str):
#     """Python 2 中 unicode 转为 str"""
#     if isinstance(unicode_or_str, unicode):
#         value = unicode_or_str.encode('utf-8')
#     else:
#         value = unicode_or_str
#     return value


