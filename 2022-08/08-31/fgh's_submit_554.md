### 554
https://leetcode.com/problems/brick-wall/

#### 思路
经过边缘 + 经过中间的砖块 == 常量 

#### code
```cpp
int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int, int> cnt;
        for (auto &widths : wall) {
            int sum = 0, n = widths.size();
            for (int i = 0; i < n - 1; i++) {
                sum += widths[i];
                cnt[sum] ++;
            }
        }
        
        int res = 0;
        for(auto & it : cnt) res = max(res, it.second);
        
        return wall.size() - res;
    }
```