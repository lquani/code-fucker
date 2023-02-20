# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/20 10:25 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 2347. 最好的扑克手牌.py
"""
from typing import List
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        flush = set(suits)
        t = set(ranks)
        a = 0
        for i in t:
            a = max(ranks.count(i), a)
        if len(flush) == 1:
            return 'Flush'
        elif a >=3:
            return 'Three of a Kind'
        elif a == 2:
            return 'Pair'
        else:
            return 'High Card'

print(Solution().bestHand([4,4,2,4,4],["d","a","a","b","c"]))