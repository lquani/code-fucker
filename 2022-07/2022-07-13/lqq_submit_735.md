## 题目
https://leetcode.cn/problems/asteroid-collision/
## 思路
使用栈进行比较,各种if，有点丑
## code
```py
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        m = len(asteroids)
        stack = []
        for i in range(m):
            alive = True
            while stack and asteroids[i]<0:
                if stack[-1]>0:
                    if stack[-1]>abs(asteroids[i]):
                        alive=False
                        break 
                    elif stack[-1]==abs(asteroids[i]):
                        stack.pop()
                        alive=False
                        break
                    else:
                        stack.pop()
                else:
                    break
            if alive:
                stack.append(asteroids[i])
        return stack```
