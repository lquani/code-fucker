## 题目
https://leetcode.cn/problems/make-two-arrays-equal-by-reversing-sub-arrays/submissions/
## 思路
今天是送分题没什么好讲的
## code
```py
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        return target==arr
