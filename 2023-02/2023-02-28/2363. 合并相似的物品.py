# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/28 9:12 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 2363. 合并相似的物品.py
"""
from typing import List
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res = []
        item = items1 + items2
        item.sort()
        i = 0
        w0 = item[0][0]
        v0 = item[0][1]
        while i<len(item)-1:
            i += 1
            w = item[i][0]
            v = item[i][1]
            if w==w0:
                v0+=v
            else:
                res.append([w0,v0])
                w0 = item[i][0]
                v0 = item[i][1]
        res.append([w0,v0])
        return res

Solution().mergeSimilarItems([[1,1],[4,5],[3,8]],[[3,1],[1,5]])