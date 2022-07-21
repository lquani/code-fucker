## 题目
https://leetcode.cn/problems/binary-tree-pruning/submissions/
## 思路
递归，当左右叶子节点0和根节点得时候返回None，当根节点为1的时候更新叶子节点，且返回根节点
## code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None 
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        root.left = left 
        root.right = right 
        if root.val==0 and not left and not right:
            return None
        return root 
```
