# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/27 9:46 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 46. 全排列.py
"""
import copy
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def trace(road, select):
            if len(road) == len(select):
                result.append(road[:])
                return
            else:
                for i, num in enumerate(select):
                    if num not in road:
                        road.append(num)
                        trace(road, select)
                        road.pop()
        trace([], nums)
        print(result)
        return result

Solution().permute([1,2,3])
