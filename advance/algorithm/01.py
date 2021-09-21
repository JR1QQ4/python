#!/usr/bin/python
# -*- coding:utf-8 -*-
import math


# 1、二分查找
# 前提：有序列表
# def binary_search(lst: list, item):
#     low = 0
#     high = len(lst) - 1
#     while low <= high:
#         mid = (low + high) / 2
#         guess = lst[math.floor(mid)]
#         print("mid={}, guess={}, high={}".format(mid, guess, high))
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             high = mid + 1
#     return None
# my_list = [1, 3, 5, 7, 9]
# print(binary_search(my_list, 3))
# print(binary_search(my_list, -1))

# 2、大O表示法，算法运行时间用大O表示法表示
# O(log n)，对数时间，二分查找
# O(n)，线性时间，简单查找
# O(n * log n)，快速排序
# O(n^2)，选择排序
# O(n!)，旅行商问题的解决方案

# 3、链表与数组
# 读取：数组 O(1)，链表 O(n)
# 插入：数组 O(n)，链表 O(1)
# 删除：数组 O(n)，链表 O(1)

# 4、选择排序
def findSmallest(arr: list):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
def selectionSort(arr: list):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
print(selectionSort([5, 3, 6, 2, 10]))





