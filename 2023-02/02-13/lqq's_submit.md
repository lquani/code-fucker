## 题目
https://leetcode.cn/problems/replace-the-substring-for-balanced-string/submissions/
## 思路
1、先找出那些字母是多余的，多多少个，多出来的字母所组成的字符串叫s1，我们要替换的那个字符串叫s2,s2必须要包含s1的所有字符（不需要顺序一样）。
2、其实就是找到一个包含了s1的最短的s2，用双指针可以解决
## code
'py
'
