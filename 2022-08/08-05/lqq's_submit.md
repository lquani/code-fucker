## 题目
https://leetcode.cn/problems/add-one-row-to-tree/solution/zai-er-cha-shu-zhong-zeng-jia-yi-xing-by-xcaf/
## 思路
简单的递归
## code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def helper(root, val, depth, way):
            # if not root:
            #     return root 
            if depth==1:
                node = TreeNode(val)
                if way=='left':
                    node.left = root
                else:
                    node.right = root
                return node 
            if not root:
                return root
            root.left = helper(root.left,val,depth-1,'left')
            root.right = helper(root.right,val,depth-1, 'right')
            return root
        return helper(root,val,depth,'left')
```
