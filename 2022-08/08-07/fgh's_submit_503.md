### 503
https://leetcode.com/problems/next-greater-element-ii/

#### 思路
单调栈 \
维持一个递减的栈 \
遍历当前数,如果严格小于等于栈顶元素,就入栈 \
否则出栈,并且出栈的部分更新结果 \ 
需要注意的是,最后遍历结束 栈内的元素,因为这是个循环的数组

#### code
```cpp
vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, -1);
        stack<pair<int, int>> vecs;
        
        for (int i = 0; i < n; i++) {
            if (vecs.empty() || nums[i] <= vecs.top().first) {
                vecs.push({nums[i], i});
                continue;
            }
            
            while (!vecs.empty() && nums[i] > vecs.top().first) {
                int index = vecs.top().second;
                res[index] = nums[i];
                vecs.pop();
            }
            vecs.push({nums[i], i});
        }
        
        for (int i = 0; i < n; i++) {
            if (vecs.empty()) break;
            if (nums[i] <= vecs.top().first) continue;
            
            while (!vecs.empty() && nums[i] > vecs.top().first) {
                res[vecs.top().second] = nums[i];
                vecs.pop();
            }
        }
        return res;
    }
```