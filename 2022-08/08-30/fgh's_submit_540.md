### 540
https://leetcode.com/problems/single-element-in-a-sorted-array/

#### 思路
二分法 \
1、二分,计算mid的左右值,判断mid是单个值的话直接返回\
2、如果mid是双值,确保mid是两个值的右边那个\
3、分别计算mid左右两边值的个数,如果左边是奇数 right = mid - 2; 如果右边是奇数 left = mid + 1; \
4、退出循环:left = right ; 考虑mid 右边只有right一个值的时候,left = mid + 1。这个时候left = right。这个时候再循环是没有意义的,所以可以直接退出

#### code
```cpp
 int singleNonDuplicate(vector<int>& nums) {
        int n = nums.size();
        int left = 0, right = n - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (mid == n-1 && nums[mid-1] != nums[mid]) return nums[mid];
            if (mid == 0 && nums[mid] != nums[mid+1]) return nums[mid];
            if (nums[mid] != nums[mid-1] && nums[mid] != nums[mid+1]) return nums[mid];
            
            if (mid + 1 < n && nums[mid+1] == nums[mid]) mid = mid + 1;
            int leftNum = mid - left + 1;
            int rightNum = right - mid;
            if (leftNum % 2 == 1) right = mid - 2;
            else if (rightNum % 2 == 1) left = mid + 1;
        }
        
        return nums[left];
    }

```
