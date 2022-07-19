### 155
#### 链接
[https://leetcode.com/problems/min-stack/](http://)

#### 思路
两个栈, 一个栈用来保存最小值


#### code
```cpp
class MinStack {
public:
    stack<int> stack_;
    stack<int> min_stack_;
    MinStack() {

    }

    void push(int val) {
        this->stack_.push(val);
        if (this->min_stack_.empty() || val <= this->min_stack_.top())
            this->min_stack_.push(val);
    }

    void pop() {
        int num = this->stack_.top();
        this->stack_.pop();
        if (!this->min_stack_.empty() && num == this->min_stack_.top())
            this->min_stack_.pop();
    }

    int top() {
        return this->stack_.top();
    }

    int getMin() {
        return this->min_stack_.top();
    }
};

```

### 32

#### 链接
[https://leetcode.com/problems/longest-valid-parentheses/](http://)

#### 思路

//! < dp[i]表示以i结尾的,最长的有效字符串长度、  \
    //! 递推公式 1、s[i] == '(' dp[i] = 0;  \
    //!         2、s[i] == ')' :  \
    //!                    2.1 if s[i-1] == '(' dp[i] = i-2>=0 ? dp[i-2]+2 : 2; 和相邻的(组成一对  \
    //!                    2.2 if i-1 < 0 dp[i-1] = 0  \
    //!                    2.3 和最远端的(组成一对 最远端 dp[i-1] + j + 1 = i -> j = i - dp[i-1] - 1; if (j < 0 || s[j] == ')' dp[i-1] = 0 else
    
#### code
```cpp
int longestValidParentheses(string s) {
    int n = s.length(), res = 0;
    vector<int> dp(n, 0);
    //! < dp[i]表示以i结尾的,最长的有效字符串长度、
    //! 递推公式 1、s[i] == '(' dp[i] = 0;
    //!         2、s[i] == ')' :
    //!                    2.1 if s[i-1] == '(' dp[i] = i-2>=0 ? dp[i-2]+2 : 2; 和相邻的(组成一对
    //!                    2.2 if i-1 < 0 dp[i-1] = 0
    //!                    2.3 和最远端的(组成一对 最远端 dp[i-1] + j + 1 = i -> j = i - dp[i-1] - 1; if (j < 0 || s[j] == ')' dp[i-1] = 0 else
    for (int i = 1; i < n; i++) {
        if (s[i] == '(') continue;
        if (i-1 < 0) dp[i] = 0;
        else if (s[i-1] == '(') dp[i] = i-2 >= 0 ? dp[i-2]+2 : 2;
        else {
            int j = i - dp[i-1] - 1;
            if (j < 0 || s[j] == ')') dp[i] = 0;
            else dp[i] = dp[i-1] + 2 + (j - 1 < 0 ? 0 : dp[j-1]);
        }
        res = max(res, dp[i]);
    }

    return res;
}
```

### 43
#### 链接
[https://leetcode.com/problems/multiply-strings/](http://)

#### 思路
双指针法,带carry
#### code
``` cpp
string multiply(string num1, string num2) {
        std::string res;

        int m = num1.size(), n = num2.length();
        for (int i = n - 1; i >= 0; i--) {
            int index = n - 1 - i;
            int carry = 0;
            for (int j = m - 1; j >= 0; j--) {
                int n1 = num2[i] - '0', n2 = num1[j] - '0', n3 = index >= res.size() ? 0 : res[index] - '0';
                int tmp = n1 * n2 + carry + n3;
                carry = tmp / 10;
                tmp = tmp % 10;
                char c = tmp + '0';
                if (index >= res.size())
                    res.push_back(c);
                else
                    res[index] = c;
                index++;
            }
            if (carry != 0) {
                char c = carry + '0';
                res.push_back(c);
            }
        }


        reverse(res.begin(), res.end());
        if (res.empty()) return "0";
        if (res[0] == '0') return "0";
        return res;
    }
```