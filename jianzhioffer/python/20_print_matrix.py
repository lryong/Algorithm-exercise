#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 20_print_matrix.py
# Author            : lryong <15816537946@163.com>
# Date              : 01.06.2019
# Last Modified Date: 02.06.2019
# Last Modified By  : lryong <15816537946@163.com>

# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res=[]
        n=len(matrix)
        m=len(matrix[0])
        if n==1 and m==1:
            res=[matrix[0][0]]
            return res
        for o in xrange((min(m,n)+1)//2):
            [res.append(matrix[o][i]) for i in xrange(o,m-o)]
            [res.append(matrix[j][m-1-o]) for j in xrange(o,n-o) if matrix[j][m-1-o] not in res]
            [res.append(matrix[n-1-o][k]) for k in xrange(m-1-o,o-1,-1) if matrix[n-1-o][k] not in res]
            [res.append(matrix[l][o]) for l in xrange(n-1-o,o-1,-1) if matrix[l][o] not in res]
        return res

''' better solution
class Solution:
    def printMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix[0]
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix nad matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
'''
