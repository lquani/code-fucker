### 1031
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

#### 难度
medium

#### 思路
看答案了 bug free

#### code

```cpp
class Solution {
public:
    int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(4, 0));
        int sum = 0, maxSum = 0;
        for (int i = 0; i < firstLen; i++) sum += nums[i];
        maxSum = sum;
        dp[firstLen-1][0] = maxSum;
        for (int i = firstLen; i < n; i++) {
            sum -= nums[i-firstLen];
            sum += nums[i];
            maxSum = max(maxSum, sum);
            dp[i][0] = maxSum;
        }
        
        sum = 0, maxSum = 0;
        for (int i = 0; i < secondLen; i++) sum += nums[i];
        maxSum = sum;
        dp[secondLen-1][1] = maxSum;
        for (int i = secondLen; i < n; i++) {
            sum -= nums[i-secondLen];
            sum += nums[i];
            maxSum = max(maxSum, sum);
            dp[i][1] = maxSum;
        }
        
        sum = 0, maxSum = 0;
        for (int i = n - 1; i >= n-firstLen; i--) sum += nums[i];
        maxSum = sum;
        dp[n-firstLen][2] = maxSum;
        for (int i = n-1-firstLen; i >= 0; i--) {
            sum -= nums[i+firstLen];
            sum += nums[i];
            maxSum = max(maxSum, sum);
            dp[i][2] = maxSum;
        }
        
        sum = 0, maxSum = 0;
        for (int i = n - 1; i >= n-secondLen; i--) sum += nums[i];
        maxSum = sum;
        dp[n-secondLen][3] = maxSum;
        for (int i = n-1-secondLen; i >= 0; i--) {
            sum -= nums[i+secondLen];
            sum += nums[i];
            maxSum = max(maxSum, sum);
            dp[i][3] = maxSum;
        }
        
        //! l在左 m在右
        int res = 0;
        for (int i = firstLen; i <= n - secondLen; i++) 
            res = max(res, dp[i-1][0] + dp[i][3]);
        //! m在左 l在右
        for (int i = secondLen; i <= n - firstLen; i++)
            res = max(res, dp[i-1][1] + dp[i][2]);
        
        return res;
    }
};
```