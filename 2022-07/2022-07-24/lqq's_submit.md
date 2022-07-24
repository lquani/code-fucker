## 题目
https://leetcode.cn/problems/distance-between-bus-stops/
## 思路 
记录环形路程的总路程sumi，顺时针遍历start到destination的距离a，然后比较a和sumi-a的最小值
## code
```py
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sumi = sum(distance)
        ans = 0
        if start>destination:
            start,destination = destination,start
        for i in range(start,destination):
            ans += distance[i]
        return min(ans,sumi-ans)
```
