## 题目
https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
## 思路
滑动窗口，用了一个栈
## code
```py
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        res = 0
        stack = []
        m = len(s)
        for i in range(m):
            
            if len(stack)>=k:
                cur = stack.pop(0)
                res -= cur in ('a','e','i','o','u')
            stack.append(s[i])
            res += s[i] in ('a','e','i','o','u')
            ans = max(ans, res)
        return ans
```
