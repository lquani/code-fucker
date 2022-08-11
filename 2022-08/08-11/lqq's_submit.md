## 题目
https://leetcode.cn/problems/reformat-the-string/solution/pythonjavatypescriptgo-by-himymben-nrem/
## 思路
双指针
## code
```py
class Solution:
    def reformat(self, s: str) -> str:
        ss = ''
        digit = ''
        ans = ''
        for cur in s:
            if ord('0')<=ord(cur)<=ord('9'):
                digit += cur 
            else:
                ss += cur 
        m = len(digit)
        n = len(ss)
        if abs(m-n)>1:
            return ''
        l1 = 0
        l2 = 0
        while l1<m and l2<n:
            if m>n:
                ans += digit[l1]+ss[l2]
            else:
                ans += ss[l2]+digit[l1]
            l1 += 1
            l2 += 1
        if l1<m :
            ans += digit[l1]
        if l2<n:
            ans += ss[l2] 
        return ans
