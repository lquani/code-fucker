## 题目
https://leetcode.cn/problems/WhsWhI/
## 思路
用集合去重，集合取数复杂度O(1)，python的集合原理就是哈希
## code
```py
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        res = set(nums)
        for i in range(len(nums)):
            num = nums[i]
            if num-1 in res:
                continue 
            temp = 1
            while num+1 in res:
                temp += 1
                num += 1
            ans = max(ans,temp)
        return ans 
```
