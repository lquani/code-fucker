## 题目
https://leetcode.cn/problems/maximum-binary-tree/submissions/
## 思路
二叉树，直接递归可以解决
## code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None 
        maxi = max(nums)
        index = nums.index(maxi)
        root = TreeNode(maxi)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root
