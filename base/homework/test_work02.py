#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from base.homework.work01 import login_check


class TestLogin(unittest.TestCase):
    def test_login_pass(self):
        # 第一步：准备测试用例数据
        params = {'username': 'admin', 'password': 'pwd'}
        expected = {'code': 0, 'msg': '登录成功'}

        # 第二步：调用被测的功能函数
        res = login_check(username=params['username'], password=params['password'])

        # 第三步：断言
        assert res == expected

    def test_login_user_error(self):
        params = {'username': 'admin1', 'password': 'pwd'}
        expected = {'code': 1, 'msg': '账号或密码不正确'}
        res = login_check(username=params['username'], password=params['password'])
        assert res == expected

    def test_login_pwd_error(self):
        params = {'username': 'admin1', 'password': 'pwd1'}
        expected = {'code': 1, 'msg': '账号或密码不正确1'}
        res = login_check(username=params['username'], password=params['password'])
        assert res == expected


class TestRegister(unittest.TestCase):
    def test_register_01(self):
        assert 'OK' == 'NO'

    def test_register_02(self):
        assert '100' == '100'
