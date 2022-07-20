## 题目
https://leetcode.cn/problems/shift-2d-grid/
## 思路
数学题，每次算一下经过k次移动后回到哪里
## code
```py
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                cur_i = (i+(j+k) // n) %m
                cur_j = (j+k) % n
                ans[cur_i][cur_j] = grid[i][j]
        return ans 
 ```
