# -*- coding:utf-8 -*-
# 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def compare(self, left, right):
        if left is None:
            return right is None
        if right is None:
            return False
        if left.val != right.val:
            return False
        return self.compare(right.left, left.right) and self.compare(left.left, right.right)

    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.compare(pRoot.left, pRoot.right)

