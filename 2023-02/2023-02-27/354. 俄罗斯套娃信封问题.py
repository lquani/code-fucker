# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/27 12:25 上午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 354. 俄罗斯套娃信封问题.py
"""
from typing import List
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: x[0])
        l = [x[1] for x in envelopes]
        dp = [1] * len(l)
        print(l)
        for i in range(len(l)):
            for j in range(i):
                if l[i] > l[j] and envelopes[i][0] > envelopes[j][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(max(dp))
        print(dp)
        return max(dp)

Solution().maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]])

