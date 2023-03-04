# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/3 7:24 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 1487. 保证文件名唯一.py
"""
from typing import List
from collections import Counter
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        count = Counter()
        res = []
        for name in names:
            if name not in count.keys():
                res.append(name)
                count[name] = 1
            else:
                k = count[name]
                while name + '(' + str(k) + ')' in count:
                    k+=1
                res.append(name+'('+str(k)+')')
                count[name] = k+1
                count[name+'('+str(k)+')'] = 1
                # count[name] += 1
                # res.append(name+'('+str(count[name])+')')
                # count[name + '(' + str(count[name]) + ')'] = 1
        print(res)
        return res


a = ["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]
Solution().getFolderNames(a)