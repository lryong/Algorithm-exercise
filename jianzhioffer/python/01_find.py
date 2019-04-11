#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : find.py
# Author            : lryong <15816537946@163.com>
# Date              : 06.04.2019
# Last Modified Date: 12.04.2019
# Last Modified By  : lryong <15816537946@163.com>
#!/usr/bin/python

# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# 思路
'''
思路1
二维数组(矩阵)是有序的, 从左下角来看, 向右数字递增， 向上数字递减。因此从左下角开始查找, 当要查找的数字比左下角数字大时， 右移。要查找数字比左下角小时， 上移。
'''

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        if not target:
            return False
        for i in xrange(len(array)-1,-1,-1):
            for j in xrange(len(array[0])):
                if target == array[i][j]:
                    return True
                if target < array[i][j]:
                    break
        return False

'''
思路2
二分查找
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        if not target:
            return False
        for i in array:
            low = 0
            high = len(i)-1
            while low <= high:
                mid = (low + high)/2
                if target > i[mid]:
                    low = mid+1
                elif target < i[mid] :
                    high = mid -1
                else:
                    return True


print  Solution().Find(1,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
