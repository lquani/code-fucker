### 678
https://leetcode.com/problems/valid-parenthesis-string/

#### 思路
![](https://github.com/lquani/code-fucker/blob/main/001image/678.png) \
动态规划  \
如上图所示, dp[i][j] 代表 s[j]~s[i]的子串是否是有效的\
遍历方式,从左到右遍历 i , j从0遍历到i-1 \
有以下几种情况: \
1、如果是单个字符串,dp[i][i] = s[i]=='' \
2、如果s[i] == ( 这个时候j~i无论如何不能匹配 dp[i][j] = false; \
3、如果i-j == 1, 只有两个字符串: dp[i][j] = s[j] != ')', 只有s[j]是)的时候不匹配 \
4、如果i-j > 1 分为两种情况: \
4.1 边界条件1:如果s[i] == * 这个时候可以是空的 dp[i][j] = dp[i-1][j] \
4.2 边界条件2: 如果s[i] 与 是s[j]进行了匹配,dp[i][j] = dp[i-1][j+1] \
4.3 如果s[i]与j+1 到 i-1之间任意一个字符串匹配,这个时候需要满足的条件就是:
	k不能是右括号, 并且dp[k][j-1] 是有效字符 并且 dp[i-1][k+1]是有效字符
    ~~
#### code
```cpp
bool checkValidString(string s) {
	int n = s.length();
    vector<vector<bool>> dp(n, vector<bool>(n, false));
	//! < dp[i][j] 表示 s[i]~s[j]是否是有效的;
	for (int i = 0; i < n; i++) {
		if (s[i] == '*') dp[i][i] = true;
		if (s[i] == '(') continue;
		for (int j = 0; j < i; j++) {
			if (s[j] == ')') continue;

			if (i - j == 1) dp[i][j] = s[j] != ')';
			else {
				dp[i][j] = s[i] == '*' && dp[i - 1][j];
				dp[i][j] = dp[i][j] || dp[i - 1][j + 1];
				for (int k = j+1; k < i && !dp[i][j]; k++) {
					dp[i][j] = s[k] != ')' && dp[k - 1][j] && (i-k==1 || dp[i-1][k + 1]);
				}
			}
		}
	}

	return dp.back()[0];
}
```
