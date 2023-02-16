# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/16 9:31 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 2341. 数组能形成多少数对.py
"""
from typing import List
from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        i = 0
        j = 0
        for k in count.keys():
            i += count[k]//2
            j += count[k]%2
        return [i,j]
