### 581. Shortest Unsorted Continuous Subarray
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

### 难度
Medium

### 思考情况
思路正确 \
bug free

#### 思路
双指针法 \

left 从左往右,找一个降序的位置 \
right 从右往左, 找一个升序的位置 \

找left - right 当中最大值和最小值 \
从left和right分别找nums[left] <= mn 和 nums[right] 》= mx 

#### code
```cpp
int findUnsortedSubarray(vector<int>& nums) {
        int left = 0, n = nums.size(), right = n - 1;
        for (; left < n - 1; left++) {
            if (nums[left] > nums[left+1]) break;
        }
        if (left == n - 1) return 0;
        for (; right > 0; right--) {
            if (nums[right] < nums[right-1]) break;
        }
        if (right == 0) return n;
        int mx = INT_MIN, mn = INT_MAX;
        for (int i = left; i <= right; i++) {
            mx = max(mx, nums[i]);
            mn = min(mn, nums[i]);
        }
        
        for (left--; left >= 0; left--) {
            if (nums[left] <= mn) break;
        }
        for (right++; right < n; right++) {
            if (nums[right] >= mx) break;
        }
        
        return right - left - 1;
    }
```