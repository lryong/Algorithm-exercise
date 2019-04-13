# -*- coding:utf-8 -*-
# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return  []
        stack = [pRoot]
        ret = []
        flag = 0
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
            flag+=1
            if flag%2:
                ret.append(res)
            else:
                ret.append(res[::-1])
        return ret

