# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/2 7:38 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 面试题 05.02. 二进制数转字符串.py
"""
class Solution:
    def printBin(self, num: float) -> str:
        res = '0.'
        for i in range(1, 31):
            if num - 1/(2**i) > 0:
                res += '1'
                num -= 1/(2**i)
            elif num - 1/(2**i) == 0:
                res += '1'
                return res
            else:
                res += '0'
        return 'ERROR'

print(Solution().printBin(0.1))

