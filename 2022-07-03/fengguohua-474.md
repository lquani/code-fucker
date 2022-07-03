## 题目链接
[https://leetcode.com/problems/ones-and-zeroes/](http://)
## 思路
01 背包问题,
背包大小是二维的,size:(m, n)
问题转化为将一个 物品 (str) value值(重量值)是其中包含的0 1字符串个数
即:将一个重量为(zeroNum, oneNum)大小放进一个size为(m, n)的背包内
最大能放多少个;

## code
``` cpp
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        
        for (auto& str : strs) {
            int zeroNum = 0;
            for (auto& c : str) {
                if (c == '0') zeroNum += 1;
            }
            int oneNum = str.length() - zeroNum;
            for (int i = m; i >= zeroNum; i--) {
                for (int j = n; j >= oneNum; j--) {
                    dp[i][j] = max(dp[i][j], dp[i - zeroNum][j - oneNum] + 1);
                }
            }
        }
        
        return dp[m][n];
    }
};
```