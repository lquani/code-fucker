### 946
#### 题目链接
https://leetcode.com/problems/validate-stack-sequences/

#### 思路
easy

#### code
```cpp
bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
	int m = pushed.size(), n = popped.size();
	stack<int> vecs;
	for (int i = 0, j = 0; i < m && j < n; i++) {
		vecs.push(pushed[i]);
		while (!vecs.empty() && vecs.top() == popped[j]) {
			vecs.pop();
			j++;
		}
	}

	return vecs.empty();
}

```

### 307

#### 题目链接
https://leetcode.com/problems/range-sum-query-mutable/

#### 思路

线段树:  fenwick tree  \
![](https://github.com/lquani/code-fucker/blob/main/001image/fenwick_tree.jpg) 
上图所示;以最后一个节点作为主节点,将vector {1, 2, 3, 4, 5, 6, 7, 8}平均分到两个数,这样构建节点;  \
每个节点的值是 当前节点子节点的累加和 \

#### code
```cpp
class NumArray {
public:
	class FenwickTree {
	public:
		FenwickTree(int n) : sums(n + 1, 0) {

		}
		void upDate(int i, int val) {
			while(i < sums.size()) {
				sums[i] += val;
				i += this->lowBit(i);
			}
		}
		int query(int i) {
			int sum = 0;
			while (i > 0) {
				sum += sums[i];
				i -= this->lowBit(i);
			}
			return sum;
		}
	private:
		int lowBit(int i) { return i & (-i); }
		std::vector<int> sums;
	};

	NumArray(vector<int>& nums) {
		this->nums = nums;
		tree = new FenwickTree(nums.size());
		for (int i = 0; i < nums.size(); i++)
			tree->upDate(i + 1, nums[i]);
	}

	void update(int index, int val) {
		tree->upDate(index + 1, val - nums[index]);
		nums[index] = val;
	}

	int sumRange(int left, int right) {
		return tree->query(right + 1) - tree->query(left);
	}
	FenwickTree *tree;
	std::vector<int> nums;
};
```
