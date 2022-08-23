## 题目
https://leetcode.cn/problems/sorted-matrix-search-lcci/submissions/
## 思路
遍历每一行，对每一列用二分
## code
```py
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            l = n - 1
            cur = 0
            while cur <= l:
                mid = cur + (l - cur)//2
                print(mid)
                if matrix[i][mid]==target:
                    return True 
                elif matrix[i][mid]>target:
                    l = mid - 1
                else:
                    cur = mid + 1
        return False
