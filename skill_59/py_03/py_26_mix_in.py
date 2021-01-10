#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 26 条: 只在使用 Mix-in 组件制作工具类时进行多重继承

# 能用 mix-in 组件实现的效果，就不用多重继承来做
# 将各功能实现为可插拔的 mix-in 组件，然后令相关的类继承自己需要的那些组件，即可定制该类实例所具备的行为
# 把简单的行为封装到 mix-in 组件里，然后就可以用多个 mix-in 组合出复杂的行为了


class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = BinaryTree(10,
                  left=BinaryTree(7, right=BinaryTree(9)),
                  right=BinaryTree(13, left=BinaryTree(11)))
from pprint import pprint
pprint(tree.to_dict(), indent=2)


class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent
    
    def _traverse(self, key, value):
        if isinstance(value, BinaryTreeWithParent) and key == 'parent':
            return value.value
        else:
            return super()._traverse(key, value)


root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
pprint(root.to_dict(), indent=2)


class NamedSunTree(ToDictMixin):
    def __init__(self, name, tree_with_parent):
        self.name = name
        self.tree_with_parent = tree_with_parent


my_tree = NamedSunTree('foobar', root.left.right)
pprint(my_tree.to_dict())


import json
class JsonMixin(object):
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict())


class Switch(ToDictMixin, JsonMixin):
    pass


class Machine(ToDictMixin, JsonMixin):
    pass


class DatacenterRack(ToDictMixin, JsonMixin):
    def __init__(self, switch=None, machines=None):
        self.switch = Switch(**switch)
        self.machines = [Machine(**kwargs) for kwargs in machines]




















