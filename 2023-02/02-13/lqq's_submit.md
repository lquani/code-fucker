## 题目
https://leetcode.cn/problems/replace-the-substring-for-balanced-string/submissions/
## 思路
1、先找出那些字母是多余的，多多少个，多出来的字母所组成的字符串叫s1，我们要替换的那个字符串叫s2,s2必须要包含s1的所有字符（不需要顺序一样）。  
2、其实就是找到一个包含了s1的最短的s2，用双指针可以解决。
## code
```py
## 这代码写得又长又臭，晚点再优化
class Solution:
    def balancedString(self, s: str) -> int:
        m = len(s)
        n = m//4
        ans = float("inf")
        res1 = {}
        res2 = {}
        for i in range(m):
            res1[s[i]]=res1.get(s[i],0)+1
        res2 = {'Q':0,'W':0,'E':0,'R':0}
        for key,value in res1.items():
            res2[key] = value-n if value-n>0 else 0
        flag = 0
        for key,value in res2.items():
            if value==0:
                flag += 1
        cur = {'Q':0,'W':0,'E':0,'R':0}
        left = 0 
        right = 0
        while right<m:
            cur[s[right]] += 1
            if cur[s[right]]==res2[s[right]]:
                flag += 1
                while flag==4:
                    ans = min(right - left + 1,ans)
                    cur[s[left]] -= 1
                    if cur[s[left]]<res2[s[left]]:
                        flag -= 1
                    left += 1
            right += 1
        return 0 if ans==float("inf") else ans 
