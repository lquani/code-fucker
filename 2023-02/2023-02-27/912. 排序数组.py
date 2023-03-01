# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/27 7:55 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 912. 排序数组.py
"""
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = nums[0]
            left = [x for x in nums[1:] if x <= mid]
            right = [x for x in nums[1:] if x > mid]
            return quick_sort(left) + [mid] + quick_sort(right)
        return quick_sort(nums)

Solution().sortArray([1,1,4,2,3])
