### 622
https://leetcode.com/problems/design-circular-queue/

#### 思路
循环数组

#### code
```cpp
class MyCircularQueue {
public:
	MyCircularQueue(int k) {
		this->data.resize(k);
		this->cnt = 0;
		this->head = k - 1;
		this->tail = 0;
		this->size = k;
	}

	bool enQueue(int value) {
		if (this->isFull()) return false;

		this->data[this->tail] = value;
		tail = (tail + 1) % size;
		this->cnt++;

		return true;
	}

	bool deQueue() {
		if (this->isEmpty()) return false;

		head = (head + 1) % size;
		this->cnt--;

		return true;
	}

	int Front() {
		if (this->isEmpty()) return -1;
		int index = (head + 1) % size;

		return this->data[index];
	}

	int Rear() {
		if (this->isEmpty()) return -1;
		int index = (tail - 1 + size) % size;

		return this->data[index];
	}

	bool isEmpty() {
		return this->cnt == 0;
	}

	bool isFull() {
		return this->cnt == this->size;
	}
private:
	std::vector<int> data;
	int head, tail, cnt, size;
};

```