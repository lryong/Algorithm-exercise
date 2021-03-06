#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : print_tree_node.py
# Author            : lryong <15816537946@163.com>
# Date              : 04.05.2019
# Last Modified Date: 04.05.2019
# Last Modified By  : lryong <15816537946@163.com>
# -*- coding:utf-8 -*-

# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        ret = []
        stack = [pRoot]
        while stack:
            res = []
            nextStack = []
            for i in stack:
                res.append(i.val)
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
            stack = nextStack
            ret.append(res)
        return ret


