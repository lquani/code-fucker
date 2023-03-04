# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/4 11:13 上午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 982. 按位与为零的三元组.py
"""
from typing import List
from collections import Counter
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        memo = Counter()
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(n):
                memo[nums[i]&nums[j]] += 1
        for k in range(n):
            for tmp in memo.keys():
                if tmp&nums[k] == 0:
                    res += memo[tmp]

        return res

print(Solution().countTriplets([2,1,3]))

