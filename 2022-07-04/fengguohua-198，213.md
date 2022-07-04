## 题目链接
https://leetcode.com/problems/house-robber/submissions/
https://leetcode.com/submissions/detail/738105961/

## 思路

dp[i] = max(dp[i-1], dp[i-2] + nums[i])

dp[i-1] 不抢当前[i]
dp[i-2] + nums[i] 抢当前[i] 获得的金额


## code

```cpp
// 198
int rob(vector<int>& nums) {
        if(nums.empty()) return 0;
        int n = nums.size();
        if(n==1) return nums[0];
        if(n==2) return max(nums[0], nums[1]);
        
        vector<int> value(n, 0);
        value[0] = nums[0];
        value[1] = max(nums[0], nums[1]);
        for (int i = 2; i < n; i++)
            value[i] = max(value[i-1], value[i-2]+nums[i]);
        
        return value.back();
    }

// 213
int helper(vector<int> &nums, int start, int end) {
    int n = nums.size();
    vector<int> dp(n, 0);
    dp[start] = nums[start];
    dp[start +1] = max(nums[start], nums[start+1]);

    for (int i = start + 2; i <= end; i++)
        dp[i] = max(dp[i-1], dp[i-2]+nums[i]);

    return dp[end];
}
int rob(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    if (n == 1) return nums[0];
    if (n == 2) return max(nums[0], nums[1]);
    int res1 = helper(nums, 0, n-2);
    int res2 = helper(nums, 1, n-1);
    
    return max(res1, res2);
}

```