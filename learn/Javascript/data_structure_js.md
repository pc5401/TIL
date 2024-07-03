# js 자료구조

- BOJ 토마토(7569)는 간단한 BFS 문제다. 근데 node.js 로 푸는데 시간초과가 나왔다. 다른 사람들은 잘 풀길래 확인해보니. 배열의 `shift()` 는 `O(n)` 의 복잡도를 가진다는 것이다. 그래서 다른 사람들은 따로 `queue` 를 구현해서 풀었다. 그 사실에 바로 정리했다.
- 자료구조는 중요하다.

### 목차
- [js 자료구조](#js-자료구조)
    - [목차](#목차)
  - [큐](#큐)
  - [스택](#스택)
  - [Deque](#deque)
  - [Min Heep](#min-heep)
  - [Max Heap](#max-heap)
  - [Linked-List](#linked-list)


## 큐
``` js
class Queue {
    constructor() {
        this.items = [];
        this.frontIndex = 0;
        this.backIndex = 0;
    }

    enqueue(item) {
        this.items[this.backIndex] = item;
        this.backIndex++;
    }

    dequeue() {
        if (this.isEmpty()) return null;
        const item = this.items[this.frontIndex];
        this.frontIndex++;
        return item;
    }

    isEmpty() {
        return this.frontIndex === this.backIndex;
    }

    size() {
        return this.backIndex - this.frontIndex;
    }
}

// 사용 예시
const queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
console.log(queue.dequeue()); // 1
console.log(queue.dequeue()); // 2
console.log(queue.isEmpty()); // true
```
## 스택
``` js
class Stack {
    constructor() {
        this.items = [];
    }

    push(item) {
        this.items.push(item);
    }

    pop() {
        if (this.isEmpty()) return null;
        return this.items.pop();
    }

    isEmpty() {
        return this.items.length === 0;
    }

    size() {
        return this.items.length;
    }
}

// 사용 예시
const stack = new Stack();
stack.push(1);
stack.push(2);
console.log(stack.pop()); // 2
console.log(stack.pop()); // 1
console.log(stack.isEmpty()); // true
```

## Deque
``` js
class Deque {
    constructor() {
        this.items = {};
        this.front = 0;
        this.back = 0;
    }

    pushFront(item) {
        if (this.isEmpty()) {
            this.pushBack(item);
        } else {
            this.front--;
            this.items[this.front] = item;
        }
    }

    pushBack(item) {
        this.items[this.back] = item;
        this.back++;
    }

    popFront() {
        if (this.isEmpty()) return null;
        const item = this.items[this.front];
        delete this.items[this.front];
        this.front++;
        return item;
    }

    popBack() {
        if (this.isEmpty()) return null;
        this.back--;
        const item = this.items[this.back];
        delete this.items[this.back];
        return item;
    }

    isEmpty() {
        return this.front === this.back;
    }

    size() {
        return this.back - this.front;
    }
}

// 사용 예시
const deque = new Deque();
deque.pushBack(1);
deque.pushFront(2);
console.log(deque.popFront()); // 2
console.log(deque.popBack()); // 1
console.log(deque.isEmpty()); // true
```

## Min Heep

``` js
class MinHeap {
    constructor() {
        this.heap = [];
    }

    insert(val) {
        this.heap.push(val);
        this.bubbleUp();
    }

    bubbleUp() {
        let index = this.heap.length - 1;
        while (index > 0) {
            let element = this.heap[index];
            let parentIndex = Math.floor((index - 1) / 2);
            let parent = this.heap[parentIndex];

            if (parent <= element) break;
            this.heap[index] = parent;
            this.heap[parentIndex] = element;
            index = parentIndex;
        }
    }

    extractMin() {
        const min = this.heap[0];
        const end = this.heap.pop();
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this.sinkDown(0);
        }
        return min;
    }

    sinkDown(index) {
        let length = this.heap.length;
        let element = this.heap[index];
        while (true) {
            let leftChildIndex = 2 * index + 1;
            let rightChildIndex = 2 * index + 2;
            let leftChild, rightChild;
            let swap = null;

            if (leftChildIndex < length) {
                leftChild = this.heap[leftChildIndex];
                if (leftChild < element) {
                    swap = leftChildIndex;
                }
            }

            if (rightChildIndex < length) {
                rightChild = this.heap[rightChildIndex];
                if ((swap === null && rightChild < element) || (swap !== null && rightChild < leftChild)) {
                    swap = rightChildIndex;
                }
            }

            if (swap === null) break;
            this.heap[index] = this.heap[swap];
            this.heap[swap] = element;
            index = swap;
        }
    }

    size() {
        return this.heap.length;
    }
}

// 사용 예시
const minHeap = new MinHeap();
minHeap.insert(3);
minHeap.insert(2);
minHeap.insert(1);
console.log(minHeap.extractMin()); // 1
console.log(minHeap.extractMin()); // 2
console.log(minHeap.size()); // 1
```

## Max Heap
```js
class MaxHeap {
    constructor() {
        this.heap = [];
    }

    insert(val) {
        this.heap.push(val);
        this.bubbleUp();
    }

    bubbleUp() {
        let index = this.heap.length - 1;
        while (index > 0) {
            let element = this.heap[index];
            let parentIndex = Math.floor((index - 1) / 2);
            let parent = this.heap[parentIndex];

            if (parent >= element) break;
            this.heap[index] = parent;
            this.heap[parentIndex] = element;
            index = parentIndex;
        }
    }

    extractMax() {
        const max = this.heap[0];
        const end = this.heap.pop();
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this.sinkDown(0);
        }
        return max;
    }

    sinkDown(index) {
        let length = this.heap.length;
        let element = this.heap[index];
        while (true) {
            let leftChildIndex = 2 * index + 1;
            let rightChildIndex = 2 * index + 2;
            let leftChild, rightChild;
            let swap = null;

            if (leftChildIndex < length) {
                leftChild = this.heap[leftChildIndex];
                if (leftChild > element) {
                    swap = leftChildIndex;
                }
            }

            if (rightChildIndex < length) {
                rightChild = this.heap[rightChildIndex];
                if ((swap === null && rightChild > element) || (swap !== null && rightChild > leftChild)) {
                    swap = rightChildIndex;
                }
            }

            if (swap === null) break;
            this.heap[index] = this.heap[swap];
            this.heap[swap] = element;
            index = swap;
        }
    }

    size() {
        return this.heap.length;
    }
}

// 사용 예시
const maxHeap = new MaxHeap();
maxHeap.insert(3);
maxHeap.insert(2);
maxHeap.insert(5);
console.log(maxHeap.extractMax()); // 5
console.log(maxHeap.extractMax()); // 3
console.log(maxHeap.size()); // 1
```

## Linked-List
- 특정 연산에서 배열 보다 링크드 리스트가 더 좋다.
  - ex. 중간에 노드 삽입 or 삭제
```js
class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    append(value) {
        const newNode = new Node(value);
        if (this.tail) {
            this.tail.next = newNode;
            this.tail = newNode;
        } else {
            this.head = newNode;
            this.tail = newNode;
        }
        this.length++;
    }

    prepend(value) {
        const newNode = new Node(value);
        if (this.head) {
            newNode.next = this.head;
            this.head = newNode;
        } else {
            this.head = newNode;
            this.tail = newNode;
        }
        this.length++;
    }

    delete(value) {
        if (!this.head) return null;

        if (this.head.value === value) {
            this.head = this.head.next;
            this.length--;
            return value;
        }

        let currentNode = this.head;
        while (currentNode.next && currentNode.next.value !== value) {
            currentNode = currentNode.next;
        }

        if (currentNode.next) {
            const deletedNode = currentNode.next;
            currentNode.next = currentNode.next.next;
            if (deletedNode === this.tail) {
                this.tail = currentNode;
            }
            this.length--;
            return value;
        }

        return null;
    }

    size() {
        return this.length;
    }
}

// 사용 예시
const list = new LinkedList();
list.append(1);
list.append(2);
list.prepend(0);
console.log(list.delete(1)); // 1
console.log(list.size()); // 2
``