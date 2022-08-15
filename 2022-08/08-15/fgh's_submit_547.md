### 547
https://leetcode.com/problems/number-of-provinces/

#### 思路
无向图 \
1、深度优先搜索 \
2、广度优先搜索 \
都需要一个isVisited数组,判断节点是否访问过. \
广度优先搜索需要一个queue

#### code
1、 \
```cpp
void helper(vector<vector<int>>& isConnected, vector<bool> &isVisited, int city) {
	int m = isConnected.size();
	isVisited[city] = true;
	for (int i = 0; i < m; i++) {
		if (!isConnected[city][i] || isVisited[i]) continue;
		isVisited[i] = true;
		helper(isConnected, isVisited, i);
	}
}
int findCircleNum(vector<vector<int>>& isConnected) {
	int m = isConnected.size();
	if (m == 0) return 0;
	int res = 0;
	vector<bool> isVisited(m, false);
	for (int i = 0; i < m; i++) {
		if (isVisited[i]) continue;
		helper(isConnected, isVisited, i);
		res++;
	}

	return res;
}
```

2、\
```cpp
int findCircleNum(vector<vector<int>>& isConnected) {
	int m = isConnected.size();
	if (m == 0) return 0;
	vector<int> isVisited(m, false);
	queue<int> ques;
	int res = 0;
	for (int i = 0; i < m; i++) {
		if (isVisited[i]) continue;
		ques.push(i);
		while (!ques.empty()) {
			int city = ques.front();
			ques.pop();
			isVisited[city] = true;
			for (int k = 0; k < m; k++) {
				if (!isConnected[city][k] || isVisited[k]) continue;
				ques.push(k);
			}
		}
		res++;
	}

	return res;
}


```