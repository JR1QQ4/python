#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket
from urllib import request, parse, error


class UrllibTest:
    @staticmethod
    def test1():
        response = request.urlopen('http://www.baidu.com')
        print(response.read().decode('utf-8'))

    @staticmethod
    def test2():
        data = bytes(parse.urlencode({'world': 'hello'}), encoding='utf-8')
        response = request.urlopen('http://httpbin.org/post', data=data)
        print(response.read())

    @staticmethod
    def test3():
        response = request.urlopen('http://httpbin.org/get', timeout=1)
        print(response.read())

    @staticmethod
    def test4():
        try:
            response = request.urlopen('http://httpbin.org/get', timeout=0.1)
            print(response.read())
        except error.URLError as e:
            if isinstance(e.reason, socket.timeout):
                print('TIME OUT')

    @staticmethod
    def test5():
        response = request.urlopen('http://www.python.org')
        print(response)

    @staticmethod
    def test6():
        response = request.urlopen('http://www.python.org')
        print(response.status)
        # print(response.getheaders())
        print(response.getheaders('Server'))

    @staticmethod
    def test7():
        req = request.Request('http://www.python.org')
        res = request.urlopen(req)
        print(res.read().decode('utf-8'))

    @staticmethod
    def test8():
        url = 'http://www.python.org'
        params = {'name': 'Tom'}
        data = bytes(parse.urlencode(params), encoding='utf-8')
        req = request.Request(url=url, data=data, method='POST')
        res = request.urlopen(req)
        print(res.read().decode('utf-8'))

    @staticmethod
    def test9():
        url = 'http://www.python.org'
        params = {'name': 'Tom'}
        headers = {
            'User-Agent': 'User-Agent:Mozilla/4.0(compatible, MISE 5.5,windows NT)',
            'Host': 'httpbin.org'
        }
        data = bytes(parse.urlencode(params), encoding='utf-8')
        req = request.Request(url=url, data=data, headers=headers, method='POST')
        res = request.urlopen(req)
        print(res.read().decode('utf-8'))

    @staticmethod
    def test10():
        proxy_handler = request.ProxyHandler({'http': 'http://127.0.0.1:9743'})


if __name__ == '__main__':
    # 响应
    # UrllibTest.test1()
    # UrllibTest.test2()
    # UrllibTest.test3()
    # UrllibTest.test4()
    UrllibTest.test7()

    # 响应
    # UrllibTest.test5()
    # UrllibTest.test6()
