#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 31 条: 用描述符来改写需要符用 @property 方法

# 如果想复用 @property 方法及其验证机制，那么可以自己定义描述符类
# WeakKeyDictionary 可以保证描述符类不会泄露内存
# 通过描述符协议来实现属性得获取和设置操作时，不要纠结于 __getattribute__ 的方法具体运作细节
# WeakKeyDictionary：
#   如果运行期系统发现这种字典所持有得引用，使整个程序里面指向 Exam 实例得最后一份引用，那么，系统就会自动将实例从字典得键中移除

class Homework(object):
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value


galileo = Homework()
galileo.grade = 95
print(galileo.__dict__)  # {'_grade': 95}


class Exam(object):
    def __int__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value


from weakref import WeakKeyDictionary
class Grade(object):
    def __int__(self):
        # self._value = 0  # 多个实例调用同一个

        # self._values = {}  # 报错，会内存泄露，引用计数无法降为 0，从而使垃圾收集其无法将其回收

        self._values = WeakKeyDictionary()  # 特殊的字典

    def __get__(self, instance, instance_type):
        # return self._value

        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        # self._value = value

        self._values[instance] = value


class NewExam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


exam = NewExam()
exam.writing_grade = 40  # Exam.__dict__['writing_grade'].__set__(exam, 40)
print(exam.writing_grade)  # Exam.__dict__['writing_grade'].__get__(exam, Exam)

# second_exam = NewExam()
# second_exam.writing_grade = 50
# print('Second', second_exam.writing_grade)
# print('First', exam.writing_grade)











