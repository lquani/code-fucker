### 133
https://leetcode.com/problems/clone-graph/

### 难度
Medium

### 思考情况
思路正确 \
数据结构错误 \
bug free

#### 思路
广度优先搜索 \
unordered_map<Node*, Node*> visited key 表示原本的节点 值表示的是克隆的值

#### code
```cpp
Node* cloneGraph(Node* node) {
        if (node == NULL) return NULL;
        unordered_map<Node*, Node*> visited;
        queue<Node*> vecs;
        visited[node] = new Node(node->val);
        vecs.push(node);
        
        while (!vecs.empty()) {
            Node *curNode = vecs.front();
            vecs.pop();
            
            for (Node *n : curNode->neighbors) {
                if (visited.find(n) == visited.end()) {
                    visited[n] = new Node(n->val);
                    vecs.push(n);
                }
                visited[curNode]->neighbors.push_back(visited[n]);
            }
        }
        return visited[node];
    }
```