## 题目
https://leetcode.cn/problems/maximize-the-topmost-element-after-k-moves/
## 思路
直接模拟
## code
```py
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        m = len(nums)
        if m==1 and k!=0 and k%2==1:
            return -1
        if m<k:
            return max(nums)
        elif m==k:
            return max(nums[:m-1])
        else:
            if k<=1 and m>=1:
                return nums[k]
            maxi = max(nums[:k-1])
            num = nums[k]
        return max(maxi,num)```
