# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/2 8:54 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 72. 编辑距离.py
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1==word2:
            return 0
        elif word1 == '':
            return len(word2)
        elif word2 == '':
            return len(word1)
        n = len(word1)
        m = len(word2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==j==0:
                    dp[i][j] = -int((word1[0]==word2[0]))+1
                elif word1[j] == word2[i]:
                    dp[i][j] = dp[i-1][j-1]
                elif word1[j] != word2[i]:
                    dp[i][j] = min(dp[i-1][j] if i-1>=0 else float('inf'), dp[i][j-1] if j-1>=0 else float('inf'),
                                   dp[i-1][j-1] if i>=1 and j>=1 else float('inf')) + 1
        print(dp)
        return dp[m-1][n-1]

print(Solution().minDistance('zoologicoarchaeologist','zoogeologist'))