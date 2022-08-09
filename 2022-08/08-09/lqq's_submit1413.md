## 题目
https://leetcode.cn/problems/minimum-value-to-get-positive-step-by-step-sum/
## 思路
逐步求和，记录最小的值，如果为负数则返回其绝对值+1，否则返回1
## 
```PY
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res = 0
        ans = float('inf')
        for i in range(len(nums)):
            res += nums[i]
            ans = min(ans, res)
        return 1 if ans>0 else -ans+1
```
