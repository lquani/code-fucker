### 673
https://leetcode.com/problems/number-of-longest-increasing-subsequence/
#### 思路
动态规划  \
dp[i] 表示以nums[i]结尾的递增序列的长度  \
cnt[i] 表示以nums[i]结尾的最长递增序列的个数 \

#### code
```cpp
int findNumberOfLIS(vector<int> &nums) {
	int n = nums.size();
	std::vector<int> dp(n, 1), cnt(n, 1);
	int res = 0, maxLen = 0;
	//! < dp[i] 表示以nums[i]结尾的递增序列的长度
	//! < cnt[i] 表示以nums[i]结尾的最长递增序列的个数
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (nums[i] <= nums[j]) continue;
			int tmp = dp[j] + 1;
			if (tmp > dp[i]) { // 长度变大了 重置个数和长度
				dp[i] = tmp;
				cnt[i] = cnt[j];
			}
			else if (tmp == dp[i])  // 长度相等 
				cnt[i] += cnt[j];
		}

		if (dp[i] == maxLen) res += cnt[i];
		else if (dp[i] > maxLen) {
			res = cnt[i];
			maxLen = dp[i];
		}
	}

	return res;
}

```