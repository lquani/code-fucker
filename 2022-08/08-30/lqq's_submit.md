## 题目
https://leetcode.cn/problems/maximum-binary-tree-ii/submissions/
## 思路
树的遍历
## code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        parent, cur = None, root
        while cur:
            if val > cur.val:
                if not parent:
                    return TreeNode(val, root, None)
                node = TreeNode(val, cur, None)
                parent.right = node
                return root
            else:
                parent = cur
                cur = cur.right
        
        parent.right = TreeNode(val)
        return root
