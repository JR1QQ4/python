#!/usr/bin/python
# -*- coding:utf-8 -*-
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return len(set(nums)) < len(nums)
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i != j:
                    return True
        return False
