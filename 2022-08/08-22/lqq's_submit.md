## 题目
https://leetcode.cn/problems/print-binary-tree/submissions/
## 思路
先算树得高度，然后构建矩阵，遍历树将值放到对应得位置
## code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def helper(root):
            if not root:
                return 0 
            return 1 + max(helper(root.left), helper(root.right))
        height = helper(root)-1
        m = height+1
        n = 2**(height+1)-1
        ans = [["" for i in range(n)] for i in range(m) ]
        def Trreee(root,r,c):
            if not root:
                return 
            ans[r][c] = str(root.val)
            Trreee(root.left,r+1,c-2**(height-r-1))
            Trreee(root.right,r+1,c+2**(height-r-1))
        Trreee(root,0,(n-1)//2)
        return ans 
