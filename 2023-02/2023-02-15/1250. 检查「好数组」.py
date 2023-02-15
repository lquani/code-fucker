# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/15 7:23 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 1250. 检查「好数组」.py
"""
from typing import List
from math import gcd
from functools import reduce
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(gcd, nums) == 1
