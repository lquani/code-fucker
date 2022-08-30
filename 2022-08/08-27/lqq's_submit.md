## 题目
https://leetcode.cn/problems/maximum-width-of-binary-tree/
## 思路
层次遍历，比较最右和最左子节点的距离差
## code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 0)]
        ans = 1
        while stack:
            cur_stack = []
            for node, index in stack:
                # print(node,index)
                if node.left:
                    cur_stack.append((node.left, 2*index+1))
                if node.right:
                    cur_stack.append((node.right, 2*index+2))
            if len(cur_stack)>1:
                ans = max(ans, cur_stack[-1][1]-cur_stack[0][1]+1)
            stack = cur_stack
        return ans 
