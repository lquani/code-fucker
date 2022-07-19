### 165
#### 链接
https://leetcode.com/problems/compare-version-numbers/

#### 思路
双指针法,以.进行分割  \
比较繁琐

#### code
```cpp
class Solution {
public:
    int compareVersion(string version1, string version2) {
	int m = version1.length(), n = version2.length();
	int p1 = 0, p2 = 0;
	std::string s1, s2;
	while (p1 <= m && p2 <= n) {
		if (p1 == m && ((!s1.empty() && s1.back() != '.') || s1.empty())) 
			s1.push_back('.');
			
		if (p2 == n && ((!s2.empty() && s2.back() != '.') || s2.empty())) 
			s2.push_back('.');
		


		if (!s1.empty() && s1.back() == '.' && !s2.empty() && s2.back() == '.') {
			s1.pop_back();
			s2.pop_back();
			if (s1.length() < s2.length()) return -1;
			else if (s1.length() > s2.length()) return 1;

			for (int i = 0; i < s1.length(); i++) {
				if (s1[i] < s2[i]) return -1;
				else if (s1[i] > s2[i]) return 1;
			}
			s1.clear();
			s2.clear();
			if (p1 == m && p2 == n) break;
		}

		if (s1.empty() && p1 < m && version1[p1] == '0') {
			p1++;
			continue;
		}
		if (s2.empty() && p2 < n && version2[p2] == '0') {
			p2++;
			continue;
		}

		if (p1 < m && s1.back()!='.') s1.push_back(version1[p1++]);
		if (p2 < n && s2.back()!='.') s2.push_back(version2[p2++]);
	}

	if (s1.empty() && s2.empty()) return 0;
	if (s1.empty()) return -1;

	return 1;
}
};
```

### 64

#### 链接
https://leetcode.com/problems/minimum-path-sum/

#### 思路
动态规划  \
//! 动态规划, dp[i][j] 表示从左上角到dp[i][j] 的最短路径 \

#### code

```cpp
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
	int m = grid.size();
	int n = grid[0].size();
	
	vector<vector<int>> dp(m, vector<int>(n, 0));
	//! 动态规划, dp[i][j] 表示从左上角到dp[i][j] 的最短路径

	//! init 
	dp[0][0] = grid[0][0];
	for (int i = 1; i < n; i++) dp[0][i] = dp[0][i - 1] + grid[0][i];
	for (int i = 1; i < m; i++) dp[i][0] = dp[i - 1][0] + grid[i][0];

	//! computer
	for (int i = 1; i < m; i++) {
		for (int j = 1; j < n; j++) {
			dp[i][j] = (min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]);
		}
	}

	return dp.back().back();
}
};

```
