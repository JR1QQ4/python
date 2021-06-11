#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
from requests.packages import urllib3


class RequestsTest:
    @staticmethod
    def test1():
        res = requests.get("http://www.baidu.com")
        print(type(res))
        print(res.status_code)
        print(type(res.text))
        print(res.text)
        print(res.cookies)

    @staticmethod
    def test2():
        """各种请求方式"""
        requests.post("http://www.baidu.com")
        requests.put("http://www.baidu.com")
        requests.delete("http://www.baidu.com")
        requests.head("http://www.baidu.com")
        requests.options("http://www.baidu.com")

    @staticmethod
    def test3():
        """GET请求"""
        res = requests.get("http://httpbin.org/get")
        print(res.text)

    @staticmethod
    def test4():
        """带参数GET请求"""
        data = {
            'name': 'Tom',
            'age': 22
        }
        res = requests.get("http://httpbin.org/get", params=data)
        print(res.text)

    @staticmethod
    def test5():
        """解析json"""
        res = requests.get("http://httpbin.org/get")
        print(type(res.text))
        print(res.json())
        print(type(res.json()))

    @staticmethod
    def test6():
        """获取二进制数据"""
        res = requests.get("https://cn.bing.com/sa/simg/favicon-2x.ico")
        print(type(res.text), type(res.content))
        print(res.text)
        print(res.content)
        with open('favicon.ico', 'wb') as fs:
            fs.write(res.content)

    @staticmethod
    def test7():
        """添加headers"""
        # res = requests.get('https://www.zhihu.com/explore')
        # print(res.text)
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) "
                          "Chrome/14.0.835.163 Safari/535.1"
        }
        res = requests.get('https://www.zhihu.com/explore', headers=headers)
        print(res.text)

    @staticmethod
    def test8():
        data = {
            'name': 'tom',
            'age': 22
        }
        res = requests.post("http://httpbin.org/post", data=data)
        print(res.text)

    @staticmethod
    def test9():
        data = {
            'name': 'tom',
            'age': 22
        }
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) "
                          "Chrome/14.0.835.163 Safari/535.1"
        }
        res = requests.post("http://httpbin.org/post", headers=headers, data=data)
        print(res.json())

    @staticmethod
    def test10():
        """response属性"""
        res = requests.get('http://www.jianshu.com')
        print(type(res.status_code), res.status_code)
        print(type(res.headers), res.headers)
        print(type(res.cookies), res.cookies)
        print(type(res.url), res.url)
        print(type(res.history), res.history)

    @staticmethod
    def test11():
        """状态码判断"""
        res = requests.get('http://www.jianshu.com')
        exit() if not res.status_code == requests.codes.ok else print('Request Successfully')
        res = requests.get('http://www.jianshu.com')
        exit() if not res.status_code == 200 else print('Request Successfully')

    @staticmethod
    def test12():
        files = {'file': open('爬虫.md', 'rb')}
        res = requests.post("http://httpbin.org/post", files=files)
        print(res.text)

    @staticmethod
    def test13():
        """获取cookie"""
        res = requests.get("http://www.baidu.com")
        print(res.cookies)
        for key, value in res.cookies.items():
            print(key + "=" + value)

    @staticmethod
    def test14():
        """会话维持"""
        # requests.get("http://httpbin.org/cookies/set/number/123456789")
        # res = requests.get("http://httpbin.org/cookies")
        # print(res.text)

        s = requests.session()
        s.get("http://httpbin.org/cookies/set/number/123456789")
        res = s.get("http://httpbin.org/cookies")
        print(res.text)

    @staticmethod
    def test15():
        """证书验证"""
        # res = requests.get("https://www.12306.cn")
        # print(res.text)

        # 消除警告信息
        urllib3.disable_warnings()
        res = requests.get("https://www.12306.cn", verify=False)
        print(res.status_code)

        # res = requests.get("https://www.12306.cn", cert=("/path/server.crt", "/path/key"))
        # print(res.status_code)

    @staticmethod
    def test16():
        """代理设置"""
        proxies = {
            "http": "http://127.0.0.1:9743",
            "https": "https://127.0.0.1:9743"
        }
        res = requests.get("https://www.taobao.com", proxies=proxies)
        print(res.status_code)

        proxies = {
            "http": "http://user:password@127.0.0.1:9743"
        }
        res = requests.get("https://www.taobao.com", proxies=proxies)
        print(res.status_code)

        # pip3 install 'requests[socks]，socks代理
        proxies = {
            "http": "socks5://127.0.0.1:9742",
            "https": "socks5://127.0.0.1:9742"
        }
        res = requests.get("https://www.taobao.com", proxies=proxies)
        print(res.status_code)

    @staticmethod
    def test17():
        """超时设置"""
        from requests.exceptions import ReadTimeout
        try:
            res = requests.get("https://www.taobao.com", timeout=1)
            print(res.status_code)
        except ReadTimeout as e:
            print("TIME OUT")

    @staticmethod
    def test18():
        """认证设置"""
        from requests.auth import HTTPBasicAuth
        r = requests.get("http://120.27.34:24.9001", auth=HTTPBasicAuth("user", "123"))
        print(r.status_code)

        r = requests.get("http://120.27.34:24.9001", auth=("user", "123"))
        print(r.status_code)

    @staticmethod
    def test19():
        from requests.exceptions import ReadTimeout, HTTPError, RequestException
        try:
            res = requests.get("http://httpbin.org/get", timeout=0.5)
            print(res.status_code)
        except ReadTimeout:
            print("TIME OUT")
        except HTTPError:
            print("HTTP error")
        except RequestException:
            print("Error")


if __name__ == '__main__':
    # RequestsTest.test1()

    # GET请求
    # RequestsTest.test3()
    # RequestsTest.test4()
    # RequestsTest.test5()
    # RequestsTest.test6()
    # RequestsTest.test7()

    # POST请求
    # RequestsTest.test8()
    # RequestsTest.test9()

    # RequestsTest.test10()
    # RequestsTest.test11()

    # RequestsTest.test12()
    # RequestsTest.test13()
    # RequestsTest.test14()
    # RequestsTest.test15()
    # RequestsTest.test16()
    # RequestsTest.test17()
    # RequestsTest.test18()
    RequestsTest.test19()
