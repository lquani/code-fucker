## 题目链接
https://leetcode.com/problems/interleaving-string/submissions/

## 思路
动态规划  \
二维dp  \
dp[i][j] 代表 p[i][j] 表示 s1 0:i + s2 0:j 交错相加是否能构成 s3的 (0~i+j)部分

## code
```cpp
bool isInterleave(string s1, string s2, string s3) {
        int m = s1.length(), n = s2.length(), k = s3.length();
        if (m + n != k) return false;
        vector<vector<bool>> dp(m+1, vector<bool>(n+1, false));
        //! < dp[i][j] 表示 s1 0:i + s2 0:j 相加是否能构成 s3的 (0~i+j)部分
        
        dp[0][0] = true;
        for (int i = 1; i <= m; i++) 
            dp[i][0] = s1.substr(0, i) == s3.substr(0, i);
        for (int i = 1; i <= n; i++)
            dp[0][i] = s2.substr(0, i) == s3.substr(0, i);
        
        for (int i = 1; i <=m; i++) {
            for (int j = 1; j <= n; j++) {
                std::string s3_ = s3.substr(i+j-2, 2);
                std::string t1 = s1.substr(i-1, 1) + s2.substr(j-1, 1);
                std::string t2 = s2.substr(j-1, 1) + s1.substr(i-1, 1);
                if (dp[i-1][j-1]) dp[i][j] = dp[i][j] || (s3_ == t1) || (s3_ == t2);
                if (dp[i-1][j]) dp[i][j] = dp[i][j] || (s3[i+j-1] == s1[i-1]);
                if (dp[i][j-1]) dp[i][j] = dp[i][j] || (s3[i+j-1] == s2[j-1]);
            }
        }
        
        return dp[m][n];
    }
```