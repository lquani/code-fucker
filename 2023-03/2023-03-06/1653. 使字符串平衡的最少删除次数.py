# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/6 7:07 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 1653. 使字符串平衡的最少删除次数.py
"""
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n)]
        cnt = 0
        if s[0] == 'b':
            cnt = 1
        for i in range(1, n):
            if s[i] == 'b':
                dp[i] = dp[i-1]
                cnt += 1
            else:
                dp[i] = min(dp[i-1]+1,cnt)
        return dp[-1]

print(Solution().minimumDeletions('bbaaaaabb'))