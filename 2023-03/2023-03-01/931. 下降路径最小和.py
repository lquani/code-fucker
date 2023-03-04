# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/1 7:39 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 931. 下降路径最小和.py
"""
from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(1, n):
            for j in range(n):
                dp[i][j] = matrix[i][j] + min(dp[i-1][j-1] if j-1>=0 else float('inf'), dp[i-1][j], dp[i-1][j+1] if j+1<=n-1 else float('inf'))
        res = float('inf')
        for i in range(n):
            res = min(res, dp[-1][i])
        return res
Solution().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])


