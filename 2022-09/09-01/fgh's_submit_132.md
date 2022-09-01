### 132
https://leetcode.com/problems/132-pattern/

### 难度
hard

### 思考情况
看了部分思路 \
代码自己写的

#### 思路
单独栈 \
1、单独栈维护的是 3 个值当中最大的那个值 \
2、k 维护的是三个值第二小的值 \
3、从后往前遍历,如果当前的值大于栈顶的元素,需要把栈内元素出栈,并且更新K的值

#### code
```cpp
bool find132pattern(vector<int>& nums) {
        stack<int> vecs;
        int k = INT_MIN, n = nums.size();
        for(int i = n - 1; i >= 0; i--) {
            if (nums[i] < k) return true;
            
            while (!vecs.empty() && nums[i] > vecs.top()) {
                k = max(k, vecs.top());
                vecs.pop();
            }
            
            vecs.push(nums[i]);
        }
        return false;
    }
```
