#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 21_define_min_stack.py
# Author            : lryong <15816537946@163.com>
# Date              : 02.06.2019
# Last Modified Date: 08.06.2019
# Last Modified By  : lryong <15816537946@163.com>

# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

class Solution:
    stack = []
    stack_min = []
    def push(self, node):
        # write code here
	self.stack.append(node)
	if not self.stack_min:
		self.stack_min.append(node)
	if self.stack_min and node < self.stack_min[-1]:
		self.stack_min.append(node)

    def pop(self):
        # write code here
	if self.stack[-1] == self.stack_min[-1]:
		self.stack_min.pop() # stack_min作为辅助栈，需要压出最后一个元素
	self.stack.pop()
    def top(self):
        # write code here
	return self.stack[-1]
    def min(self):
        # write code here
	return self.stack_min[-1]
