# -*- coding:utf-8 -*-
# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？


def getN(i, j):
    res = 0
    while i:
        res += (i % 10)
        i //= 10
    while j:
        res += (j % 10)
        j //= 10

    return res


def DFS(array, i, j, threshold, visited):
    if i<0 or j<0 or i>=len(array) or j>=len(array) or array[i][j]>threshold or visited[i][j]:
        return 0
    res = 1
    visited[i][j] = 1
    res += DFS(array, i+1, j, threshold, visited)
    res += DFS(array, i-1, j, threshold, visited)
    res += DFS(array, i, j+1, threshold, visited)
    res += DFS(array, i, j-1, threshold, visited)
    return res


class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        array = []
        for i in xrange(rows):
            res = []
            for j in xrange(cols):
                res.append(getN(i,j))
            array.append(res)
        visited = [[0]*rows for _ in xrange(cols)]
        return DFS(array, 0, 0,threshold, visited)
