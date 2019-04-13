#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 07_fibonacci.py
# Author            : lryong <15816537946@163.com>
# Date              : 13.04.2019
# Last Modified Date: 13.04.2019
# Last Modified By  : lryong <15816537946@163.com>
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39

# My Solution 1
class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n < 3:
            return 1
        else:
            return self.Fibonacci(n-2) + self.Fibonacci(n-1)

# Better Solution, 动态规划
class Solution:
    def Fibonacci(self, n):
        a, b = 0, 1
        while n > 0:
            a, b = b, a+b
            n -= 1
        return a

class Solution:
    def Fibonacci(self, n):
        # write code here
        x, y = 0, 1
        while n > 0:
            x,y=y,x+y
            n-=1
        return x

