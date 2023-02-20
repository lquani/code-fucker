## 题目
https://leetcode.cn/problems/best-poker-hand/solution/zui-hao-de-bu-ke-shou-pai-by-leetcode-so-5zz2/
## 思路
哈希+枚举
## code
```py
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        flush = False
        pair = False
        kind = False
        m = len(ranks)
        res = {}
        for i in range(m):
            res[ranks[i]] = res.get(ranks[i],0)+1
            res[suits[i]] = res.get(suits[i],0)+1
            cur1 = res[ranks[i]]
            if cur1==2:
                pair = True
            elif cur1==3:
                kind=True 
            cur2 = res[suits[i]]
            if cur2 == 5:
                flush = True 
        if flush:
            return "Flush"
        elif kind:
            return "Three of a Kind"
        elif pair:
            return "Pair"
        return "High Card"
