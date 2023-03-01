# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/27 10:27 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 51. N 皇后.py
"""
import copy
from typing import List
class Solution:
    def check(self, pos, matrix):
        x, y = pos
        l = len(matrix)
        for i in range(l):
            if matrix[x][i] == 'Q':
                return False
            if matrix[i][y] == 'Q':
                return False
            if (0 <= x-i < l and 0 <= y-i < l and matrix[x-i][y-i] == 'Q') or (0 <= x+i < l and 0 <= y+i < l and matrix[x+i][y+i] == 'Q')\
                or (0 <= x-i < l and 0 <= y+i < l and matrix[x-i][y+i] == 'Q') or (0 <= x+i < l and 0 <= y-i < l and matrix[x+i][y-i] == 'Q'):
                return False
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        matrix = [['.' for i in range(n)] for i in range(n)]
        res = []
        def traceback(num, select, road):
            if len(road) == num:
                tmp = copy.deepcopy(select)
                t = [''.join(tmp[i]) for i in range(len(tmp))]
                if t not in res:
                    res.append(t)
                return
            for i in range(num):
                for j in range(num):
                    if self.check([i, j], select):
                        select[i][j] = 'Q'
                        road.append(1)
                        traceback(num, select, road)
                        road.pop()
                        select[i][j] = '.'

        traceback(n, matrix, [])
        return res



Solution().solveNQueens(4)