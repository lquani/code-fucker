## 题目
https://leetcode.cn/problems/implement-magic-dictionary/
## 思路
主要思路使用字典树和递归得方法
## code
```py
class TreeNode():
    def __init__(self):
        self.child = {}
        self.is_end = False

class MagicDictionary:

    def __init__(self):
        self.root = TreeNode()


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for s in word:
                if s not in node.child:
                    node.child[s] = TreeNode()
                node = node.child[s]
            node.is_end = True

    def search(self, searchWord: str) -> bool:
        def dfs(node,cur,count):
            if cur==len(searchWord):
                return node.is_end and count==0 # 这里必须要有且只有一个字符不同
            if searchWord[cur] in node.child:
                if dfs(node.child[searchWord[cur]],cur+1,count):
                    return True
            if count==1:
                for ch in node.child:
                    if ch != searchWord[cur]:
                        if dfs(node.child[ch],cur+1,count-1):
                            return True
            return False
        node = self.root
        return dfs(node,0,1)
```
