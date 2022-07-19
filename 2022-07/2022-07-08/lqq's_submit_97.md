## 题目
https://leetcode.cn/problems/interleaving-string/
## 思路
递归，使用备忘录记着出现过的组合
## code
```py
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        res = {}
        def func(i1,i2,i3):
            if (i1,i2,i3) in res:
                return res[(i1,i2,i3)]
            if i1==len(s1) and i2==len(s2):
                return True
            if i1<len(s1) and s1[i1]==s3[i3] and func(i1+1,i2,i3+1):
                return True
            if i2<len(s2) and s2[i2]==s3[i3] and func(i1,i2+1,i3+1):
                return True
            res[(i1,i2,i3)]=False
            return False
        return func(0,0,0)```
