## 题目
https://leetcode.cn/problems/Ygoe9J/solution/by-wo-yao-chu-qu-luan-shuo-rcvf/
## 思路
回溯，可以选重复，排序一下
## code
```py
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def comeback(nums,res,cur):
            if cur==target:
                ans.append(res)
                return 
            elif cur>target:
                return 
            m= len(nums)
            for i in range(m):
                if nums[i]>target:
                    return 
                comeback(nums[i:],res+[nums[i]],cur+nums[i])
        candidates.sort()
        comeback(candidates,[],0)
        return ans
```
