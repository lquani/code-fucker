## 题目
https://leetcode.cn/problems/maximum-number-of-pairs-in-array/solution/shu-zu-neng-xing-cheng-duo-shao-shu-dui-jq01j/
## 思路
哈希表记录每个数字出现的次数，然后用取余的方式判断是否是数对
##
```py
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ans= [0,0]
        res = {}
        m = len(nums)
        for i in range(m):
            res[nums[i]] = res.get(nums[i],0)+1
        for key,value in res.items():
            if value%2:
                ans[0] += value//2
                ans[1] += value%2
            else:
                ans[0] += value//2
        return ans 
