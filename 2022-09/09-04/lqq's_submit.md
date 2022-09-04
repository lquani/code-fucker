## 题目
https://leetcode.cn/problems/special-positions-in-a-binary-matrix/
## 思路
记录一下每行每列1出现的次数
## code
```py
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        cols = [0 for i in range(n)]
        rows = [0 for i in range(m)]
        for i in range(m):
            for j in range(n):
                cols[j] += mat[i][j]
                rows[i] += mat[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and cols[j]+rows[i]==2:
                    ans += 1
        return ans 
