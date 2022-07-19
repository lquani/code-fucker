```cpp
class Solution {
public:
     int findKthLargest(vector<int>& nums, int k) {
        if(nums.empty()) return 0;
        priority_queue<int, vector<int>, greater<>> p;
        for(int i = 0; i < k; i++) p.push(nums[i]);
        for(int i = k; i < nums.size();i++){
            int val = p.top();
            if(nums[i] > val){
                p.pop();
                p.push(nums[i]);
            }
        }
        return p.top();
    }
};

```