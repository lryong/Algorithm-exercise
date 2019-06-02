#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 17_reverse_list.py
# Author            : lryong <15816537946@163.com>
# Date              : 06.05.2019
# Last Modified Date: 06.05.2019
# Last Modified By  : lryong <15816537946@163.com>

# 输入一个链表，反转链表后，输出新链表的表头。

#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last

