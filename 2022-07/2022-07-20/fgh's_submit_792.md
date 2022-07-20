### 792
#### 题目链接
https://leetcode.com/problems/number-of-matching-subsequences/

#### 思路
##### 思路1:暴力法
std::unordered_map<std::string, int> maps;  记录中间变量;  \
超时

###### code
```cpp
int numMatchingSubseq(string s, vector<string>& words) {
        int m = s.length(), n = words.size(), res = 0;
        if (m == 0) return 0;
        
        std::unordered_map<std::string, int> maps; 
        for (auto & str : words) {
            if (maps.count(str) != 0) {
                res++;
                continue;
            }
            
            int i = 0, j = 0;
            while (i < m && j < str.length()) {
                if (maps.count(str.substr(0, j+1)) && (j+1 == str.length() || maps.count(str.substr(j+1, str.length()-j-1)))) {
                    res ++;
                    j = -1;
                    break;
                }
                
                if (s[i] == str[j]) {
                    i++;
                    j++;
                } else i++;
            }
            if (j == str.length()) {
                maps[str]++;
                res++;
            } else if (j == -1) continue;
            else 
                maps[str.substr(0, j+1)]++;
        }
        
        return res;

    }
```

##### 思路2: 桶排序 参考了 答案思路
使用桶,26个桶分别代表,字母开头a~z的的字符串的索引; \
1、初始化桶  \
2、遍历字符串,获得字母 c ; 进去c代表的桶\
 遍历桶内的字符串,如果字符串的长度是1,代表当前字符串匹配完毕,结果+1,从桶内删除掉这个字符串  \
 如果长度不是1,将当时字符串str去掉首字符,从当前桶内删除该字符串,并且重新按照当时字符串首字符加入桶。

##### code
```cpp
int numMatchingSubseq(string s, vector<string>& words) {
        int n = words.size(), res = 0;
        vector<vector<int>> buckets(26);
        int index = 0;
        for (auto & str : words) {
            int start = str[0] - 'a';
            buckets[start].push_back(index);
            index++;
        }
        
        for (char c : s) {
            auto &bucket = buckets[c-'a'];
            for (int i = 0; i < bucket.size(); i++) {
                auto &str = words[bucket[i]];
                int size = str.length();
                if (str.length() == 1) {
                    res++;
                    bucket.erase(bucket.begin()+i);
                    i--;
                }
                else {
                    str = str.substr(1, str.length()-1);
                    if (c != str[0]) {
                        buckets[str[0]-'a'].push_back(bucket[i]);
                        bucket.erase(bucket.begin()+i);
                        i--;
                    }
                }  
            }
        }
        
        return res;
    }
```
