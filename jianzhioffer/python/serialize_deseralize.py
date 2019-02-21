# -*- coding:utf-8 -*-
# 请实现两个函数，分别用来序列化和反序列化二叉树

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    index = -1

    def Serialize(self, root):
        # write code here
        return self.recursionSerialize(root)

    def recursionSerialize(self, root):
        if root is None:
            return '$,'
        s = str(root.val)+','
        left = self.recursionSerialize(root.left)
        right = self.recursionSerialize(root.right)
        return s+left+right

    def Deserialize(self, s):
        # write code here
        self.index += 1
        l = s.split(',')
        root = None
        if l[self.index] != '$':
            root = TreeNode(int(s[self.index]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
