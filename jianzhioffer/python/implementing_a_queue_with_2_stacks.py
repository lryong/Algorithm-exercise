#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

# My Solution:
class Solution:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
    def push(self, node):
        self.push_stack.append(node)
    def pop(self):
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack.pop()
        return self.pop_stack.pop()

    
# Better Solution
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()
