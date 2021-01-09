#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 22 条: 尽量用辅助类来维护程序的状态，而不要用字典和元组

# 不要使用包含其他字典的字典，也不要使用过长的元组
# 如果容器中包含简单而又不可变的数据，那么可以先使用 namedtuple 来表示，待稍后有需要时，再修改为完整的类
# 保存内存状态的字典如果变得比较复杂，那就应该把这些代码拆解为多个辅助类


class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


book = SimpleGradebook()

book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)
book.report_grade('Isaac Newton', 95)
book.report_grade('Isaac Newton', 93)
print(book.average_grade('Isaac Newton'))


class BySubjectGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        print(by_subject)
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 95)
print(book.average_grade('Albert Einstein'))


class WeightedGradebook(object):
    def __init__(self):
        self._grades = {}

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                pass
        return score_sum / score_count


print('*' * 50)


import collections

Animal = collections.namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age=31, type='cat')
print(perry)  # Animal(name='perry', age=31, type='cat')
print(perry.name)  # perry

Grade = collections.namedtuple('Grade', ('score', 'weight'))

g = Grade(score=100, weight=0.2)
print(g)  # Grade(score=100, weight=0.2)
print(g.score)  # 100


class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        print(total, total_weight)
        return total / total_weight


class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]


book = Gradebook()
albert = book.student('Albert Einstein')
math = albert.subject('Math')
math.report_grade(80, 0.10)
math = albert.subject('physics')
math.report_grade(99, 0.30)
print(albert.average_grade())















