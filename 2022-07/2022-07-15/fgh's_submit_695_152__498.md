### 695
#### 链接
https://leetcode.com/problems/max-area-of-island/
#### 思路
深度优先搜索

#### code
```cpp
class Solution {
public:
    void helper(vector<vector<int>>& grid, int row, int col, int &tmp) {
      int m = grid.size(), n = grid[0].size();
      if (row < 0 || row >= m || col < 0 || col >= n || grid[row][col] == 0) return;

      grid[row][col] = 0;
      tmp++;
      helper(grid, row-1, col, tmp);
      helper(grid, row+1, col, tmp);
      helper(grid, row, col-1, tmp);
      helper(grid, row, col+1, tmp);
  }
  int maxAreaOfIsland(vector<vector<int>>& grid) {
      int res = 0, m = grid.size(), n = grid[0].size();

      for (int i = 0; i < m; i++) {
          for (int j = 0; j < n; j++) {
              if (grid[i][j] == 0) continue;

              int tmp = 0;
              helper(grid, i, j, tmp);
              res = max(res, tmp);
          }
      }

      return res;
  }
};
```


### 152

#### 链接
https://leetcode.com/problems/maximum-product-subarray/

#### 思路
动态规划:两个数 分别代表负数最小 正数最大

#### code

```cpp
class Solution {
public:
   int maxProduct(vector<int>& nums) {
    int m = nums.size();
    vector<int> dp_neg(m, 0);
    vector<int> dp_pos(m, 0);
    dp_neg[0] = nums[0];
    dp_pos[0] = nums[0];
    int res = nums[0];
    for (int i = 1; i < m; i++) {
        int tmp1 = max(max(dp_neg[i-1]*nums[i], dp_pos[i-1]*nums[i]), nums[i]);
        int tmp2 = min(min(dp_neg[i-1]*nums[i], dp_pos[i-1]*nums[i]), nums[i]);
        dp_neg[i] = tmp2;
        dp_pos[i] = tmp1;
        res = max(res, max(tmp1, tmp2));
    }
    
    return res;
}

};

```

### 498

#### 链接
https://leetcode.com/submissions/detail/747548775/

#### 思路
递归搜索  \
direction 控制在col = 0 row = m -1 row = 0 col = n-1处转向  \
分别在从坐下 和 右上遍历

#### code

```cpp

class Solution {
public:
    void helper(vector<vector<int>>& mat, vector<int> &res, int row, int col, bool direction) {
            int m = mat.size(), n = mat[0].size();
            if (col < 0 || row >= m || row < 0 || col >= n) return;
            if (direction && (col == 0 || row == m-1)) {
                res.push_back(mat[row][col]);
                if (row == m-1)
                    helper(mat, res, row, col + 1, !direction);
                else
                    helper(mat, res, row+1, col, !direction);
                return;
            }
            if (!direction && (row == 0 || col == n-1)) {
                res.push_back(mat[row][col]);
                if (col == n-1)
                    helper(mat, res, row + 1, col, !direction);
                else
                    helper(mat, res, row, col + 1, !direction);
                return;
            }

            res.push_back(mat[row][col]);
            if (direction)
                helper(mat, res, row+1, col-1, direction);
            else
                helper(mat, res, row-1, col+1, direction);

    }
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        vector<int> res;
        helper(mat, res, 0, 0, false);

        return res;
    }
};
```
