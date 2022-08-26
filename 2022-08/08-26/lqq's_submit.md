## 题目
https://leetcode.cn/problems/spiral-matrix-iii/submissions/
## 思路
设置一下方向和边界，当到达边界的时候转换方向
## code
```py
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        x, y, num, way = rStart, cStart, 1, 0 
        ways = [(0,1), (1,0), (0,-1), (-1,0)]
        upper, lower, left, right = rStart-1, rStart+1, cStart-1, cStart+1
        ans = []
        while num <= rows*cols:
            if 0<=x<rows and 0<=y<cols:
                ans.append([x,y])
                num += 1
            if way==0 and y == right:
                way+=1
                right += 1
            elif way==1 and x == lower:
                way += 1
                lower+=1 
            elif way==2 and y==left:
                left -= 1
                way += 1
            elif way==3 and x == upper:
                way = 0
                upper -= 1
            x += ways[way][0]
            y += ways[way][1]
        return ans 
