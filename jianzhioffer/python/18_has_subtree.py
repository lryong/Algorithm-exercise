#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 18_has_subtree.py
# Author            : lryong <15816537946@163.com>
# Date              : 06.05.2019
# Last Modified Date: 01.06.2019
# Last Modified By  : lryong <15816537946@163.com>


# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left,B.left) and self.is_subtree(A.right, B.right)