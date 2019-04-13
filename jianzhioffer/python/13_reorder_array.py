#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 13_reorder_array.py
# Author            : lryong <15816537946@163.com>
# Date              : 13.04.2019
# Last Modified Date: 13.04.2019
# Last Modified By  : lryong <15816537946@163.com>
i#!/usr/vin/env python
# -*- coding:utf-8 -*-

# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

# My Solution
class Solution:
    def reOrderArray(self, array):
        odd_list = []
        even_list = []
        for i in array:
            if i%2:
                odd_list.append(i)
            else:
                even_list.append(i)
        return odd_list + even_list

# better solution
# 插入排序法
