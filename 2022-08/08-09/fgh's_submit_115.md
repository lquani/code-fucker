### 115
https://leetcode.com/problems/distinct-subsequences/

#### 思路
动态规划 \


#### code
```cpp
int numDistinct(string s, string t) {
	int m = s.length(), n = t.length();
	vector<vector<uint64_t>> dp(m+1, vector<uint64_t>(n+1, 0));
	//! < 1、dp(i)(j) 表示到s(i)为止,与 t(j)能匹配上的个数
	//! < 2、递推公式: 2.1 s(i) == s(j) dp(i)(j) = sum(dp(i)(j), dp(i-1)(j-1)--i与j匹配 , dp(i-1)(j) -- i与j不匹配
	//! <			    2.2 s(i) != s(j) dp(i)(j) = max(dp(i)(j), dp(i-1)(j)
	//! < 3、初始化: dp[0][0] = 1;
	dp[0][0] = 0;
	for (int j = 1; j <= n; j++) {
		int k = j;
		for (int i = j; i <= m; i++) {
			if (s[i-1] == t[j-1])
				dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + (j == 1 ? 1 : 0);
			else
				dp[i][j] = dp[i - 1][j];	
		}
	}

	return dp[m][n];
}
```