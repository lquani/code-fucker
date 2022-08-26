### 301
https://leetcode.com/problems/remove-invalid-parentheses/

#### 思路

#### code

```cpp
class Solution {
public:
    bool isValid(string &str) {
        int n = str.length(), left = 0, right = 0;
        for (char c : str) {
            if (c == '(') left++;
            else if (c == ')') right++;
            else continue;
            if (right > left) return false;
        }
        
        return left == right;
    }
    void cntLR(string &str, int &l, int &r) {
        int n = str.length();
        for (char c : str) {
            if (c == '(') l++;
            else if (c == ')') {
                if (l == 0) r ++;
                else l--;
            }
        }
    }
    void helper(vector<string> &res, string &s, string tmp, int l, int r, int index) {
        int n = s.length();
        if (l ==0 && r == 0) {
            if (index < n) tmp += s.substr(index, n - index);
            if (isValid(tmp)) res.push_back(tmp);
            return;
        }
        
        for (int i = index; i < n; i++) {
            if ((s[i] >= 'a' && s[i] <= 'z') || (i != index && s[i] == s[i-1]))
                tmp.push_back(s[i]);
            else {
                if (r != 0) {
                    if (s[i] == ')') helper(res, s, tmp, l, r - 1, i + 1);
                } else if (l != 0){
                    if (s[i] == '(') helper(res, s, tmp, l - 1, r, i + 1);
                }
                tmp.push_back(s[i]);
            }
        }
    }
    vector<string> removeInvalidParentheses(string s) {
        vector<string> res;
        int n = s.length(), left = 0, right = 0;
        cntLR(s, left, right);
        helper(res, s, "", left, right, 0);
        
        return res;
    }
};
```