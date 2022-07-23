### 153
#### 题目链接
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

#### 思路
方法: 二分搜索  \
一个升序数组,经过0此旋转 或者 k此旋转  \
![](https://github.com/lquani/code-fucker/blob/main/001image/153.png)  \
有两种情况: \
1、没有保持原有的升序 2、保持不变 \
第二种情况:直接返回left就是最小值 \
第一种情况: 看mid的情况,如果>=left 说明结果处于右侧,left左侧收缩  \
如果 < right (不可能会等于right 结果右侧收缩

#### code
```cpp
int findMin(vector<int>& nums) {
        int n = nums.size(), left = 0, right = n-1;
        
        if (n == 1) return nums[0];
        while (left < right) {
            if (nums[left] < nums[right]) return nums[left];
            
            int mid = left + (right - left) / 2;
            if (nums[mid] >= nums[left]) left = mid + 1;
            else if (nums[mid] < nums[right]) right = mid; 
        }
        
        
        return nums[left];
    }
```

### 1539
#### 题目链接
https://leetcode.com/problems/kth-missing-positive-number/

#### 思路
用res来计算,当前点为止,缺少了多少个数。 \
如果是第一个数,res = arr[0]-1; \
如果不是 res += (arr[i]-arr[i-1]-1) \
通过判断res的状态来决定返回结果\
1、res=k 直接返回当前值-1\
2、res < k 继续遍历\
3、res > k 返回当前值-1-(res-k) k包含在res结果当中了\
如果遍历完没有返回 说明缺失的是当前数组后续的数字

#### code
```cpp
int findKthPositive(vector<int>& arr, int k) {
        int res = 0;
        
        for (int i = 0; i < arr.size(); i++) {
            if (i == 0) res += (arr[0]-1);
            else res += (arr[i] - arr[i-1] - 1);
            
            if (res == k) return arr[i]-1;
            else if (res < k) continue;
            else return arr[i]-(res-k)-1;
        }
        
        return arr.back()+k-res;
    }
```