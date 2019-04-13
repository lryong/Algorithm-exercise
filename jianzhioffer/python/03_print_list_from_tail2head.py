#!/usr/bin/env python
# -*- coding:utf-8 -*-

#输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# My Solution
class Solution:
    def printListFromTailToHead(self, listNode):
        array = []
        while listNode:
            array.insert(0, listNode.val)
            listNode = listNode.next
        return array


'''
java 递归超简洁版本
public class Solution {
    ArrayList<Integer> arrayList=new ArrayList<Integer>();
    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        if(listNode!=null){
            this.printListFromTailToHead(listNode.next);
            arrayList.add(listNode.val);
        }
        return arrayList;
    }
}
'''

print Solution.printListFromTailToHead()
