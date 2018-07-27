#!/usr/bin/env python
# -*- coding:utf-8 -*-

# My solution

'''
class Solution:
    def Find(self, target, array):
        for i in array:
            for k in i:
                if k == targe:
                    return True
'''

# 从左下角元素往上查找，右边元素是比这个元素大，上边是的元素比这个元素小。于是，target比这个元素小就往上找，比这个元素大就往右找。如果出了边界，则说明二维数组中不存在target元素。

class Solution:
    def Find(self, target, array):
        rows = len(array) -1
        cols = len(array[0]) -1
        i = rows
        j = 0
        while i >= 0 and j <= cols:
            if target > array[i][j]:
                j+=1
            elif target < array[i][j]:
                i-=1
            else:
                return True
        return False
