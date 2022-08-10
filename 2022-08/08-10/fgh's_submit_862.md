### 862
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

#### 思路
优先队列 \
保存0~i 的累加和 \


#### code
```cpp
int shortestSubarray(vector<int>& nums, int k) {
	int res = INT_MAX, n = nums.size();
	priority_queue < pair<long, int>, vector<pair<long, int>>, greater<pair<long, int>>> vecs;
	long sum = 0;
	for (int i = 0; i < n; i++) {
		sum += nums[i];
		if (sum >= k) res = min(res, i + 1);
		while (!vecs.empty() && (sum - vecs.top().first) >= k) {
			res = min(res, i - vecs.top().second);
			vecs.pop();
		}
		vecs.push({ sum, i });
	}

	if (res == INT_MAX) return -1;

	return res;
}
```