## 题目
https://leetcode.cn/problems/my-calendar-ii/
## 思路
维护两个列表，first记录没有相交的日程，second记录有一次相交的日程，先遍历second，如果有重合就返回fasle，然后遍历first，有重合记录到second里
## code
```py
class MyCalendarTwo:

    def __init__(self):
        self.first = []
        self.second = []

    def book(self, start: int, end: int) -> bool:
        for l,r in self.second:
            if start<r and l<end:
                return False 
        for l,r in self.first:
            if start<r and l<end:
                self.second.append([max(start,l),min(end,r)])
        self.first.append([start,end])
        return True
    
```
