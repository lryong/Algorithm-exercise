#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : replace_space.py
# Author            : lryong <15816537946@163.com>
# Date              : 12.04.2019
# Last Modified Date: 12.04.2019
# Last Modified By  : lryong <15816537946@163.com>
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

# my Solution: trick方法
class Solution:
    def replaceSpace(self, s):
        return s.replace(' ', '%20')

# better Solution
#方法二：这一题的关键是替换是从往后往前遍历还是从前往后遍历是不一样的，如果从前往后遍历的话，每一个空格都要移动这个空格后面所有的字符串一次，但是如果从后往前遍历的话，每一个字符串只需要移动一次。
class Solution:
    def replaceSpace(self, s):
        cnt = 0
        ret = []
        for i in s:
            if i == " ":
                cnt +=1
        for i in xrange(len(s)-1,-1,-1):
            print i
            if s[i] == " ":
                ret[i+cnt*2] = s[i]
            else:
                cnt -= 1
                ret[i+2*cnt] = '%'
                ret[i+2*cnt+1] = '2'
                ret[i+2*cnt+2] = '0'
        return s


print Solution().replaceSpace("we are young")
