## 题目链接
https://leetcode.com/problems/coin-change-2/
## 思路
题目类型:完全背包
完全背包,可多次重复放入
遍历背包容量 从小到大遍历

## code
``` cpp
int change(int amount, vector<int>& coins) {
        vector<int> dp(amount + 1, 0);
        dp[0] = 1;
        for (int i = 0; i < coins.size(); i++) {
            for (int j = coins[i]; j <= amount; j++) 
                dp[j] += dp[j - coins[i]];
        }
        
        return dp.back();
    }
```