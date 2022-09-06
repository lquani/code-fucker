### 312 
https://leetcode.com/problems/burst-balloons/

### 难度
Hard

### 思考情况
x想不出来 \
bug free

#### 思路
分治法 \
以 k 将 问题分解为(i , k) (k, j) 其中都是开区间

#### code
```cpp
int maxCoinsT(vector<int> &nums, vector<vector<int>> &cache, int start, int end) {
        if (start == end-1) return 0;
        if (cache[start][end] != 0) return cache[start][end];
        int mx = 0;
        for (int i = start + 1; i < end; i++) {
            int tmp = maxCoinsT(nums, cache, start, i) + 
                maxCoinsT(nums, cache, i, end) + nums[i] * nums[start] * nums[end];
            mx = max(mx, tmp);
        }
        cache[start][end] = mx;
        
        return mx;
    }
    int maxCoins(vector<int>& nums) {
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        int n = nums.size();
        vector<vector<int>> cache(n, vector<int>(n, 0));
        
        return maxCoinsT(nums, cache, 0, n - 1);
    }
```