# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/14 6:42 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 1124. 表现良好的最长时间段.py
"""
class Solution:
    def longestWPI(self, hours) -> int:
        h = [1 if hour > 8 else -1 for hour in hours]
        tmp = [0]*len(hours)
        for i, s in enumerate(h):
            if i == 0:
                tmp[i] = s
            else:
                tmp[i] = tmp[i-1] + s
        print(tmp)
        return 0

Solution().longestWPI([1,4,6,9,9,9])
