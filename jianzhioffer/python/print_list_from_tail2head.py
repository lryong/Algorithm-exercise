#!/usr/bin/env python
# -*- coding:utf-8 -*-

#输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

# My Solution
class Solution:
    def printListFromTailToHead(self, listNode):
        array = []
        while listNode:
            array.insert(0, listNode.val)
            listNode = listNode.next
        return array
        
        
