#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : find_path.py
# Author            : lryong <15816537946@163.com>
# Date              : 12.04.2019
# Last Modified Date: 01.06.2019
# Last Modified By  : lryong <15816537946@163.com>
# -*- coding:utf-8 -*-
'''
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的)
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        # 返回二维列表，内部每个列表表示找到的路径
            def FindPath(self, root, expectNumber):
                        # write code here
                        if not root:
                            return []
                        if root and not root.left and not root.right and root.val == expectNumber:
                            return [[root.val]]

                        res = []
                        left = self.FindPath(root.left,expectNumber-root.val)
                        right = self.FindPath(root.right,expectNumber-root.val)

                        for i in left + right:
                            res.append([root.val]+i)
                        return res
