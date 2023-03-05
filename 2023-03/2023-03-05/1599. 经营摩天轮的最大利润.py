# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/5 2:14 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 1599. 经营摩天轮的最大利润.py
"""
from typing import List
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = -1
        count = 0
        tmp = 0
        index = 0
        for i, num in enumerate(customers):
            if tmp > 0:
                num += tmp
            if num <= 4:
                count += num * boardingCost - runningCost
                if count > res:
                    res = count
                    index = i
            else:
                count += 4 * boardingCost - runningCost
                if count > res:
                    res = count
                    index = i
                tmp = num - 4
        while tmp != 0:
            if tmp <= 4:
                count += tmp * boardingCost - runningCost
                if count > res:
                    res = count
                    index += 1
                tmp = 0
            else:
                count += 4 * boardingCost - runningCost
                if count > res:
                    res = count
                    index += 1
                tmp -= 4
        if res < 0:
            return -1
        return index + 1

print(Solution().minOperationsMaxProfit([3,4,0,5,1],1,92))
