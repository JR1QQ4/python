#!/usr/bin/python
# -*- coding:utf-8 -*-
import http.cookiejar
import socket
from urllib import request, parse, error, robotparser
from urllib.parse import urlparse, urlunparse, urljoin, urlencode


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
        """传递请求阐述"""
        url = 'http://www.python.org'
        params = {'name': 'Tom'}
        data = bytes(parse.urlencode(params), encoding='utf-8')
        req = request.Request(url=url, data=data, method='POST')
        res = request.urlopen(req)
        print(res.read().decode('utf-8'))

    @staticmethod
    def test9():
        """传递header"""
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
        """add_header添加header的另一种方法"""
        url = 'http://www.python.org'
        params = {'name': 'Tom'}
        data = bytes(parse.urlencode(params), encoding='utf-8')
        req = request.Request(url=url, data=data, method='POST')
        req.add_header('User-Agent', 'User-Agent:Mozilla/4.0(compatible, MISE 5.5,windows NT)')
        res = request.urlopen(req)
        print(res.read().decode('utf-8'))

    @staticmethod
    def test11():
        """代理设置"""
        proxy_handler = request.ProxyHandler({
            'http': 'http://127.0.0.1:8888',
            'https': 'https://127.0.0.1:8888'
        })
        opener = request.build_opener(proxy_handler)
        res = opener.open('http://www.baidu.com')
        print(res.read())

    @staticmethod
    def test12():
        """Cookies"""
        cookie = http.cookiejar.CookieJar()
        handler = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(handler)
        res = opener.open('http://www.baidu.com')
        for item in cookie:
            print(item.name + '=' + item.value)

    @staticmethod
    def test13():
        filename = "cookie.txt"
        cookie = http.cookiejar.MozillaCookieJar(filename)
        handler = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(handler)
        res = opener.open("http://www.baidu.com")
        cookie.save(ignore_discard=True, ignore_expires=True)

    @staticmethod
    def test14():
        filename = "cookie.txt"
        cookie = http.cookiejar.LWPCookieJar(filename)
        handler = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(handler)
        res = opener.open("http://www.baidu.com")
        cookie.save(ignore_discard=True, ignore_expires=True)

    @staticmethod
    def test15():
        cookie = http.cookiejar.LWPCookieJar()
        cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
        handler = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(handler)
        res = opener.open("http://www.baidu.com")
        print(res.read().decode('utf-8'))

    @staticmethod
    def test16():
        try:
            res = request.urlopen("http://dadsadwedqd.com/index.html")
        except error.URLError as e:
            print(e.reason)

    @staticmethod
    def test17():
        try:
            res = request.urlopen("http://dadsadwedqd.com/index.html")
        except error.HTTPError as e:
            print(e.reason, e.code, e.headers, sep='\n')
        except error.URLError as e:
            print(e.reason)
        else:
            print("Request Successfully")

    @staticmethod
    def test18():
        try:
            res = request.urlopen("http://baidu.com", timeout=0.1)
        except error.URLError as e:
            print(e.reason)
            if isinstance(e.reason, socket.timeout):
                print("TIME OUT")

    @staticmethod
    def test19():
        """urlparse 解析"""
        result = urlparse("http://www.baidu.com/index.html?id=5#comment")
        print(type(result), result)

    @staticmethod
    def test20():
        result = urlparse("www.baidu.com/index.html?id=5#comment", scheme='https')
        print(result)

    @staticmethod
    def test21():
        result = urlparse("http://www.baidu.com/index.html?id=5#comment", scheme='https')
        print(result)

    @staticmethod
    def test22():
        result = urlparse("http://www.baidu.com/index.html?id=5#comment", allow_fragments=False)
        print(result)

    @staticmethod
    def test23():
        result = urlparse("http://www.baidu.com/index.html#comment", allow_fragments=False)
        print(result)

    @staticmethod
    def test24():
        data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
        print(urlunparse(data))

    @staticmethod
    def test25():
        print(urljoin('http://www.baidu.com', 'FQA.html'))
        print(urljoin('http://www.baidu.com', 'https://www.httpbin.com/FQA.html'))
        print(urljoin('http://www.baidu.com/about.html', 'https://www.httpbin.com/FQA.html'))

    @staticmethod
    def test26():
        params = {
            'name': 'Tom',
            'age': 22
        }
        base_url = 'http://www.baidu.com?'
        url = base_url + urlencode(params)
        print(url)

    @staticmethod
    def test27():
        rp = robotparser.RobotFileParser()
        rp.set_url("http://www.musi-cal.com/robots.txt")
        rp.read()
        rrate = rp.request_rate("*")
        print(rrate.requests)
        print(rrate.seconds)
        print(rp.crawl_delay("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco"))
        print(rp.can_fetch("*", "http://www.musi-cal.com"))


if __name__ == '__main__':
    # 响应
    # UrllibTest.test1()
    # UrllibTest.test2()
    # UrllibTest.test3()
    # UrllibTest.test4()
    # UrllibTest.test7()

    # 响应
    # UrllibTest.test5()
    # UrllibTest.test6()
    # UrllibTest.test8()
    # UrllibTest.test9()
    # UrllibTest.test10()

    # 代理
    # UrllibTest.test11()

    # Cookie
    # UrllibTest.test12()
    # UrllibTest.test13()
    # UrllibTest.test14()
    # UrllibTest.test15()

    # 异常
    # UrllibTest.test16()
    # UrllibTest.test17()
    # UrllibTest.test18()

    # URL解析
    # UrllibTest.test19()
    # UrllibTest.test20()
    # UrllibTest.test21()
    # UrllibTest.test22()
    UrllibTest.test23()
    UrllibTest.test24()
    UrllibTest.test25()
    UrllibTest.test26()
