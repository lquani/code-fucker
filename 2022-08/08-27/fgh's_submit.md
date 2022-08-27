### 523
https://leetcode.com/problems/continuous-subarray-sum/

#### 思路
我们令 b = x * k + r1b=x∗k+r1,a = y * k + r2a=y∗k+r2,那么 r1r1 和 r2r2 分别为 bb 和 aa 模 kk 的值。

即有: b - a = (x * k + r1) - (y * k + r2) =(x - y) * k + (r1 - r2)b−a=(x∗k+r1)−(y∗k+r2)=(x−y)∗k+(r1−r2)。

由 b - ab−a 为 kk 的倍数,可以推导出 r1 = r2r1=r2,即 bb 和 aa 模 kk 相同

#### code
```cpp
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        if (n < 2) return false;
        unordered_map<int, int> maps;
        maps[0] = 0;
        
        for (int i = 1; i < n; i++) {
            nums[i] += nums[i-1];
            if (i >= 2)
                maps[nums[i-2] % k] = 0;
            if (maps.find(nums[i] % k) != maps.end())
                return true;
        } 
        
        return false;
    }
};
```
