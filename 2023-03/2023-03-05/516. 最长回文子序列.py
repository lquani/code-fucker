# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/5 4:37 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 516. 最长回文子序列.py
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(1, n):
            for j in reversed(range(i)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i-1][j+1] + 2
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j+1])
        return dp[n-1][0]

print(Solution().longestPalindromeSubseq('babbbbaabbababbaaaaababbaaabbbbaaabbbababbbbabaabababaabaaabbbabababbbabababaababaaaaabbabaaaabaaaab'))
