# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/9 12:56 上午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 2379. 得到 K 个黑块的最少涂色次数.py
"""
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b, w = blocks[0:k].count('B'), blocks[0:k].count('W')
        res = min(len(blocks), w)
        for i in range(1, len(blocks)-k+1):
            if blocks[i-1] == 'B':
                b -= 1
            elif blocks[i-1] == 'W':
                w -= 1
            if blocks[i+k-1] == 'B':
                b += 1
            elif blocks[i+k-1] == 'W':
                w += 1
            res = min(res, w)
        return res

print(Solution().minimumRecolors('WBBWWBBWBW', 7))