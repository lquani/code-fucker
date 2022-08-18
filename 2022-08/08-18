## 题目
https://leetcode.cn/problems/maximum-equal-frequency/submissions/
## 思路
哈希表
三种情况满足条件
1、全都只出现一次
2、全部数都出现了n次，有一个数出现了一次
3、全部数字都出现了n次，有一个数字出现了n+1次
## code
```py
from collections import defaultdict
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        res1 = defaultdict(int)
        res2 = defaultdict(int)
        maxi=0
        ans=0
        for i, num in enumerate(nums):
            if res1[num]:
                res2[res1[num]] -= 1
            res1[num] += 1
            res2[res1[num]] += 1
            # if maxi<res1[num]
            maxi = max(maxi,res1[num])
            if maxi==1 or res2[maxi]*maxi==i or (res2[maxi-1]+1)*(maxi-1)==i:
                ans = i + 1
        return ans 
  ```
