#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 09_jump_floor2.py
# Author            : lryong <15816537946@163.com>
# Date              : 13.04.2019
# Last Modified Date: 13.04.2019
# Last Modified By  : lryong <15816537946@163.com>
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution:
    def jumpFloorII(self, number):
        if number <= 0:
            return -1
        else:
            #return (number - 1) << 1
            return pow(2, number-1)

