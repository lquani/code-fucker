### 149
https://leetcode.com/problems/max-points-on-a-line/submissions/

#### 思路
y = kx + b 将K B转化为 string 存入map \

#### code
```cpp
std::string getLineOfK(std::vector<int>& p1, std::vector<int>& p2) {
            if (p1[0] == p2[0]) return std::to_string(INT_MAX);

            double k = 1.0 * (p1[1] - p2[1]) / (1.0 * (p1[0] - p2[0]));
            if (p1[1] == p2[1]) k = 0.0;
            if (k < 0) return "-" + std::to_string(abs(k));

            return std::to_string(k);
        }

        std::string getLineOfB(std::vector<int>& p1, std::vector<int>& p2) {
            if (p1[0] == p2[0]) return std::to_string(p1[0]);

            double k = 1.0 * (p1[1] - p2[1]) / (1.0 * (p1[0] - p2[0]));
            double b = p1[1] * 1.0 - k * p1[0] * 1.0;

            return std::to_string(b);
        }

        int maxPoints(vector<vector<int>>& points) {
            int n = points.size();
            if (n <= 1) return n;
            int res = 1;
            
            for (int i = 0; i < n; i++) {
                unordered_map<string, int> maps;
                for (int j = i + 1; j < n; j++) {
                    auto& p1 = points[i], & p2 = points[j];
                    std::string key = getLineOfK(p1, p2) + "&" + getLineOfB(p1, p2);
                    maps[key] ++;
                }
                for (auto& it : maps)
                    res = max(res, it.second + 1);
            }

            return res;

        }
```