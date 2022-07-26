## 题目
https://leetcode.cn/problems/count-number-of-pairs-with-absolute-difference-k/submissions/
https://leetcode.cn/problems/single-element-in-a-sorted-array/
## 思路
题目1：使用哈希表记录数字出现的次数，每次遇到一新的数字时就进行+k和-k的操作看哈希表里有没有这个数  
题目2：因为是排序好的，所以可以用二分查找。如果全都是只出现了两次，那么偶数位和他+1的数必相等，如果不相等，那一定是前面出现了一个数字只出现了一次，所以二分查找就往左边移动。
位或操作有一个操作，奇数^1=奇数-1，偶数^1=偶数+1。可以使用nums[mid] == nums[mid^1]来判断二分查找往那边移动。
## code
第一题  
```py
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = {}
        ans = 0
        for num in nums:
            ans += res.get(num+k,0)+res.get(num-k,0)
            res[num] = res.get(num,0)+1
        return ans 
```
第二题
```py
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] == nums[mid^1]:
                left = mid+1
            else:
                right = mid
        return nums[left]
```
