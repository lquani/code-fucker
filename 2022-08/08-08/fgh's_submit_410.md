### 410
https://leetcode.com/problems/split-array-largest-sum/

### 思路
1、dp[i][j] 表示将0 ~ nums[i]划分为 j个子串各自和的最大值的最小值 \
2、递推关系:dp[i][j] = min(dp[i][j], max(dp[i-k][j-1], sum[i-k:i]) \ 
	    k 表示 nums[i]应该和0~i中哪个数组成单独的子串 \
 3、初始化:j = 0: dp[i][0] = 0 ; j = 1: dp[i][1] 是数组的累加和
 
 ### code
```cpp
int splitArray(vector<int>& nums, int m) {
	if (m == 0) return 0;
	int n = nums.size();
	vector<vector<int>> dp(n, vector<int>(m+1, INT_MAX));
	//! < 1、dp[i][j] 表示将0 ~ nums[i]划分为 j个子串各自和的最大值的最小值
	//! < 2、递推关系:dp[i][j] = min(dp[i][j], max(dp[i-k][j-1], sum[i-k:i])
	//! <     k 表示 nums[i]应该和0~i中哪个数组成单独的子串
	//! < 3、初始化:j = 0: dp[i][0] = 0 ; j = 1: dp[i][1] 是数组的累加和 
	int sum = 0;
	for (int i = 0; i < n; i++) {
		sum += nums[i];
		dp[i][0] = 0;
		dp[i][1] = sum;
	}
	
	for (int i = 1; i < n; i++) {
		for (int j = 2; j <= m; j++) {
			int sum = 0;
			for (int k = i - 1; k >= j - 2; k--) {
				int sub = i - k;
				sum += nums[i - sub + 1];
				dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sum));
			}
		}
	}

	return dp[n - 1][m];
}
```