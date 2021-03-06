#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : get_median.py
# Author            : lryong <15816537946@163.com>
# Date              : 01.06.2019
# Last Modified Date: 01.06.2019
# Last Modified By  : lryong <15816537946@163.com>
# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。


class Solution:
    def __init__(self):
        self.ret = []

    def Insert(self, num):
        # write code here
        n = len(self.ret)
        self.ret.append(num)
        while n != 0:
            if self.ret[n] > self.ret[n-1]:
                self.ret[n], self.ret[n-1] = self.ret[n-1], self.ret[n]
            n -= 1

    def GetMedian(self,x):
        # write code here
        n = len(self.ret)
        if n % 2 == 0:
            return (self.ret[n/2]+self.ret[n/2-1])/2.0
        return self.ret[n/2]
