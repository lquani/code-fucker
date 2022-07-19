### 440
https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

#### 思路
字典数  \
![](https://github.com/lquani/code-fucker/blob/main/001image/442-1.png) \
相当于对一个10叉树进行前序遍历  \
countNodes 计算 cur下 <= n的节点数目  \
1、如果n 属于cur所在层的数,计算的当前层的节点就是 n - cur + 1  \
2、如果n 不在cur所在层 当前层的节点都加入 next - cur  \

如果计算出的节点数目 不够 k cur当前node不够 往cur右侧走  \
如果计算出的节点数目 够K了 说明结果在cur的子树当,cur向下走 \

#### code
```cpp
int findKthNumber(int n, int k) {
        long cur = 1;
        k --;
        
        while (k > 0) {
            int nodes = countNodes(n, cur); // ! < 计算cur下有多少个 < n的节点应该被包含
            if (k >= nodes) { //! cur当前node不够 往cur右侧走
                k -= nodes;
                cur = cur + 1;
            } else { //! cur当前node包含了k 往cur下层走
                k--;
                cur *= 10;    
            }
        }
        
        return (int) cur;
    }
    
    int countNodes(int n, long cur) {
        long total = 0;
        long next = cur + 1;
        
        while (cur <= n) {
            total += min(n - cur + 1, next - cur); 
            //! < n - cur + 1: n 包含在cur层
            //! < next - cur: n 不包含在cur的曾 cur这一层是所有的子树都可以计入
            cur *= 10;
            next *= 10;
        }
        
        return (int)total;   
    }

```

### 629

https://leetcode.com/problems/k-inverse-pairs-array/

#### 思路:
动态规划,。但是超时...


#### code
```cpp

 int kInversePairs(int n, int k) {
        int M = 1000000007;
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
        dp[0][0] = 1;
        for (int i = 1; i <= n; ++i) {
            dp[i][0] = 1;
            for (int j = 1; j <= k; ++j) {
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % M;
                if (j >= i) {
                    dp[i][j] = (dp[i][j] - dp[i - 1][j - i] + M) % M;
                }
            }
        }
        return dp[n][k];
    }
```

