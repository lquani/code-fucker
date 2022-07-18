## 题目
https://leetcode.cn/problems/YesdPw/submissions/
## 思路
先把和走廊联通的房间找出来，然后再统计没有联通房间的面积，比较大小，思路简单，但是写起来比较复杂
## code
```py
class Solution:
    def __init__(self):
        self.ans = 0
        self.res = 0
    def largestArea(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        flag = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' and flag[i][j]==0:
                    flag[i][j]=1
                    for k,l in [(1,0),(-1,0),(0,1),(0,-1)]:
                        self.res = 0
                        if 0<=i+k<m and 0<=j+l<n:
                            self.find_s(grid,flag,i+k,j+l,grid[i+k][j+l]) 
        print(flag)
        for i in range(m):
            if flag[i][0]==0:
                self.find_s(grid,flag,i,0,grid[i][0])
            if flag[i][n-1]==0:
                self.find_s(grid,flag,i,n-1,grid[i][n-1])
        for j in range(n):
            if flag[0][j]==0:
                self.find_s(grid,flag,0,j,grid[0][j])
            if flag[m-1][j]==0:
                self.find_s(grid,flag,m-1,j,grid[m-1][j])
        print(flag)
        for i in range(m):
            for j in range(n):
                if flag[i][j]==0:
                    self.res = 0
                    self.find_s(grid,flag,i,j,grid[i][j]) 
                    self.ans = max(self.ans,self.res)
        return self.ans

    def find_s(self,grid,flag,i,j,s):
        if flag[i][j]==1:
            return 
        if grid[i][j]!=s or grid[i][j]=='0':
            return 
        self.res += 1
        flag[i][j] = 1
        for k,l in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0<=i+k<len(grid) and 0<=j+l<len(grid[0]):
                self.find_s(grid,flag,i+k,j+l,s) 
        return 
```
