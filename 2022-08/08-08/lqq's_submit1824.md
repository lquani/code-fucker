## 题目
https://leetcode.cn/problems/minimum-sideway-jumps/submissions/
## 思路
动态规划，可以用一个3\*m的矩阵，矩阵中的位置表示从出发位置（0列1行）到次位置所需要跳跃的最小次数，它可以从三个位置来，分别是从同一列的其他位置跳跃而来，或者从坐边不用跳跃来，取最小值即可
## code
```py
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        m = len(obstacles)
        if m<3:
            return 0
        dp1,dp2,dp3 = 1, 0, 1 # 初始化
        for i in range(1,m):
            pre1,pre2,pre3 = dp1,dp2,dp3 
            dp1,dp2,dp3 = float('inf'),float('inf'),float('inf') # 初始化，如果有障碍物则无法跳到，赋予一个极大值
            if obstacles[i]!=1:dp1=pre1 # 从左边跳过来
            if obstacles[i]!=2:dp2=pre2
            if obstacles[i]!=3:dp3=pre3
            if obstacles[i]!=1:dp1=min(dp1,min(dp2,dp3)+1) # 从同一列其他位置跳过来，比较一下三个位置过来谁的跳跃次数最短
            if obstacles[i]!=2:dp2=min(dp2,min(dp1,dp3)+1)
            if obstacles[i]!=3:dp3=min(dp3,min(dp2,dp1)+1)
        return min(dp1,dp2,dp3) # 返回最后一列里最小的数
```
