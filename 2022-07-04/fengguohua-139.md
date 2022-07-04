## 题目链接
https://leetcode.com/problems/word-break/

## 思路
背包问题: \
wordDict[i] 作为物品大小
s.length() 作为背包大小
转化:wordDict 物品的排列恰好能构成 背包 s
	 排列问题:先遍历背包 再遍历物品
 dp[i] 由wordDict内物品恰好组成s.substr(0, i)的字符串
 dp[i] = dp[i] && dp[i - len]  
 
 ## code
 
 ```cpp
 bool wordBreak(string s, vector<string>& wordDict) {
    int n = s.length();
    vector<bool> dp(n+1, false);
    dp[0] = true;

    for (int i = 1; i <= n; i++) {
        for (auto& str : wordDict) {
            if (dp[i]) break;
            int len = str.length();
            if (i - len >= 0 && s.substr(i-len, len) == str)
            dp[i] = dp[i - len];
        }
    }


    return dp.back();
}
 ```
