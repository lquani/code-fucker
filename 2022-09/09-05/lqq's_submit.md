## 题目
https://leetcode.cn/problems/find-duplicate-subtrees/submissions/
## 思路
哈希表+序列化树
## code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        res = defaultdict(int)
        def helper(root):
            if not root:
                return "#"
            cur_root = str(root.val) + '|' + helper(root.left) +'|' + helper(root.right)
            if res[cur_root]==1:
                ans.append(root)
            res[cur_root] += 1
            return cur_root
            
        helper(root)
        return ans 
