### 916
https://leetcode.com/problems/word-subsets/

#### 思路
哈希表  \
将words2 结合成一个哈希表字符串, 字符串单个字符个数,为words2当中最大值 \

#### code
```cpp
 void merge(vector<int> &maps, std::string &str) {
        vector<int> tmp(26, 0);
        for (char c : str) {
            tmp[c-'a']++;
        }
        
        for (int i = 0; i < 26; i++) 
            maps[i] = max(maps[i], tmp[i]);
    }
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
        vector<string> res;
        vector<int> maps(26, 0);
        for (auto & str : words2) {
            merge(maps, str);
        }
        
        for (auto & str : words1) {
            vector<int> tmp = maps;
            for (char c : str) {
                int index = c - 'a';
                if (tmp[index] != 0) 
                    tmp[index]--;
            }
            
            bool isValid = true;
            for (int i = 0; i < 26; i++) {
                if (tmp[i] != 0) {
                    isValid = false;
                    break;
                }
            }
            
            if (isValid) res.push_back(str);
        }
        
        return res;
    }
```