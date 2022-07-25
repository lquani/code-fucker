## 题目
https://leetcode.cn/problems/complete-binary-tree-inserter/solution/wan-quan-er-cha-shu-cha-ru-qi-by-leetcod-lf8t/
## 思路
使用栈,初始化时先将树里的叶子节点存入栈中，插入的时候先看栈里第一个节点的左右子节点都为空，若只有右节点为空，则插入子节点，并将该节点在栈中弹出
## code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.stack1 = []
        if root:
            node = self.root
            self.stack2 = [node]
            while self.stack2:
                cur = self.stack2.pop(0)
                left = cur.left 
                right = cur.right 
                if left:
                    self.stack2.append(left)
                if right:
                    self.stack2.append(right)
                if not left or not right:
                    self.stack1.append(cur)

    def insert(self, val: int) -> int:
        if not self.stack1:
            return 0 
        cur = TreeNode(val)
        ans = self.stack1[0].val 
        if not self.stack1[0].left:
            self.stack1[0].left = cur
        else:
            node = self.stack1.pop(0)
            node.right = cur 
        self.stack1.append(cur)
        return ans

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
```
