# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/1 7:11 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 2373. 矩阵中的局部最大值.py
"""
import numpy as np
from typing import List
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        grid = np.array(grid)
        res = []
        for i in range(n-2):
            tmp = []
            for j in range(n-2):
                tmp.append(np.max(grid[j:j+3,i:i+3]))
            res.append(tmp)
        res = np.array(res)
        res = res.T
        return res.tolist()

Solution().largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])