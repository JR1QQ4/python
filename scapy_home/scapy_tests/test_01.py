#!/usr/bin/python
# -*- coding:utf-8 -*-
# Requests + 正则表达式爬取猫眼电影TOP100
# url: https://maoyan.com/board/4
import json
import re
from multiprocessing import Pool

import requests
from requests.exceptions import RequestException


def get_one_page(url):
    """访问网页获取内容"""
    try:

        headers = {
            'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                            ' (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        res = requests.get(url, headers=headers)
        # 乱码问题
        # 解决方法一
        # res.encoding = res.apparent_encoding
        # 解决方法二，根据html中的<meta charset="utf-8">判断
        res.encoding = "utf-8"
        if res.status_code == 200:
            # 解决方法三
            # return res.text.encode("latin1").decode("utf-8")
            return res.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    """提取想要的内容"""
    pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            "index": item[0],
            "image": item[1],
            "title": items[2],
            "actor": items[3].strip()[3:],
            "time": items[4].strip()[5:],
            "score": items[5] + item[6]
        }


def write_to_file(content):
    """写入文件"""
    with open("result.txt", "w", encoding="utf-8") as fs:
        fs.write(json.dumps(content) + "\n")


class Test01:
    def __init__(self):
        self.url = "http://maoyan.com/board/4"
        self.html = get_one_page(self.url)

    def test_01(self):
        print(self.html)
        for item in parse_one_page(self.html):
            print(item)
            write_to_file(item)

    def test_02(self, offset):
        """遍历多个页面"""
        self.url = "http://maoyan.com/board/4?" + offset
        self.html = get_one_page(self.url)
        print(self.html)
        for item in parse_one_page(self.html):
            print(item)
            write_to_file(item)


if __name__ == '__main__':
    t = Test01()
    # t.test_01()

    # 普通方法抓取多个页面
    # for i in range(10):
    #     t.test_02(i)

    # 使用线程池的方式执行抓取多个页面
    pool = Pool()
    pool.map(t.test_02, [i*10 for i in range(10)])
