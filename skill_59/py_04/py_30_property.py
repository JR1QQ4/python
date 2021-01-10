#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 30 条: 考虑用 @property 来代替属性重构

# @property 可以为现有得实例属性添加新得功能
# 可以用 @property 来逐步完善数据模型
# 如果 @property 用得太过频繁，那就应该考虑彻底重构该类并修改相关得调用代码
from datetime import timedelta, datetime


class Buket(object):
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        # self.quota = 0

        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        # return 'Bucket(quota=%d)' % self.quota
        return ('Bucket(max_quota=%d, quota_consumed=%d)' %
                (self.max_quota, self.quota_consumed))

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


def fill(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount


def deduct(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True


bucket = Buket(60)
fill(bucket, 100)
print(bucket)

if deduct(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print(bucket)
