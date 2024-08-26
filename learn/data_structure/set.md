# Set (셋)

Set은 고유한 요소만을 저장하는 자료구조이다. 중복된 값을 허용하지 않으며, 삽입된 요소들은 자동으로 정렬된다. Set은 Map과 달리 키-값 쌍이 아닌 단일 값만을 저장한다. Set에 동일한 값을 여러 번 삽입해도 중복이 제거되며, 최종적으로 하나의 값만 남는다.

## 시간 복잡도

- **참조**: O(log n)
- **탐색**: O(log n)
- **삽입/삭제**: O(log n)

## C++의 `set` 구현 방식

C++에서 `set`은 **균형 이진 탐색 트리**로 구현되며, 구체적으로는 **레드-블랙 트리**를 사용한다. 이 구조 덕분에 Set에 저장된 요소들은 자동으로 정렬되며, 삽입, 삭제, 탐색 등의 연산이 O(log n)의 시간 복잡도로 수행된다.

## 예시

아래는 정수를 저장하는 Set의 예시이다. 중복된 값을 삽입하려고 할 때, Set은 이를 무시하고 유일한 값만을 저장한다.

```cpp
#include <set>
#include <iostream>

using namespace std;

int main() {
    set<int> mySet;

    // 값 삽입
    mySet.insert(5);
    mySet.insert(3);
    mySet.insert(5);  // 중복된 값

    // 값 출력
    for(auto it : mySet){
        cout << it << '\n';
    }

    // 값 삭제
    mySet.erase(3);

    // 특정 값 탐색
    if(mySet.find(5) != mySet.end()){
        cout << "5는 셋에 있다.\n";
    } else {
        cout << "5는 셋에 없다.\n";
    }

    return 0;
}

```

### 예시 설명

1. `mySet.insert(5)`는 Set에 5를 삽입한다. 두 번째 `insert(5)`는 이미 존재하는 값이므로 삽입되지 않는다.
2. `mySet.erase(3)`는 Set에서 3을 삭제한다.
3. `mySet.find(5)`를 통해 Set에서 5를 찾고, 5가 존재하면 해당 메시지를 출력한다.

### 주요 메서드와 연산자

- **insert(value)**: Set에 값을 삽입한다. 중복된 값은 무시된다.
- **erase(value)**: Set에서 특정 값을 제거한다.
- **find(value)**: Set에서 특정 값을 찾고, 해당 이터레이터를 반환한다. 값이 없으면 `end()`를 반환한다.
- **size()**: Set에 저장된 요소의 개수를 반환한다.
- **clear()**: Set의 모든 요소를 제거한다.
- **순회 (iteration)**:
    - **범위 기반 for 루프**: `for (auto it : mySet)`을 통해 Set을 순회할 수 있다.
    - **이터레이터를 사용한 순회**: `for (auto it = mySet.begin(); it != mySet.end(); it++)`으로 Set을 순회할 수 있다.