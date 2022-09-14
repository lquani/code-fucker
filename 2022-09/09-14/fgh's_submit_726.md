### 726
https://leetcode.com/problems/number-of-atoms/

### 难度
Hard

### 思考情况
思路比较简单 \
代码复杂 \
bug free

#### 思路
栈和哈希表 \

#### code
```cpp
class Solution {
public:
    int getIndex(string& formula, int i) {
            int n = formula.size();
            int index = 0;
            while (i + 1 < n && formula[i + 1] >= '0' && formula[i + 1] <= '9') {
                index = index * 10 + (formula[i + 1] - '0');
                i++;
            }
            index = index == 0 ? 1 : index;

            return index;
        }
        string countOfAtoms(string formula) {
            string res;
            stack<pair<string, int>> vecs;
            int n = formula.size();
            for (int i = 0; i < n; i++) {
                char c = formula[i];
                if (c >= 'A' && c <= 'Z') {
                    string name(1, c);
                    while (i + 1 < n && formula[i + 1] >= 'a' && formula[i + 1] <= 'z') {
                        name.push_back(formula[i + 1]);
                        i++;
                    }
                    int index = getIndex(formula, i);
                    vecs.push({ name, index });
                }
                else if (c == '(') vecs.push({ "(", 0 });
                else if (c == ')') {
                    int index = getIndex(formula, i);
                    vector<pair<string, int>> tmp;
                    while (!vecs.empty()) {
                        auto top = vecs.top();
                        vecs.pop();
                        if (top.first == "(") break;
                        top.second *= index;
                        tmp.push_back(top);
                    }
                    for (auto& t : tmp) vecs.push(t);
                }
            }
            map<string, int> tmpMaps;
            while (!vecs.empty()) {
                tmpMaps[vecs.top().first] += vecs.top().second;
                vecs.pop();
            }

            for (auto& tmp : tmpMaps) {
                res += tmp.first;
                if (tmp.second != 1)
                    res += std::to_string(tmp.second);
            }

            return res;
        }
};
```