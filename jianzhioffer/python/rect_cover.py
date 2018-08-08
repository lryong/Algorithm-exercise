#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# Fibonacci数列 

#My Solution
class Solution:
    def rectCover(self, number):
        if number < 2:
            return number
        i, j = 1, 1
        for a in range(number):
            i, j = j, i+j
        return i
