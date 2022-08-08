## 题目
https://leetcode.cn/problems/smallest-number-in-infinite-set/
## 思路
栈
## code
```py
class SmallestInfiniteSet:

    def __init__(self):
        self.left = 1
        self.right = 1000
        self.stack = []

    def popSmallest(self) -> int:
        if not self.stack:
            self.left += 1
            return self.left - 1
        ans = self.stack.pop(0)
        while self.stack and self.stack[0]==ans:
            self.stack.pop(0)
        return ans 


    def addBack(self, num: int) -> None:
        if num<self.left or num >self.right:
            self.stack.append(num)
            cur = len(self.stack)-1
            while cur-1>=0 and self.stack[cur-1]>self.stack[cur]:
                self.stack[cur-1],self.stack[cur] = self.stack[cur],self.stack[cur-1]
                cur -= 1
```
