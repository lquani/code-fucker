## 题目
https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time/
## 思路
差分数列
## code
```py
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        query = [0 for i in range(1005)]
        m = len(startTime)
        for i in range(m):
            query[startTime[i]] += 1
            query[endTime[i]+1] -= 1
        for i in range(1,1001):
            query[i] += query[i-1]
        return query[queryTime]
