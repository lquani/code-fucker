### 208

### 题目链接
https://leetcode.com/problems/implement-trie-prefix-tree/

### 思路
前缀树  \
### code
```cpp
class Trie {
private:
    vector<Trie*> children;
    bool isEnd;
public:
    Trie() {
        this->children.resize(26);
        this->isEnd = false;
    }

    void insert(string word) {
        Trie *node = this;
        for (char c : word) {
            int index = c - 'a';
            if (node->children[index] == NULL)
                node->children[index] = new Trie();
            node = node->children[index];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        Trie *node = this;
        for (char c : word) {
            int index = c - 'a';
            if (node->children[index] == nullptr) return false;
            node = node->children[index];
        }

        return node != NULL && node->isEnd;
    }

    bool startsWith(string prefix) {
        Trie *node = this;
        for (char c : prefix) {
            int index = c - 'a';
            if (node->children[index] == nullptr) return false;
            node = node->children[index];
        }

        return node != nullptr;
    }
};
```