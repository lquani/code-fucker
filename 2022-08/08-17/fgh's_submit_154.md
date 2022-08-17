### 154
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

#### 思路
二分法 \
主要是要注意边界 \
while (left < right) : 结束循环 left == right \

#### code
```cpp
int findMin(vector<int>& nums) {
	int n = nums.size();
	if (n <= 1) return nums.back();
	if (nums[0] < nums.back()) return nums[0];

	int left = 0, right = n - 1;
	while (left < right) {
		int mid = left + (right - left) / 2;
		if (nums[mid] > nums[right])
			left = mid + 1;
		else if (nums[mid] < nums[right])
			right = mid;
		else
			right -= 1;
	}

	return nums[left];
}

```