# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/27 12:08 上午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 300. 最长递增子序列.py
"""
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
