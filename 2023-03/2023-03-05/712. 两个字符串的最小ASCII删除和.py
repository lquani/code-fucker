# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/5 1:58 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 712. 两个字符串的最小ASCII删除和.py
"""
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        cnt1 = sum([ord(i) for i in list(s1)])
        cnt2 = sum([ord(i) for i in list(s2)])
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = max(dp[i - 1][j - 1]+ord(s1[i-1]), dp[i-1][j],dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
        return cnt1+cnt2-2*dp[n][m]

print(Solution().minimumDeleteSum('delete', 'leet'))

