#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

# My Solution
class Solution:
    def jumpFloor(self, number):
        a, b = 1, 1
        while number > 0:
            a, b = b, a + b
            n -= 1
        return a 

# Better Solution -> 递归
