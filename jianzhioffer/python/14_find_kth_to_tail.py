#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 14_find_kth_to_tail.py
# Author            : lryong <15816537946@163.com>
# Date              : 13.04.2019
# Last Modified Date: 13.04.2019
# Last Modified By  : lryong <15816537946@163.com>

# 输入一个链表，输出该链表中倒数第k个结点。

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# my solution
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        L = []
        while head !=None:
            L.append(head)
            head = head.next
        if k >len(L) or k < 1:
            return
        return L[-k]

# 两个指针，先让第一个指针和第二个指针都指向头结点，然后再让第一个指正走(k-1)步，到达第k个节点。然后两个指针同时往后移动，当第一个结点到达末尾的时候，第二个结点所在位置就是倒数第k个节点了
