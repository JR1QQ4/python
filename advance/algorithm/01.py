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
# def findSmallest(arr: list):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
# def selectionSort(arr: list):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr
# print(selectionSort([5, 3, 6, 2, 10]))

# 5、递归
# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x - 1)

# 6、快速排序
# def sum(arr):
#     total = 0
#     for x in arr:
#         total += x
#     return total
# print(sum([1, 2, 3, 4]))
# 步骤：（1）选择基准值；（2）将数组分成两个子数组：小于基准值的元素和大于基准值的元素；（3）对这两个子数组进行快速排序
# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort([10, 5, 2, 3]))  # [2, 3, 5, 10]

# 7、散列表
# cache = {}
# def get_data_from_server(url):
#     return None
# def get_page(url):
#     if cache.get(url):
#         return cache[url]
#     else:
#         data = get_data_from_server(url)
#         cache[url] = data
#         return data

# 8、广度优先搜索
# 队列——先进先出（FIFO）；栈——后进先出（LIFO）
# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []  # 这个数组用于记录检查过的人
#     while search_queue:
#         person = search_queue.popleft()
#         if person not in searched:  # 仅当这个人没检查过时才检查
#             if person_is_seller(person):
#                 print(person + " is a mango seller!")
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)  # 将这个人标记为检查过
#     return False
# search("you")

# 9、狄克斯特拉算法
# 权重（Weight），带权重的图称为加权图（weighted graph），不带权重的称为非加权图（unweighted graph）
# processed = []
# def find_lowest_cost_node(costs):
#     lowest_cost = float("inf")
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node
# node = find_lowest_cost_node(costs)  # 在未处理的节点中找出开销最小的节点
# while node is not None:  # 在所有节点被处理后结束
#     cost = costs[node]
#     neighbors = graph[node]
#     for n in neighbors.keys():  # 遍历当前节点的所有邻居
#         new_cost = cost + neighbors[n]
#         if costs[n] > new_cost:  # 如果经当前节点前往该邻居更近
#             costs[n] = new_cost  # 就更新邻居的开销
#             parents[n] = node  # 同时将邻居节点的父节点设置为当前节点
# processed.append(node)  # 将当前节点标记为处理过
# node = find_lowest_cost_node(costs)  # 找出接下来要处理的节点，并循环

# 10、贪婪算法
# 贪婪算法很简单：每步都采取最优的做法
# 面临NP完全问题时，最佳的做法是使用近似算法
















