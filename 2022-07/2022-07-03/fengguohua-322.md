## 题目链接
https://leetcode.com/problems/coin-change/submissions/

## 思路

动态规划 完全背包问题
dp[j] 表示刚好凑齐 j 金额所需的coin 的最小数,初始化所有的dp为INT_MAX
dp[0] = 0
++求组合问题:先遍历物品再从小到大遍历背包++

递推公式:dp[j] = min(dp[j], dp[j - coins[i] + 1)
 需要注意dp[j - coins[i]不能超过INT_MAX


## code
```cpp
int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1, INT_MAX);
        dp[0] = 0;
        for (int i = 0; i < coins.size(); i++) {
            for (int j = coins[i]; j <= amount; j++) {
                if (dp[j-coins[i]] < INT_MAX)
                    dp[j] = min(dp[j], dp[j-coins[i]] + 1);
            }
        }
        
        if (dp.back() == INT_MAX) return -1;
        
        return dp[amount];
    }
```