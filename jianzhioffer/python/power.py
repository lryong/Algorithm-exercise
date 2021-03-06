#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方

# My Solution:
class Solution:
    def Power(self, base, exponet):
        if base == 0:
            return 0
        return base ** exponet

# Better Solution:
# 快速排序法

class Solution:
    def fast_poewr(self, base, exponet):
        if base == 0:
            return 0
        if exponet == 0:
            return 1
        e = abs(exponet)
        tmp = base
        res = 1
        while(e > 0):
            # 如果最后一位为1， 那么给res乘上这一位的结果
            if ( e& 1 == 1):
                res = res * tmp
            e = e >> 1
            tmp = tmp * tmp
        return res if exponet > 0 else 1/exponet
            
