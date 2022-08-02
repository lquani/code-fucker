### 400
https://leetcode.com/problems/nth-digit/submissions/

#### 思路
统计数字 主要是要注意下标-1

#### code
```cpp
int findNthDigit(int n) {
            int k = 10;
            std::vector<long> nums;
            for (int i = 0; i < 10; i++) {
                long num = (i + 1) * 9 * pow(10, i);
                nums.push_back(num);
            }

            //! < 确定n的位数
            long i = 0, preSum = 0;
            for (; i < 10; i++) {
                preSum += nums[i];
                if (preSum >= n) break;
            }
            preSum -= nums[i];

            int next = n - preSum - 1;
            long start = pow(10, i);
            start += (next / (i + 1));

            int index = next % (i + 1);
            index = i + 1 - index;

            for (int j = 0; j < index - 1; j++) start /= 10;

            return start % 10;
        }

```