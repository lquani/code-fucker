### 670
https://leetcode.com/problems/maximum-swap/


#### 思路
双指针法 \
将数字转换成数组 \
posMin 指向高位当中的最小值 posMax 指向低位当中的最大值 \
mx 指向低位当中最大值的位置

#### code
```cpp
int maximumSwap(int num) {
        std::string str = std::to_string(num);
        int n = str.size();
        int posMin = -1, posMax = -1, mx = n-1;
        for (int i = n - 2; i >= 0; i--) {
            if (str[i] < str[mx]) {
                posMin = i; 
                posMax = mx;
            } else {
                mx = i;
            }
        }
        if (posMin != -1) swap(str[posMin], str[posMax]);
        
        return stoi(str);
    }
    
```