## 题目
https://leetcode.cn/problems/jC7MId/
## 思路
树的做法直接想递归，输入什么值，返回什么值
## code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = float("-inf")
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            maxi = max(root.val,root.val+left,root.val+right)
            self.ans = max(self.ans, root.val+left+right,maxi)
            return maxi 
        helper(root)
        return self.ans
        ```
