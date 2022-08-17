## 题目
https://leetcode.cn/problems/deepest-leaves-sum/submissions/
## 思路
层次遍历
## code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        ans =0
        while stack:
            cur_stack = []
            ans = 0
            for root in stack:
                ans += root.val
                if root.left:
                    cur_stack.append(root.left)
                if root.right:
                    cur_stack.append(root.right)
            stack = cur_stack
        return ans 
