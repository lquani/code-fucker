### 556
https://leetcode.com/problems/next-greater-element-iii/

#### 思路
双指针法 \

#### code
```cpp

bool isValid(std::string& s) {
            std::string maxNum = std::to_string(INT_MAX);
            if (s.length() < maxNum.length()) return true;
            for (int i = 0; i < s.length(); i++) {
                if (s[i] < maxNum[i]) return true;
                else if (s[i] > maxNum[i]) return false;
            }

            return true;
        }
        int nextGreaterElement(int n) {
            std::string num = std::to_string(n);
            int len = num.length();
            //! < 从后往前找一个峰值
            if (len == 1) return -1;

            int p = len - 2;
            for (; p >= 0; p--) {
                if (num[p] >= num[p + 1]) continue;

                int i = p + 1;
                for (; i < len; i++) {
                    if (num[i] <= num[p]) break;
                }
                swap(num[p], num[i - 1]);
                sort(num.begin() + p + 1, num.end());
                if (isValid(num)) return stoi(num);

                return -1;
            }

            return -1;
        }

```