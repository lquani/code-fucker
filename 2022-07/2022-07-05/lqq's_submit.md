## 题目
每日一题 https://leetcode.cn/problems/my-calendar-i/submissions/
## 思路
直接暴力
```py
class MyCalendar:

    def __init__(self):
        self.meeting = []


    def book(self, start: int, end: int) -> bool:
        if not self.meeting:
            self.meeting.append([start,end])
            return True
        m = len(self.meeting)
        for l,r in self.meeting:
            if end>l and start<r:
                return False
        self.meeting.append([start,end])
        return True
```
