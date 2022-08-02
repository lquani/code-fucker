## 题目
https://leetcode.cn/problems/volume-of-histogram-lcci/
## 思路
思路一：维护左右两个列表，分别记录从左到右最大储水量，然后再遍历两个列表累加对应位置的最小值
## code
```py
class Solution:
    def trap(self, height: List[int]) -> int:
        m = len(height)
        if m <3:
            return 0
        left = [0 for i in range(m)]
        right = [0 for i in range(m)]
        l = height[0]
        r = height[-1]
        for i in range(m):
            left[i] = max(l-height[i],0)
            right[m-i-1] = max(r-height[m-i-1],0)
            l = max(l,height[i])
            r = max(r,height[m-i-1])
        ans = 0
        print(left,right)
        for i in range(m):
            ans += min(left[i],right[i])
        return ans 
```
