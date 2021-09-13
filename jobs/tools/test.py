#!/usr/bin/python
# -*- coding:utf-8 -*-
# coding:utf-8
import requests


def req(url, agent, cookie, authorization, email):
    headers = {
        "User-Agent": agent,
        "Cookie": cookie,
        "Authorization": authorization
    }
    data = {
        'code': "C989",
        'email': email,
        'name': "张军",
        'passcode': "",
        'student_id': 300,
    }
    for i in range(500, 1000):
        data = {
            'code': "C989",
            'email': email,
            'name': "张军",
            'passcode': "",
            'student_id': i,
        }
        res = requests.post(url=url, headers=headers, data=data)
        if res.status_code == 200:
            print(res.text, i)
        else:
            print(res.text, i)


agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
cookie = 'Hm_lvt_6f63cfeea8c9a84040e2c4389f01bb91=1631461766; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiOTM2ODAyMkBxcS5jb20iLCJuYW1lIjoi5LuK5aSpIiwiaWQiOiI3OTA1NTEiLCJyb2xlcyI6WyJzdHVkZW50Il0sImxhc3RfbG9naW4iOjB9LCJpYXQiOjE2MzE0NjE4ODMsImV4cCI6MTYzMjc1Nzg4M30.SCE2bb41iCYrycHRloEsqONjI1oui-VrhhY5nQUripY; Hm_lpvt_6f63cfeea8c9a84040e2c4389f01bb91=1631462187; io=VUXwXcA8ydGv5W96B-7B'
authorization = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiOTM2ODAyMkBxcS5jb20iLCJuYW1lIjoi5LuK5aSpIiwiaWQiOiI3OTA1NTEiLCJyb2xlcyI6WyJzdHVkZW50Il0sImxhc3RfbG9naW4iOjB9LCJpYXQiOjE2MzE0NjE4ODMsImV4cCI6MTYzMjc1Nzg4M30.SCE2bb41iCYrycHRloEsqONjI1oui-VrhhY5nQUripY'
email = '9368022@qq.com'
req("http://python123.io/api/v1/student/courses", agent, cookie,
    authorization, email)
