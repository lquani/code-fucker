# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/8 12:18 上午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 剑指 Offer 47. 礼物的最大价值.py
"""
from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = grid[i-1][j-1]
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
        return dp[n][m]