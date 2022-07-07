## 题目
https://leetcode.cn/problems/replace-words/submissions/
## 思路
一看到这道题就想起我以前在博客上写的一个分享，介绍字典树的，这里粘贴过来https://blog.csdn.net/m0_37820194/article/details/105247560  
两年了才140的阅读量！giao！
直接用字典树解决。
## code
```py
class TreeNode():
    def __init__(self):
        self.child = {}  
        self.is_end = False

class Trie():
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        node = self.root
        for s in word:
            if s not in node.child:
                node.child[s] = TreeNode()
            node = node.child[s]
        node.is_end = True

    def search(self, word):
        node = self.root
        ans = ''
        for s in word:
            if s not in node.child:
                return False,''
            ans += s
            # print(s,node.is_end)
            node = node.child[s]
            if node.is_end:
                return True,ans
        return node.is_end,ans


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tree = Trie()
        for word in dictionary:
            tree.insert(word)
        res = sentence.split()
        ans = []
        for word in res:
            is_root,root = tree.search(word)
            if is_root:
                ans.append(root)
            else:
                ans.append(word)
        return ' '.join(ans)
```
