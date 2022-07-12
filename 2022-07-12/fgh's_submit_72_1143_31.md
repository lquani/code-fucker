## 72
### 题目链接
[https://leetcode.com/problems/edit-distance/](http://)  \

### 思路

动态规划:\
含义:dp[i][j] 表示word1.substr(0, i) 转化为 word2[(0, j)需要的最短距离   \
递推公式: 有四种操作 1、插入 -- dp[i-1][j]+1  2、删除 -- dp[i][j-1]+1  3、替换 -- dp[i-1][j-1]+1  4、word1[i] == word1[j] : dp[i-1][j-1];  \
初始化:0~(i)初始化为i


### code
```cpp
int minDistance(string word1, string word2) {
    int m = word1.length(), n = word2.length();
    if (m == 0) return n;
    if (n == 0) return m;

    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    //! 含义:dp[i][j] 表示word1.substr(0, i) 转化为 word2[(0, j)需要的最短距离
    //! 递推公式: 有四种操作 1、插入 -- dp[i-1][j]+1  2、删除 -- dp[i][j-1]+1  3、替换 -- dp[i-1][j-1]+1  4、word1[i] == word1[j] : dp[i-1][j-1];
    //! 初始化:0~(i)初始化为i
    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int i = 0; i <= n; i++) dp[0][i] = i;
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1[i-1] == word2[j-1]) dp[i][j] = dp[i-1][j-1];
            else dp[i][j] = min(min(dp[i-1][j-1], dp[i][j-1]), dp[i-1][j]) + 1;
        }
    }
    
    return dp[m][n];
}
```


## 1143
### 链接
[https://leetcode.com/problems/longest-common-subsequence/](http://)


### 思路
和上一题差不多思路


### code
```cpp
int longestCommonSubsequence(string text1, string text2) {
    int m = text1.length(), n = text2.length();
    int res = 0;
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    //! < dp[i][j] 代表text1.substr(0, i) 与 text2.substr(0, j)的最长公共子序列
    //! < 递推公式 text1[i] == text2[j] dp[i][j] = dp[i-1][j-1] + 1; else max(max(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1[i-1] == text2[j-1]) dp[i][j] = dp[i-1][j-1] + 1;
            else dp[i][j] = max(max(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]);
        }
    }
    
    return dp[m][n];
}
```

## 31
### 链接
[https://leetcode.com/problems/next-permutation/](http://)

### 思路

双指针法:寻找峰值;\
从后往前寻找一个严格递增的序列: \
* 找到了一个峰值(拐点)--当前点<峰值点; 寻找递增序列当中最小的 哪个大于当前点的值【二分法】,交换两个值,并且sort当前点后的序列 \
* 如果没有找到,是个递增序列,下一个序列就反转当前序列

### code
```cpp

void nextPermutation(vector<int> &nums) {
    //! 思路:从后往前找一个递增序列,如果一直递增,continue
    //!       出现峰值: 交换峰值左右值,对峰值之后的数据排序

    int n = nums.size(), right = n - 1;
    for (; right >= 0; right--) {
        if (right == n-1 || nums[right] >= nums[right+1]) continue;


        //! < find > target
        int target = nums[right];
        int p1 = right+1, p2 = n-1;
        while(p1 <= p2) {
            int mid = p1 + (p2 - p1) / 2;
            if (nums[mid] > target) p1 = mid + 1;
            else p2 = mid - 1;
        }

        //! < change
        swap(nums[right], nums[p2]);
        sort(nums.begin()+right+1, nums.end());
        return;
    }

    if (right == -1) sort(nums.begin(), nums.end());
}
```










