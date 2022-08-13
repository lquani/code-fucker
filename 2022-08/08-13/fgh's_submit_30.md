### 30
https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/

#### 思路
哈希表

#### code
```cpp
vector<int> findSubstring(string s, vector<string>& words) {
            vector<int> res;
            int m = words.size(), n = words[0].size(), ls = s.size();
            unordered_map<string, int> maps;
            for (auto& str : words) maps[str]++;

            for (int i = 0; i <= ls - n * m; i++) {
                unordered_map<string, int> cnts;
                int j = 0;
                for (; j < m; j++) {
                    std::string tmp = s.substr(i + j * n, n);
                    if (maps.count(tmp) == 0) break;
                    cnts[tmp]++;
                    if (cnts[tmp] > maps[tmp]) break;
                }

                if (j == m) res.push_back(i);
            }

            return res;
        }

```