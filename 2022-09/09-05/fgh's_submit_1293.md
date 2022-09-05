### 1293. Shortest Path in a Grid with Obstacles Elimination
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

### 难度
Hard

### 思考情况
广度搜索 \
具体情况:没思考完全\
代码:bug free 

#### 思路
广度搜索 \
每次消除一个障碍之后,需要保留当前的网格结构 \

#### code
```cpp
struct status {
        int x, y, k;
        status(int x_, int y_, int z_) : x(x_), y(y_), k(z_) { }
    };
    int shortestPath(vector<vector<int>>& grid, int k) {
        int res = 1;
        queue<status> vecs;
        vecs.push(status(0, 0, k));
        int m = grid.size(), n = grid[0].size();
        if (m== 1 && n == 1) return 0;
        vector<vector<vector<bool>>> visited(m, vector<vector<bool>>(n, vector<bool>(k + 1, false)));
        visited[0][0][k] = true;
        vector<vector<int>> maps{{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
        while (!vecs.empty()) {
            int size = vecs.size();
            for (int i = 0; i < size; i++) {
                auto pos = vecs.front();
                vecs.pop();
                for (int j = 0; j < 4; j++) {
                    int cx = pos.x + maps[j][0];
                    int cy = pos.y + maps[j][1];
                    if (!(cx >= 0 && cy >= 0 && cy < m && cx < n)) continue;
                    
                    if (grid[cy][cx] == 0 && !visited[cy][cx][pos.k]) {
                        if (cx == n-1 && cy == m-1) return res;
                        
                        visited[cy][cx][pos.k] = true;
                        vecs.push(status(cx, cy, pos.k));
                    } else if (grid[cy][cx] == 1 && pos.k > 0 && !visited[cy][cx][pos.k-1]) {
                        vecs.push(status(cx, cy, pos.k-1));
                        visited[cy][cx][pos.k-1] = true;
                    }
                }
            }
            res++;
                     
        }
        return -1;
    }
```