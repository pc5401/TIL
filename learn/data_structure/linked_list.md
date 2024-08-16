# 연결리스트 (Linked List)
연결리스트는 각 요소가 독립적인 메모리 공간에 저장되고, 각 요소가 다음 요소를 가리키는 포인터로 연결된 선형적인 자료구조이다. 이 구조에서 각 요소를 노드라고 하며, 노드는 데이터를 담고 있는 data와 다음 노드를 가리키는 포인터인 next로 구성되어 있다.

## 노드(Node)의 구조
노드는 간단한 구조체로, data와 next로 구성된다. data는 값을 담고, next는 다음 노드를 가리킨다. 예를 들어, 다음과 같이 노드를 정의할 수 있다:

```cpp
class Node {
public:
    int data;
    Node* next;

    Node() : data(0), next(NULL) {}

    Node(int data) : data(data), next(NULL) {}
};
```
> 이 구조를 통해 연결리스트는 여러 노드가 체인처럼 연결된 형태를 가지게 된다.

### 연결리스트의 시간복잡도
연결리스트에서 특정 노드를 참조하거나 탐색하는 데는 O(n)의 시간이 소요된다. 반면, 삽입과 삭제는 O(1) 시간에 수행된다. 이는 연결리스트의 노드들이 물리적으로 인접한 메모리 위치에 저장되지 않기 때문이다.

## 연결리스트의 종류
연결리스트는 크게 세 가지로 나뉜다:

### 1. 싱글연결리스트 (Singly Linked List)
- 각 노드는 next 포인터를 통해 다음 노드만을 가리키며, 데이터는 한 방향으로만 연결된다.
- 예시(C언어)
``` c
#include <stdio.h>
#include <stdlib.h>

// 노드 구조체 정의
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// 노드 추가 함수
void insert(Node** head, int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = *head;
    *head = new_node;
}

// 리스트 출력 함수
void printList(Node* node) {
    while (node != NULL) {
        printf("%d -> ", node->data);
        node = node->next;
    }
    printf("NULL\n");
}

int main() {
    Node* head = NULL;

    // 노드 추가
    insert(&head, 3);
    insert(&head, 2);
    insert(&head, 1);

    // 리스트 출력
    printList(head);

    return 0;
}
```
#### 출력
```
1 -> 2 -> 3 -> NULL
```


### 이중연결리스트 (Doubly Linked List)
- 각 노드는 prev와 next 두 개의 포인터를 가지고, 앞뒤로 양방향으로 데이터가 연결된다.
- 예시 C언어
```c
#include <stdio.h>
#include <stdlib.h>

// 노드 구조체 정의
typedef struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
} Node;

// 노드 추가 함수
void insert(Node** head, int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = *head;
    new_node->prev = NULL;
    
    if (*head != NULL) {
        (*head)->prev = new_node;
    }
    *head = new_node;
}

// 리스트 출력 함수 (앞에서 뒤로)
void printList(Node* node) {
    Node* last;
    printf("Traversal in forward direction:\n");
    while (node != NULL) {
        printf("%d -> ", node->data);
        last = node;
        node = node->next;
    }
    printf("NULL\n");
    
    printf("Traversal in reverse direction:\n");
    while (last != NULL) {
        printf("%d -> ", last->data);
        last = last->prev;
    }
    printf("NULL\n");
}

int main() {
    Node* head = NULL;

    // 노드 추가
    insert(&head, 3);
    insert(&head, 2);
    insert(&head, 1);

    // 리스트 출력
    printList(head);

    return 0;
}
```
#### 출력

```
Traversal in forward direction:
1 -> 2 -> 3 -> NULL
Traversal in reverse direction:
3 -> 2 -> 1 -> NULL
```

### 원형연결리스트 (Circular Linked List)
- 마지막 노드가 첫 번째 노드를 가리켜 원형을 이루는 구조이다. 
- 이 역시 싱글연결리스트와 이중연결리스트로 나뉜다.
- 예시 C언어
```c
#include <stdio.h>
#include <stdlib.h>

// 노드 구조체 정의
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// 노드 추가 함수
void insert(Node** head, int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = *head;

    if (*head != NULL) {
        Node* temp = *head;
        while (temp->next != *head) {
            temp = temp->next;
        }
        temp->next = new_node;
    } else {
        new_node->next = new_node;  // 처음 노드를 추가할 때 자신을 가리키게 설정
    }
    
    *head = new_node;
}

// 리스트 출력 함수
void printList(Node* head) {
    Node* temp = head;
    if (head != NULL) {
        do {
            printf("%d -> ", temp->data);
            temp = temp->next;
        } while (temp != head);
    }
    printf("(head)\n");
}

int main() {
    Node* head = NULL;

    // 노드 추가
    insert(&head, 3);
    insert(&head, 2);
    insert(&head, 1);

    // 리스트 출력
    printList(head);

    return 0;
}
```
#### 출력

```
1 -> 2 -> 3 -> NULL
```

### C++에서의 연결리스트 예시
- C++의 list 클래스는 연결리스트를 구현할 수 있는 편리한 방법을 제공한다. 
- 다음은 list를 사용한 간단한 예시이다:

```cpp
#include <list>
#include <iostream>

using namespace std;

list<int> a;

void print(list<int> a) {
    for(auto it : a) cout << it << " ";
    cout << '\n';
}

int main() {
    for(int i = 1; i <= 3; ++i) a.push_back(i);    // 뒤에서부터 1, 2, 3 삽입
    for(int i = 1; i <= 3; ++i) a.push_front(i);   // 앞에서부터 1, 2, 3 삽입

    auto it = a.begin(); 
    it++;
    a.insert(it, 1000);  // 두 번째 위치에 1000 삽입
    print(a);

    it = a.begin(); 
    it++;
    a.erase(it);  // 두 번째 요소 제거
    print(a);

    a.pop_front(); // 첫 번째 요소 제거
    a.pop_back();  // 마지막 요소 제거
    print(a);

    cout << a.front() << " : " << a.back() << '\n'; // 첫 번째와 마지막 요소 출력
    a.clear();  // 모든 요소 제거

    return 0;
}
```
- 이 코드에서 list는 연결리스트의 기능을 제공하며, 다양한 메서드를 사용해 요소를 추가하거나 삭제할 수 있다.

#### 연결리스트 메서드 설명
- `push_front(value)`: 리스트의 앞에 요소를 추가한다.
- `push_back(value)`: 리스트의 뒤에 요소를 추가한다.
- `insert(iterator, value)`: 리스트의 특정 위치에 요소를 삽입한다.
- `erase(iterator)`: 리스트에서 특정 위치의 요소를 제거한다.
- `pop_front()`: 리스트의 첫 번째 요소를 제거한다.
- `pop_back()`: 리스트의 마지막 요소를 제거한다.
- `front()`: 리스트의 첫 번째 요소를 참조한다.
- `back()`: 리스트의 마지막 요소를 참조한다.
- `clear()`: 리스트의 모든 요소를 제거한다.

#### 랜덤 접근과 순차적 접근
- 연결리스트는 랜덤 접근이 불가능하고, 순차적 접근만 가능하다. 
- 즉, 리스트의 특정 위치에 접근하려면 처음부터 순차적으로 탐색해야 한다. 
- 반면, 배열과 같은 구조는 랜덤 접근이 가능해 특정 인덱스의 요소에 바로 접근할 수 있다.

### 연결리스트가 사용되는 상황

연결리스트는 메모리의 효율적인 사용, 동적 크기 조정, 그리고 빈번한 삽입/삭제가 필요한 경우에 주로 사용된다.

- `빈번한 삽입/삭제가 필요한 경우`: 배열과 달리, 연결리스트는 삽입/삭제 시 다른 요소들을 이동시키지 않아도 되므로 성능이 좋다. 예를 들어, 대기열 관리, 이벤트 핸들링 시스템 등에서 유용하다.

- `동적 크기 조정이 필요한 경우`: 연결리스트는 크기가 동적으로 변하므로, 사전에 크기를 예측할 수 없는 데이터를 저장할 때 유용하다. 예를 들어, 메모리 부족 상태에서도 새로운 데이터를 추가할 수 있는 상황에서 사용된다.

- `메모리의 분산된 사용`: 배열은 연속된 메모리 공간을 필요로 하지만, 연결리스트는 분산된 메모리 공간을 사용할 수 있다. 이로 인해 큰 데이터를 처리할 때 메모리 활용이 더 유연해질 수 있다.

- `데이터 구조의 구현`: 연결리스트는 스택, 큐, 그래프의 인접 리스트와 같은 복잡한 데이터 구조를 구현하는 데 사용된다. 이러한 구조에서는 노드 간의 관계를 유지하기 위해 포인터가 필요하므로, 연결리스트가 매우 유용하다.

연결리스트는 배열과 달리, 메모리 활용이 유연하고 동적이기 때문에 다양한 상황에서 효과적으로 사용할 수 있다.

### 사용 사례

1. 운영체제
   - 프로세스 관리: 많은 운영체제에서는 프로세스 제어 블록(PCB)을 연결리스트로 관리한다. 프로세스가 생성되거나 종료될 때, PCB를 리스트에 추가하거나 제거하는 작업이 빈번하게 일어나는데, 연결리스트를 사용하면 이러한 작업을 효율적으로 수행할 수 있다.
   - 메모리 관리: 가용 메모리 블록을 관리하기 위해 연결리스트를 사용한다. 특히 동적 메모리 할당 시스템에서는 연결리스트를 통해 메모리의 가용 블록을 추적하고 관리한다.
2. 웹 브라우저
   - 히스토리 관리: 웹 브라우저의 방문 기록(히스토리)은 연결리스트 구조로 구현될 수 있다. 각 방문 페이지는 노드로 표현되며, '뒤로 가기'와 '앞으로 가기' 기능을 양방향 연결리스트로 쉽게 구현할 수 있다.
3. 문서 편집기
   - Undo/Redo 기능: 문서 편집기에서는 사용자의 작업 기록을 연결리스트로 관리한다. 사용자가 작업을 되돌리거나 다시 적용할 때, 연결리스트의 노드를 따라가며 이전 상태를 복원할 수 있다.
4. 그래픽스 및 게임 개발
   - 씬 그래프(Scene Graph): 그래픽스 엔진이나 게임 엔진에서 씬 그래프는 연결리스트 구조로 노드를 관리한다. 각 노드는 개별 객체나 장면의 요소를 나타내며, 연결리스트를 통해 이들을 효율적으로 관리하고 조작할 수 있다.
5. 동적 자료 구조
   - 스택과 큐: 스택과 큐의 구현에서 연결리스트는 매우 유용하다. 예를 들어, 웹 서버의 요청 대기열, 작업 대기열 등에 큐가 사용되며, 이때 연결리스트를 사용하면 효율적으로 관리할 수 있다.
6. 컴파일러
   - 토큰 리스트: 컴파일러는 소스 코드를 파싱할 때, 각 토큰을 연결리스트로 관리할 수 있다. 이는 구문 분석기와 같은 컴파일러 구성 요소에서 빈번하게 사용된다.
7. 데이터베이스 관리 시스템(DBMS)
   - 트랜잭션 관리: 데이터베이스에서 트랜잭션 로그를 관리하기 위해 연결리스트를 사용한다. 트랜잭션 로그는 각 데이터베이스 조작을 기록하며, 트랜잭션이 롤백되거나 커밋될 때 연결리스트를 통해 효율적으로 관리된다.