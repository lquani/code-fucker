### 71
https://leetcode.com/problems/simplify-path/

#### 思路
栈 \
按照 / 分割字符串 并且入栈 \
遇到..则出栈

#### code
```cpp
string simplifyPath(string path) {
		std::string res;
		stack<std::string> vecs;
		if (!path.empty() && path.back() == '/')
			path.push_back('/');

		for (int i = 0; i < path.size(); i++) {
			std::string tmp;
			while (i < path.size() && path[i] != '/') tmp.push_back(path[i++]);
			if (tmp.empty() || tmp == ".") continue;

			vecs.push(tmp);
		}

		int upFolderNum = 0;
		while (!vecs.empty()) {
			if (vecs.top() == "..") {
				upFolderNum++;
				vecs.pop();
				continue;
			}

			if (upFolderNum != 0) {
				vecs.pop();
				upFolderNum--;
				continue;
			}

			
			res = vecs.top() + (res.empty() ? "" : ("/" + res));
			vecs.pop();
		}

		return "/" + res;
	}
```

