### 91
https://leetcode.com/problems/decode-ways/

#### 思路1
1、回溯算法(超时) 	\	

#### code1
```cpp
void helper(std::string &s, int start, int &res) {
        int n = s.length();
        if (start == n) {
            res++;
            return;
        }
        if (s[start] == '0') return;
        
        std::string num;
        for (int i = start; i < n; i++) {
            num.push_back(s[i]);
            int index = stoi(num);
            if (index <= 26) 
                helper(s, i + 1, res);
            else 
                break;
        }
    }
    int numDecodings(string s) {
        int res = 0, n = s.length();
        helper(s, 0, res);
        
        return res;
    }
```

#### 思路2
动态规划
dp[i] 表示 以 s[i]结尾的 可decode的总类个数 \
1、s(i) == '0' : 当前i必须要和i-1匹配, 如果能匹配上dp(i) = dp(i-1) + dp(i-2) 如果不能匹配上dp(i)和i-1都是0;\
2、s(i) > 6 :只能自己和自己匹配,或者 和i-1是1的情况匹配\
3、只能前序是1 或者 2 的时候匹配
#### code2
```cpp
int numDecodings(string s) {
        int n = s.length();
        if (n == 0) return 0;
    
        std::vector<int> dp(n, 0);
        dp[0] = s[0] == '0' ? 0 : 1;
        for (int i = 1; i < n; i++) {
            if (s[i] == '0') {
                if (s[i-1] == '1' || s[i-1] == '2') {
                    dp[i] = i == 1 ? 1 : dp[i-2];
                    dp[i-1] = 0;
                } else {
                    dp[i] = 0;
                    dp[i-1] = 0;
                }
            } else if (s[i] > '6') {
                if (s[i-1] == '1') dp[i] = dp[i-1] + (i-2 >= 0 ? dp[i-2] : 1);
                else dp[i] = dp[i-1];
            } else {
                if (s[i-1] == '1' || s[i-1] == '2') dp[i] = dp[i-1] + (i-2 >= 0 ? dp[i-2] : 1);
                else dp[i] = dp[i-1];
            }
        }
        
        return dp.back();
    }

```