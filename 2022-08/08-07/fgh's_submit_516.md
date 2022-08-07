### 516
https://leetcode.com/problems/longest-palindromic-subsequence/

#### 思路
动态规划 \
dp[i][j]表示 s(j) ~ s(i)之间的最长回文的长度

#### code
```cpp
int longestPalindromeSubseq(string s) {
            int n = s.length();
            vector<vector<int>> dp(n, vector<int>(n, 0));
            //! dp[i][j] 表示s[j] ~ s[i]之间的

            for (int i = 0; i < n; i++) {
                dp[i][i] = 1;
                for (int j = i - 1; j >= 0; j--) {
                    if (s[i] == s[j])
                        dp[i][j] = max(dp[i][j], i - j == 1 ? 2 : dp[i - 1][j + 1] + 2);
                    else {
                        dp[i][j] = max(dp[i][j], i - j == 1 ? 0 : dp[i - 1][j + 1]);
                        dp[i][j] = max(dp[i][j], dp[i-1][j]);
                        dp[i][j] = max(dp[i][j], dp[i][j+1]);
                    }
                }
            }

            return dp[n - 1][0];
        }
```