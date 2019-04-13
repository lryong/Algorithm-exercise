#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : convert_tree_node.py
# Author            : lryong <15816537946@163.com>
# Date              : 11.04.2019
# Last Modified Date: 11.04.2019
# Last Modified By  : lryong <15816537946@163.com>
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
		if not pRootOfTree:
			return pRootOfTree
		if not pRootOfTree.left and not pRootOfTree.right:
			return pRootOfTree
		# 处理左树
		self.Convert(pRootOfTree.left)
		left = pRootOfTree.left

		# 连接根与左树最大节点
		if left:
			while(left.right):
				left = left.right
			pRootOfTree.left,left.right = left,pRootOfTree

		# 处理右子树
		self.Convert(pRootOfTree.right)
		right = pRootOfTree.right

		#连接根与右树最小节点
		if right:
			while(right.left):
				right = right.left
			pRootOfTree.right,right.left = right,pRootOfTree

		while(pRootOfTree.left):
			pRootOfTree = pRootOfTree.left
		return pRootOfTree

