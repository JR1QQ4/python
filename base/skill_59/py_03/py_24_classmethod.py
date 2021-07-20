#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 24 条: 以 @classmethod 形式的多态去通用地构建对象

# 在 Python 程序中，每个类只能有一个构造器，也就是 __init__ 方法
# 通过 @classmethod 机制，可以用一种与构造器相仿地方式来构造类地对象
# 通过类方法多态机制，我们能够以更加通用地方式构建并拼接具体地子类


class InputDate(object):
    def read(self):
        raise NotImplementedError


class PathInputData(InputDate):
    def __init__(self, path):
        super(PathInputData, self).__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


import os


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


from threading import Thread


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


print('=========================================')


class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class GenericPathInputData(GenericInputData):
    def __init__(self, path):
        super(GenericPathInputData, self).__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class GenericLineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def mapreduce1(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


print('-------------------------------------------')

# with open('') as f:
#     config = {'data_dir': f}
#     result = mapreduce1(LineCountWorker, GenericPathInputData, config)


