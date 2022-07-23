## 题目
https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/
## 思路
注意中序和前序遍历中根节点的位置就行了
## code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        p = preorder[0]
        root = TreeNode(p)
        index = inorder.index(p)
        root.left = self.buildTree(preorder[1:index+1],inorder[:index])
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        return root
```
