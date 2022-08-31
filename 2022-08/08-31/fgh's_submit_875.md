### 875
https://leetcode.com/problems/koko-eating-bananas/

#### 思路
二分法  \
1、left = 1 right 是piles当中最大的值\
2、二分这个值 当left == right的时候退出循环 \
3、当mid 值能使得吃完piles mid值是有效的 更小的值再左侧 right = mid \
4、如果mid是无效的 说明结果有效的最小值再右侧 left = mid + 1

#### code
```cpp
bool judgeValid(vector<int> &nums, int h, int k) {
        for (int num : nums){
            h -= (num / k);
            if (num % k != 0) h--;
            if (h < 0) return false;
        }
        
        return true;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1, right = *max_element(piles.begin(), piles.end());
        while(left < right) {
            int mid = left+ (right - left) / 2;
            if (judgeValid(piles, h, mid)) right = mid;
            else left = mid + 1;
        }
        
        return left;
    }
```