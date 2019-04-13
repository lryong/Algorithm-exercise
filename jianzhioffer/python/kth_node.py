#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : kth_node.py
# Author            : lryong <15816537946@163.com>
# Date              : 13.04.2019
# Last Modified Date: 13.04.2019
# Last Modified By  : lryong <15816537946@163.com>
# -*- coding:utf-8 -*-
# 给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.ret = []
        self.minTraversal(pRoot)
        return self.ret[k-1] if 0 < k <= len(self.ret) else None

    def minTraversal(self, pRoot):
        if not pRoot:
            return
        self.minTraversal(pRoot.left)
        self.ret.append(pRoot)
        self.minTraversal(pRoot.right)

