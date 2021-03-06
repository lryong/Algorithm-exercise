# -*- coding:utf-8 -*-
# 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。


class Solution:
    def maxInWindows(self, num, size):
        if not size:
            return []
        queue, ret, i = [], [], 0
        while i < len(num):
            # 判断最大值的位置queue[0]过期
            if queue and i-size+1 > queue[0]:
                queue.pop(0)
            while len(queue) > 0 and num[queue[-1]] < num[i]:
                queue.pop()
            queue.append(i)
            if i >= size-1:
                ret.append(num[queue[0]])
            i = i+1
        return ret
