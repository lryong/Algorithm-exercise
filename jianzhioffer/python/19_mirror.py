#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 19_mirror.py
# Author            : lryong <15816537946@163.com>
# Date              : 01.06.2019
# Last Modified Date: 01.06.2019
# Last Modified By  : lryong <15816537946@163.com>

'''
操作给定的二叉树，将其变换为源二叉树的镜像。
输入描述:
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
        # 返回镜像树的根节点
        def Mirror(self, root):
        # write code here
		if root != None:
			root.left, root.right = root.right, root.left
			self.Mirror(root.left)
			self.Mirror(root.right)
