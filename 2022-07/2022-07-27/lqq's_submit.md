## 题目
https://leetcode.cn/problems/keys-and-rooms/
## 思路
遍历，用哈希记录拿到的要是，在开房门的时候如果拿到新的钥匙就加入哈希里，维护一个列表，记录拿到的钥匙，重复出现的钥匙不记录，最后钥匙的数量等于房间的数量则返回true
## code
```py
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        res = {0:1}
        stack = []
        for key in rooms[0]:
            res[key]=1
            stack.append(key)
        ans = 1
        while stack:
            print(stack)
            key = stack.pop(0)
            for s in rooms[key]:
                if res.get(s,0)!=0:
                    continue
                stack.append(s)
                res[s] = 1
        return len(res) == len(rooms)
```
