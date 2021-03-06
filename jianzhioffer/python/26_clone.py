#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 26_clone.py
# Author            : lryong <15816537946@163.com>
# Date              : 08.06.2019
# Last Modified Date: 08.06.2019
# Last Modified By  : lryong <15816537946@163.com>
# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


# wrong Solution
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        newNode = RandomListNode(pHead.label)
        newNode.random = pHead.random
        newNode.next = self.Clone(pHead.next)
        return newNode
