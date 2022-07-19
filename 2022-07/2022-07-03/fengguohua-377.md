## 题目链接
https://leetcode.com/problems/combination-sum-iv/submissions/

## 思路
完全背包 求解排列数目
先遍历背包容量 再遍历物品

## 代码
```cpp
int combinationSum4(vector<int>& nums, int target) {
        vector<int> dp(target+1, 0);
        dp[0] = 1;
        
        for (int i = 1; i <= target; i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (i - nums[j] >= 0 && dp[i] < INT_MAX - dp[i - nums[j]])
                    dp[i] += dp[i - nums[j]];
            }
        }
        
        return dp[target];
    }
```