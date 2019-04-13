#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 11_number_of_1.py
# Author            : lryong <15816537946@163.com>
# Date              : 13.04.2019
# Last Modified Date: 13.04.2019
# Last Modified By  : lryong <15816537946@163.com>
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

#trick的方法:
class Solution:
    def NumberOf1(self, n):
        return sum([n >> i & 1 for i in range(0,32)])

# better solution
class Solution:
    def NumberOf1(self, n):
        # write code here
        count=0
        if n<0:
            n = n & 0xffffffff
        while n:
            n = n & (n-1)
            count += 1
        return count
