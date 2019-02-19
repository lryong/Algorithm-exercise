# -*- coding:utf-8 -*-
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        if pHead.val == pHead.next.val:
            # pHead.next = pHead.next.next
            pNode = pHead.next
            while pNode is not None and pNode.val == pHead.val:
                pNode = pNode.next
            return self.deleteDuplication(pNode)
        else:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead






