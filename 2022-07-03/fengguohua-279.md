## 题目链接
https://leetcode.com/problems/perfect-squares/submissions/

## 思路
整体思路和 [322](https://leetcode.com/problems/coin-change/) 题差不多
不同点:每次放入背包的数,必须是完全平方数

## code
```cpp
class Solution {
public:
    bool isSquare(int num) {
        int k = sqrt(num);
        
        return k * k == num;
    }
    int numSquares(int n) {
        vector<int> dp(n+1, INT_MAX);
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 1; i <= n; i++) {
            if (!isSquare(i)) 
                continue;
            dp[i] = 1;
            
            for (int j = i; j <= n; j++) {
                if (dp[j - i] < INT_MAX)
                    dp[j] = min(dp[j], dp[j - i] + 1);
            }
        }
        
        return dp[n];
    }
};

```