### 994
https://leetcode.com/problems/rotting-oranges/

### 难度
Medium

### 思考情况
思路正确 \
bug free

#### 思路
广度优先搜索 

#### code
```cpp
void addCurNode(vector<vector<int>> &grid, queue<pair<int, int>> &vecs, int row, int col, int &okNum) {
        int m = grid.size(), n = grid[0].size();
        if (row < 0 || col < 0 || row >= m || col >= n) return;
        int data = grid[row][col];
        if (data == 0 || data == 3) return;
        if (data == 1) okNum--;
        grid[row][col] = 3;
        vecs.push({row, col});
    }
    int orangesRotting(vector<vector<int>>& grid) {
        int okNum = 0, time = 1, m = grid.size(), n = grid[0].size();
        queue<pair<int, int>> vecs;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) okNum ++;
                else if (grid[i][j] == 2) {
                    vecs.push({i, j});
                    grid[i][j] = 3;
                }
            }
        }
        
        if (okNum == 0) return 0;
        while (!vecs.empty()) {
            int size = vecs.size();
            for (int i = 0; i < size; i++) {
                int row = vecs.front().first, col = vecs.front().second;
                vecs.pop();
                
                addCurNode(grid, vecs, row - 1, col, okNum);
                addCurNode(grid, vecs, row + 1, col, okNum);
                addCurNode(grid, vecs, row, col - 1, okNum);
                addCurNode(grid, vecs, row, col + 1, okNum);
                if (okNum <= 0) return time;
            }
            time++;
        }
        
        return -1;
    }
```