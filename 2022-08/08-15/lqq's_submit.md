## 题目
https://leetcode.cn/problems/design-circular-deque/submissions/
## 思路
python的list可以pop实现 删除头和尾元素 O(1)的复杂度
## code
```py
class MyCircularDeque:

    def __init__(self, k: int):
        self.list = []
        self.maxi = k
        self.cur = 0

    def insertFront(self, value: int) -> bool:
        if self.cur == self.maxi:
            return False
        self.list = [value] + self.list 
        self.cur += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.cur == self.maxi:
            return False
        self.list.append(value)
        self.cur += 1
        return True

    def deleteFront(self) -> bool:
        if not self.list:
            return False 
        self.list.pop(0)
        self.cur -= 1
        return True 

    def deleteLast(self) -> bool:
        if not self.list:
            return False 
        self.list.pop()
        self.cur -= 1
        return True        

    def getFront(self) -> int:
        if not self.list:
            return -1 
        return self.list[0]  

    def getRear(self) -> int:
        if not self.list:
            return -1 
        return self.list[-1] 

    def isEmpty(self) -> bool:
        return self.cur==0

    def isFull(self) -> bool:
        return self.cur == self.maxi


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```
