### 207
https://leetcode.com/problems/course-schedule/

#### 思路
图的遍历

#### code
```cpp
bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
	vector<vector<int>> graphs(numCourses);
	vector<int> preNum(numCourses);

	//! build graph
	for (auto & nums : prerequisites) {
		int first = nums[1];
		int second = nums[0];
		graphs[first].push_back(second);
		preNum[second]++;
 	}

	//! build queue
	queue<int> nodes;
	for (int i = 0; i < preNum.size(); i++) {
		if (preNum[i] == 0) nodes.push(i);
	}

	while (!nodes.empty()) {
		int first = nodes.front();
		nodes.pop();
		for (int second : graphs[first]) {
			preNum[second]--;
			if (preNum[second] == 0)
				nodes.push(second);
		} 
	}

	//! check result
	for (int i = 0; i < numCourses; i++) {
		if (preNum[i] != 0) return false;
	}

	return true;
}

```

### 7
https://leetcode.com/problems/palindrome-number/

#### 思路
反转后一半的数字 比大小
#### code
```cpp
bool isPalindrome(int x) {
    if (x == 0) return true;
	if (x < 0 || x % 10 == 0) return false;
	if (x < 10) return true;
	
	int right = 0;
	while (x > right) {
		right = right * 10 + x % 10;
		x /= 10;
	}
	return x == right || right / 10 == x;

}
```