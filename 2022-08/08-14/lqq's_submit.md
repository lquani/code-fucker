## 题目
https://leetcode.cn/problems/maximum-score-after-splitting-a-string/
## 思路
前缀和
## code
```py
class Solution:
    def maxScore(self, s: str) -> int:
        sumi = 0
        for ss in s:
            if ss=='1':
                sumi += 1
        ans = 0 
        zero = 0

        for i in range(len(s)-1):
            ss = s[i]
            if ss=='0':
                zero += 1
            else:
                sumi -= 1
            ans = max(ans, zero+sumi)
        return ans 
        ```
