#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 23_print_from_top_to_bottom.py
# Author            : lryong <15816537946@163.com>
# Date              : 02.06.2019
# Last Modified Date: 02.06.2019
# Last Modified By  : lryong <15816537946@163.com>


# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
# 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        res = []
        if not root:
            return
        else
            tmp = [root]
        while tmp:
            node = tmp.pop[0]
            res.append(node.val)
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
        return res
