## 题目
https://leetcode.cn/problems/cells-with-odd-values-in-a-matrix/submissions/
## 思路
直接模拟，easy的题就是easy
## code
```py
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0 for i in range(m)]
        cols = [0 for i in range(n)]
        for i,j in indices:
            rows[i] += 1
            cols[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if (rows[i]+cols[j])%2==1:
                    ans += 1
        return ans ```
