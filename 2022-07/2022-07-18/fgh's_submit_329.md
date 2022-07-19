### 329
#### 题目链接
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

#### 思路
题目意思:再一个矩形当中寻找一个最长的递增序列  \
方法:1、直接用深度搜索,会出现超时  \
2、搜索记忆法:使用数组vector<vector<int>>& num  \
  记录(i, j)位置是否计算过了;如果计算过了 直接用这个值  \
  不需要重复递归搜索
  
 #### code
 
 ```cpp
int helper(vector<vector<int>>& num, vector<vector<int>>& matrix, int row, int col, int pre) {
    int m = matrix.size(), n = matrix[0].size();

    if (row < 0 || row == m || col < 0 || col >= n || matrix[row][col] <= pre) return 0;
    if (num[row][col] != 0) return num[row][col];

    pre = matrix[row][col];
    num[row][col] ++;
    int up = helper(num, matrix, row - 1, col, pre);
    int down = helper(num, matrix, row + 1, col, pre);
    int left = helper(num, matrix, row, col - 1, pre);
    int right = helper(num, matrix, row, col + 1, pre);

    num[row][col] = max(max(max(left + 1, right + 1), max(up + 1, down + 1)), num[row][col]);

    return num[row][col];
}


int longestIncreasingPath(vector<vector<int>>& matrix) {
    int res = 0;
    int m = matrix.size(), n = matrix[0].size();
    vector <vector<int>> num(m, vector<int>(n, 0));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            res = max(res, helper(num, matrix, i, j, -1));
        }
    }

    return res;
}

  
 ```