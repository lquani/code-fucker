# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/7 11:21 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 1096. 花括号展开 II.py
"""
from typing import List
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        res = set()
        def dfs(exp):
            s = exp.find('}')
            if s==-1:
                res.add(exp)
                return
            tmp = exp.rfind('{',0,s-1)
            a, c = exp[:tmp], exp[s+1:]
            for b in exp[tmp+1:s].split(','):
                dfs(a+b+c)
        dfs(expression)
        return sorted(res)

print(Solution().braceExpansionII("{a,b}{c,{d,e}}"))
