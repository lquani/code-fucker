## 题目
https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/
## 思路
单调栈
## code
```py
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for num in arr:
            if not stack or stack[-1]<=num:
                stack.append(num)
            else:
                mx = stack.pop()
                while stack and stack[-1]>num:
                    stack.pop()
                stack.append(mx)
            print(stack)
        return len(stack)
```
