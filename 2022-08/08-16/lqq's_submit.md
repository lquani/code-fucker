## 题目
https://leetcode.cn/problems/design-an-ordered-stream/submissions/
## 思路
用列表就能实现
## code
```py
class OrderedStream:

    def __init__(self, n: int):
        self.list = ['' for i in range(n+1)]
        self.cur = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey] = value 
        ans = []
        m = len(self.list)
        while self.cur<m and self.list[self.cur]!='':
            ans.append(self.list[self.cur])
            self.cur+=1
        return ans 


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
