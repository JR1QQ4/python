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


"""
ddt 的使用步骤：
    1、测试类前面使用 ddt
    2、在测试方法前面使用 list_data(测试数据)
    3、在测试方法中定义一个参数，用来接收用例数据
"""
from unittestreport import ddt, list_data

cases = [
    {'expected': {'code': 1, 'msg': '账号或密码不正确1'}, 'params': {'username': 'admin1', 'password': 'pwd1'}},
    {'expected': {'code': 1, 'msg': '账号或密码不正确2'}, 'params': {'username': 'admin1', 'password': 'pwd2'}}
]


@ddt
class TestDDT(unittest.TestCase):
    @list_data(cases)
    def test_login(self, item):
        params = item['params']
        expected = item['expected']
        res = login_check(**params)
        self.assertEqual(expected, res)
