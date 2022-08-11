### 674
https://leetcode.com/problems/longest-continuous-increasing-subsequence/submissions/

#### 思路
滑动窗口 \

#### code
```cpp
int findLengthOfLCIS(vector<int>& nums) {
        int res = 1;
        int p1 = 0, p2 = 0, n = nums.size();
        while (p2 < n && p1 <= p2) {
            if (p2+1 < n && nums[p2+1] > nums[p2]) p2++;
            else {
                p1 = p2+1;
                p2 = p1;
            }
            res = max(res, p2 - p1 + 1);
        }
        
        return res;
    }
```