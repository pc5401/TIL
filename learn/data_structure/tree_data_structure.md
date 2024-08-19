
# 트리(Tree Data Structure)

트리는 자식 노드와 부모 노드로 이루어진 계층적인 구조를 가지며, 무방향 그래프의 일종이자 사이클이 없는 자료구조이다. 트리는 그래프의 한 유형으로, 다음과 같은 특징을 가진다.

## 트리의 특징

1. **부모, 자식 계층 구조**: 트리는 부모와 자식 노드 간의 계층 구조를 가진다. 예를 들어, 5번 노드는 6번 노드와 7번 노드의 부모 노드이고, 6번 노드와 7번 노드는 5번 노드의 자식 노드이다. 어떤 노드보다 위에 있는 노드는 부모, 아래에 있는 노드는 자식 노드로 불린다.

2. **V - 1 = E**: 트리의 간선 수는 노드 수에서 1을 뺀 값과 같다. 즉, 간선의 수는 노드 수 - 1이다.

3. **유일한 경로**: 임의의 두 노드 사이의 경로는 유일하게 존재한다. 트리 내의 어떤 노드에서 다른 노드까지의 경로는 반드시 하나만 존재하며, 이 경로는 중복되지 않는다.

## 트리의 기본 요소

- **루트 노드 (Root Node)**: 트리의 가장 위에 있는 노드를 의미한다. 트리를 탐색할 때는 보통 루트 노드를 중심으로 시작하면 문제가 쉽게 풀리는 경우가 많다.
  
- **내부 노드 (Internal Node)**: 루트 노드와 리프 노드 사이에 있는 노드를 의미한다.
  
- **리프 노드 (Leaf Node)**: 자식 노드가 없는 노드를 의미한다. 예를 들어, 최종적인 데이터나 끝에 위치한 노드들이 리프 노드에 해당한다.

## 트리의 높이와 레벨

- **깊이 (Depth)**: 트리에서 깊이는 각각의 노드마다 다르며, 루트 노드에서 특정 노드까지 최단 거리로 갔을 때의 거리를 의미한다. 예를 들어, 4번 노드의 깊이는 2이다.

- **높이 (Height)**: 트리의 높이는 루트 노드부터 리프 노드까지의 거리 중 가장 긴 거리를 의미하며, 트리의 전체 높이를 나타낸다.

- **레벨 (Level)**: 트리의 레벨은 노드가 트리 내에서 어느 위치에 있는지를 나타내며, 보통 깊이와 같은 의미로 사용된다. 예를 들어, 루트 노드를 1레벨이라고 하면, 그 다음 노드들은 2레벨이 된다.

- **서브트리 (Subtree)**: 트리 내의 하위 집합을 서브트리라고 한다. 이는 트리의 일부로, 특정 노드를 루트로 하는 작은 트리 구조이다.

## 숲(Forest)
- 트리로 이루어진 집합을 숲(forest)이라고 한다.

## 이진 트리와 이진 탐색 트리

트리의 한 유형인 이진 트리는 각 노드가 자식 노드를 최대 두 개까지 가질 수 있는 트리이다. 이진 트리는 다음과 같이 분류된다:

- **정이진 트리 (Full Binary Tree)**: 자식 노드가 0개 또는 2개인 이진 트리를 의미한다.

- **완전 이진 트리 (Complete Binary Tree)**: 모든 레벨이 완전히 채워져 있으며, 마지막 레벨만 부분적으로 채워진 이진 트리를 의미한다. 마지막 레벨은 왼쪽에서 오른쪽으로 채워진다.

- **변질 이진 트리 (Degenerate Binary Tree)**: 각 노드가 자식 노드를 하나씩만 가지는 이진 트리를 의미한다. 이 트리는 선형적인 구조로, 사실상 연결 리스트와 유사하다.

- **포화 이진 트리 (Perfect Binary Tree)**: 모든 노드가 꽉 차 있는 이진 트리를 의미하며, 모든 레벨이 완전히 채워져 있다.

- **균형 이진 트리 (Balanced Binary Tree)**: 모든 노드의 왼쪽 하위 트리와 오른쪽 하위 트리의 높이 차이가 1 이하인 트리를 의미한다. 예를 들어, C++의 `map`과 `set`은 균형 이진 트리인 레드-블랙 트리를 기반으로 구현되어 있다.

### 예시 코드 (C++)

```cpp
#include <iostream>
#include <queue>
using namespace std;

// 노드 구조체 정의
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int value) : data(value), left(NULL), right(NULL) {}
};

// 트리의 루트 노드부터 레벨 순서로 출력 (너비 우선 탐색)
void printLevelOrder(Node* root) {
    if (root == NULL) return;

    queue<Node*> q;
    q.push(root);

    while (!q.empty()) {
        Node* current = q.front();
        q.pop();
        cout << current->data << " ";

        if (current->left != NULL) {
            q.push(current->left);
        }
        if (current->right != NULL) {
            q.push(current->right);
        }
    }
}

int main() {
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);

    cout << "Level order traversal of binary tree: ";
    printLevelOrder(root);

    return 0;
}
```

**출력:**
```
Level order traversal of binary tree: 1 2 3 4 5 6 7 
```

## 이진 탐색 트리 (BST, Binary Search Tree)

이진 탐색 트리는 이진 트리의 일종으로, 다음과 같은 규칙을 따른다:

- 노드의 오른쪽 하위 트리에는 "노드의 값보다 큰 값"이 있는 노드만 포함된다.
- 노드의 왼쪽 하위 트리에는 "노드의 값보다 작은 값"이 있는 노드만 포함된다.

이 규칙을 따르면, 이진 탐색 트리는 효율적인 검색을 가능하게 한다. 예를 들어, 10을 찾으려고 할 때, 25의 왼쪽 하위 트리만 탐색하면 된다는 사실을 알 수 있다. 이는 전체 트리를 탐색하지 않고도 원하는 값을 빠르게 찾을 수 있음을 의미한다.

### 예시 코드 (C++)

```cpp
#include <iostream>
using namespace std;

// 노드 구조체 정의
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int value) : data(value), left(NULL), right(NULL) {}
};

// 이진 탐색 트리에서 값 검색
bool search(Node* root, int key) {
    if (root == NULL) return false;
    if (root->data == key) return true;
    if (key < root->data) return search(root->left, key);
    return search(root->right, key);
}

int main() {
    // 값 삽입
    Node* root = new Node(15);
    root->left = new Node(10);
    root->right = new Node(20);
    root->left->left = new Node(8);
    root->left->right = new Node(12);
    root->right->left = new Node(17);
    root->right->right = new Node(25);

    int key = 17;
    if (search(root, key)) {
        cout << key << " found in the BST." << endl;
    } else {
        cout << key << " not found in the BST." << endl;
    }

    return 0;
}
```

**출력:**
```
17 found in the BST.
```

### 이진 탐색 트리의 시간 복잡도
- **탐색, 삽입, 삭제, 수정**: 균형 잡힌 경우 O(log N)의 시간 복잡도를 가진다. 하지만, 삽입 순서에 따라 이진 탐색 트리가 선형적 구조를 가질 수 있으며, 이 경우 최악의 시간 복잡도는 O(N)이 된다.

균형 잡힌 이진 탐색 트리를 유지하기 위한 트리로는 **AVL 트리**와 **레드-블랙 트리**가 있으며, C++의 `map`과 `set`은 레드-블랙 트리를 기반으로 구현되어 삽입, 탐색, 삭제, 수정이 모두 O(log N)의 시간 복잡도를 보장한다.
