## 题目
https://leetcode.cn/problems/maximum-ascending-subarray-sum/submissions/
## 思路
这个比较简单，就是连续最长字串，动态规划
## code
```py
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        m = len(nums)
        sumi = nums[0]
        res = 0
        for i in range(0,m-1):
            if nums[i+1]>nums[i]:
                sumi += nums[i+1]
            else:
                res = max(res,sumi)
                sumi = nums[i+1]
        res = max(res,sumi)
        return res
```
