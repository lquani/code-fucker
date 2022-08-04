## 557
https://leetcode.com/submissions/detail/764845939/

#### 思路
双指针法; \
p1指向单个str的开始 p2指向结尾 \
然后交换p1 p2

#### code
```cpp
string reverseWords(string s) {
	int n = s.length(); 
	for (int p1 = 0; p1 < n; p1++) {
		if (s[p1] == ' ') continue;
		int p2 = p1;
		while (!(p2 + 1 == n || s[p2+1] == ' ')) p2++;
    
		int end = p2;
		while (p1 <= p2) swap(s[p1++], s[p2--]);

		p1 = end;
	}

	return s;
}
```

## 611
https://leetcode.com/problems/valid-triangle-number/

#### 思路
二分搜索 \
有效的三角形:两个较短的边相加 严格< 更长的那边边 \
对数组进行排序\
分别对i j 进行遍历,二分搜索 j ~ n-1 有序数组当中严格小于target的个数

#### code
```cpp
int triangleNumber(vector<int>& nums) {
	int res = 0, n = nums.size();
	sort(nums.begin(), nums.end());

	for (int i = 0; i <= n - 3; i++) {
		//if (i >= 1 && nums[i] == nums[i - 1]) continue;
		for (int j = i + 1; j <= n - 2; j++) {
			//if (j > i + 1 && nums[j] == nums[j - 1]) continue;

			int target = nums[i] + nums[j];
			//! < 二分搜索 j ~ n-1 有序数组当中严格小于target的个数
			int left = j + 1, right = n - 1;
			while (left <= right) {
				int mid = left + (right - left) / 2;
				if (nums[mid] >= target) right = mid - 1;
				else left = mid + 1;
			}

			res += (right - (j + 1) + 1);
		}
	}

	return res;
}
```

## 443
https://leetcode.com/problems/string-compression/

#### 思路
双指针法 \
pCur 指向当前存放新字符串的位置,pNext指向一个字符串结束位置,cnt代表当前字符串个数,默认为1

#### code
```cpp
int compress(vector<char>& chars) {
	int n = chars.size();
	if (n <= 1) return n;
	
	int pCur = 0, pNext = 0, cnt = 1;
	while (pNext < n) {
		if (pNext + 1 < n && chars[pNext + 1] == chars[pNext]) {
			pNext++;
			cnt++;
		}
		else {
			char c = chars[pNext];
			chars[pCur++] = c;
			if (cnt > 1) {
				std::string cntStr = std::to_string(cnt);
				int p = 0;
				for (int i = 0; i < cntStr.size(); i++)
					chars[pCur++] = cntStr[i];
			}

			cnt = 1;
			pNext++;	
		}
	}

	return pCur;
}

```






