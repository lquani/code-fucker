### 334

#### 思路
贪心\
使得 1 2 个数最小

#### code
```cpp
bool increasingTriplet(vector<int>& nums) {
	int n = nums.size();
	if (n < 3) return 0;
	
	int first = nums[0], second = INT_MAX;
	for (int i = 1; i < nums.size(); i++) {
		int num = nums[i];
		if (num > second) return true;
		else if (num < second && num > first) second = num;
		else if (num < first) first = num;
	}

	return false;
}
```