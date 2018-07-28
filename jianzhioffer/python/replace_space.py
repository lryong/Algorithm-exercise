#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

# my Solution
class Solution:
    def replaceSpace(self, s):
        return s.replace(' ', '%20')

# better Solution
#方法二：这一题的关键是替换是从往后往前遍历还是从前往后遍历是不一样的，如果从前往后遍历的话，每一个空格都要移动这个空格后面所有的字符串一次，但是如果从后往前遍历的话，每一个字符串只需要移动一次。
        
