# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/19 8:41 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 1792. 最大平均通过率.py
"""

from typing import List
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        res = 0
        print(classes)
        for index in range(extraStudents):
            extra_score = []
            for i, (a, b) in enumerate(classes):
                extra_score.append((b-a)/(b*b+1))
            idx = extra_score.index(max(extra_score))
            classes[idx][0] += 1
            classes[idx][1] += 1
            print(classes)
            print(extra_score)
        for index in range(len(classes)):
            res += classes[index][0]/classes[index][1]
        print(res/len(classes))
        print(len(classes))
        return res/len(classes)


Solution().maxAverageRatio([[1,2],[3,5],[2,2]], 2)
