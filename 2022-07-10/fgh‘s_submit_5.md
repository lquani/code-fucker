## 题目链接
[https://leetcode.com/problems/longest-palindromic-substring/](http://)

## code
```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        
        //! dp[i][j] 表示[i][j]是否是回文子串
        int res = 1;
        int start = 0;
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
            for (int j = 0; j < i; j++) {
                if (s[i] != s[j]) continue;
                if (dp[i-1][j+1]|| (i-j) <= 2) dp[i][j] = true;
                
                if (dp[i][j] && i-j+1 > res) {
                    res = i-j+1;
                    start = j;
                }
            }
        }
        
        return s.substr(start, res);
    }
};

```
