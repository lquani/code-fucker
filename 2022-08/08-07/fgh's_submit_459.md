### 459
https://leetcode.com/problems/repeated-substring-pattern/

#### 思路
遍历数组 获得和首字符相等的字符的index \
遍历一次这个数组 看substr是否和 target相等

#### code
```cpp
 bool repeatedSubstringPattern(string s) {
        vector<int> indexs;
        for (int i = 1; i < s.length(); i++) {
            if (s[i] == s[0]) indexs.push_back(i);
        }
        
        if (indexs.empty()) return false;
        
        std::string tmp;
        int n = s.length();
        for (int i = 0; i < indexs.size(); i++) {
            tmp = s.substr(0, indexs[i]);
            if (n % tmp.length() != 0) continue;
            
            int k = n / (tmp.length());
            bool isValid = true;
            for (int j = 0; j < k; j++) {
                std::string sub = s.substr(j * tmp.length(),  tmp.length());
                if (sub == tmp) continue;
                else {
                    isValid = false;
                    break;
                }
            }
            
            if (isValid) return true;
        }
        
        return false;    
    }
```