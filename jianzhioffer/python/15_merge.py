#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 15_merge.py
# Author            : lryong <15816537946@163.com>
# Date              : 13.04.2019
# Last Modified Date: 06.05.2019
# Last Modified By  : lryong <15816537946@163.com>

# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        tmpHead = None
        if pHead1.val < pHead2.val:
            tmpHead = pHead1
            tmpHead.next = self.Merge(pHead1.next,pHead2)
            # return pHead1.next
        #if pHead2.val < pHead1.val:
        else:
            tmpHead = pHead2
            tmpHead.next = self.Merge(pHead1,pHead2.next)
            # return pHead2.next
        return tmpHead
