#!/usr/bin/python
# -*- coding:utf-8 -*-
# 分析Ajax来抓取今日头条街拍美图
import json
from urllib.parse import urlencode

from requests.exceptions import RequestException
import requests


def get_page_index(offset, keyword):
    try:
        global headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/91.0.4472.77 Safari/537.36',
        }
        params = {
            'keyword': keyword,
            'pd': 'atlas',
            'dvpf': 'pc',
            'aid': 4916,
            'page_num': offset,
            'search_json': '{"from_search_id":"2021061412254001022819715000B9C21D",'
                           '"origin_keyword":"街拍","image_keyword":"街拍"}',
        }
        url = "http://so.toutiao.com/search?" + urlencode(params)
        res = requests.get(url, headers=headers, params=params)
        if res.status_code == 200:
            return res.json()
        return None
    except RequestException:
        print("请求索引页出错")
        return None


def parse_page_index(html):
    print(data)
    # if data and 'data' in data.keys():
    #     for item in data.get("data"):
    #         yield item.get("article_url")


def main():
    html = get_page_index(0, '街拍')
    parse_page_index(html)


if __name__ == '__main__':
    main()
