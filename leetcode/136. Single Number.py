#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
找到列表中只出现一次的那个数
1、set集合的用法学习。判断重复性的东西第一时间转成set。将有重复数据的list转成set时 就自动去重复了。
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # while True:
    #     a=nums.pop()
    #     if a in nums:
    #         nums.remove(a)
    #     else:
    #         return a
    # for i in nums:
    #     if i not in nums[nums.index(i)+1:]:
    #         return i
    return 2 * sum(set(nums)) - sum(nums)

