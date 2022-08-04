## 题目
https://leetcode.cn/problems/minimum-subsequence-in-non-increasing-order/
## 思路
降序后从做累加，当大于sum//2的时候返回
## code
```py
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        sumi = sum(nums)
        nums.sort(reverse=True)
        ans = []
        res = 0
        for num in nums:
            ans.append(num)
            res += num 
            if res > sumi//2:
                return ans 
        return ans 
        ```
