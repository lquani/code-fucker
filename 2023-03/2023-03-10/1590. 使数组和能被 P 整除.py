# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/10 12:03 上午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 1590. 使数组和能被 P 整除.py
"""
from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        n = len(nums)
        res = len(nums)
        if total%p==0:
            return 0
        if total<p:
            return -1
        for i in range(n):
            tmp = 0
            cnt = 0
            for j in range(i,n):
                tmp += nums[j]
                cnt += 1
                if (total-tmp)%p==0:
                    res = min(res, cnt)
        if res == n:
            return -1
        return res

print(Solution().minSubarray([3,1,4,2],6))