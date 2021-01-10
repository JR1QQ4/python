#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 28 条: 继承 collections.abc 以实现自定义的容器类型

# 如果要定制的子类比较简单，那就可以直接从 Python 的容器类型(如 list 或 dict)中继承
# 像正确实现自定义的容器类型，可能需要编写大量的特殊放啊
# 编写自制的容器类型时，可以从 collections.abc 模块的抽象基类中继承，那些基类能够确保我们的子类具备适当的接口及行为


class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts


foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
print('Length is', len(foo))  # Length is 7
foo.pop()
print('After pop:', repr(foo))  # After pop: ['a', 'b', 'a', 'c', 'b', 'a']
print('Frequency:', foo.frequency())  # Frequency: {'a': 3, 'b': 2, 'c': 1}


class BinaryNode(object):
    def __int__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


bar = [1, 2, 3]
print(bar[0])  # 1
print(bar.__getitem__(0))  # 1


# class IndexableNode(BinaryNode):
#     def _search(self, count, index):
#         return (found, count)
#
#     def __getitem__(self, index):
#         found, _ = self._search(0, index)
#         if not found:
#             raise IndexError('Index out of range')
#         return found.value


from collections.abc import Sequence


class BadType(Sequence):
    pass
# foo = BadType()  # TypeError: Can't instantiate abstract class BadType


# class BetterNode(SequenceNode, Sequence):
#     pass
























