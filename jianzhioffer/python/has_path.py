# -*- coding:utf-8 -*-
# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。


def BFS(matrix, row, col, path, visited):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or visited[row][col]:
        return False
    if path[0] == matrix[row][col]:
        if len(path) == 1:
            return True
        visited[row][col] = 1
        if BFS(matrix, row+1, col, path[1:], visited) or \
            BFS(matrix, row-1, col, path[1:], visited) or \
            BFS(matrix, row, col-1, path[1:], visited) or \
            BFS(matrix, row, col+1, path[1:], visited):
                return True
        return False
    else:
        return False


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        array = list(matrix)
        array = [array[i*cols:(i+1)*cols] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                visited = [[0] * len(array[0]) for _ in range(len(array))]
                if BFS(array, i, j, list(path), visited):
                    return True
        return False

