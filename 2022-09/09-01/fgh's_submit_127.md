### 127
https://leetcode.com/problems/word-ladder/

### 难度
hard

### 思考情况
看了视频思路 Hua Hua \
代码自己写的

#### 思路
广度优先搜索 \
1、wordList 用过的不能重复使用
2、搜索的每一层:遍历当前层的每一个 string 对这个字符串的每一个位置进行替换成a~z \
3、直到出现 endWord 返回结果

#### code
```cpp
int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        queue<string> vecs;
        vecs.push(beginWord);
        unordered_map<string, bool> maps;
        for (auto &str : wordList) maps[str] = false;
        int step = 1;
        while (!vecs.empty()) {
            int size = vecs.size();
            step++;
            for (int i = 0; i < size; i++) {
                auto str  = vecs.front();
                vecs.pop();
                for (int j = 0; j < str.length(); j++) {
                    char c = str[j];
                    for (int k = 0; k < 26; k++) {
                        if (c == k + 'a') continue;
                        str[j] = k + 'a';
                        if (maps.find(str) == maps.end()) continue;
                        if (maps[str]) continue;
                        if (str == endWord) return step;
                        maps[str] = true;
                        vecs.push(str);
                    }
                    str[j] = c;
                }
            }
        }
        
        return 0;
    }
```