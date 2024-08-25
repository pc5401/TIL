# Map (맵)

Map은 고유한 키를 기반으로 키-값(Key-Value) 쌍을 저장하는 정렬된 자료구조이다. 이 자료구조는 균형 잡힌 이진 탐색 트리인 레드-블랙 트리로 구현되며, 키가 삽입될 때마다 자동으로 정렬된다.

만약 해시 테이블 기반의 맵을 원한다면 `unordered_map` 를 사용하자.
## 시간 복잡도

- **참조**: O(log n)
- **탐색**: O(log n)
- **삽입/삭제**: O(log n)

## 특징

- **고유한 키**: Map의 키는 고유하며, 동일한 키를 중복하여 사용할 수 없다.
- **자동 정렬**: 삽입된 데이터는 자동으로 오름차순(아스키 코드 순서)에 따라 정렬된다.
- **대괄호 연산자**: 대괄호 `[]` 연산자를 통해 키를 사용해 값을 직접 참조할 수 있다.

## 예시

Map은 키와 값을 쌍으로 저장할 때 사용된다. 예를 들어, "이승철"이라는 이름을 키로 하고, 1이라는 정수를 값으로 저장할 수 있다. Map의 키와 값은 `string`, `int` 등 다양한 타입을 가질 수 있다.

```cpp
#include <map>
#include <string>
#include <iostream> // 입출력에 필요한 헤더

using namespace std;

map<string, int> mp;
string names[] = {"홍길동", "김철수", "이영희"};

int main() {
    // Map에 값 삽입
    for(int i = 0; i < 3; i++){
        mp.insert({names[i], i + 1});
    }

    // 특정 키의 값 출력
    cout << mp["홍길동"] << '\n';  // 출력: 1

    // Map의 크기 출력
    cout << mp.size() << '\n';  // 출력: 3

    // 특정 키 삭제
    mp.erase("홍길동");

    // 특정 키 탐색
    auto it = mp.find("홍길동");
    if(it == mp.end()){
        cout << "맵에서 해당 요소는 없다.\n";
    }

    // 대괄호를 이용한 값 삽입
    mp["이순신"] = 100;

    // Map의 모든 요소 출력
    for(auto it : mp){
        cout << it.first << " : " << it.second << '\n';
    }

    // Map 초기화
    mp.clear();
    cout << "map의 사이즈는 : " << mp.size() << "이다.\n";  // 출력: 0

    return 0;
}
```

### 주요 메서드와 연산자

- **insert({key, value})**: 키와 값을 맵에 삽입한다.
- **[key] = value**: 대괄호를 통해 키에 해당하는 값으로 설정한다.
- **[key]**: 대괄호를 통해 키를 사용하여 맵의 요소를 참조한다. 만약 해당 키가 존재하지 않으면, 기본 값으로 초기화된 상태에서 키가 추가된다.
- **size()**: 맵에 저장된 요소의 개수를 반환한다.
- **erase(key)**: 특정 키에 해당하는 요소를 삭제한다.
- **find(key)**: 맵에서 특정 키를 가진 요소를 찾아 해당 이터레이터를 반환한다. 키가 존재하지 않으면 `end()` 이터레이터를 반환한다.
- **clear()**: 맵의 모든 요소를 제거한다.
- **순회 (iteration)**:
    - **범위 기반 for 루프**: `for (auto it : mp)`로 맵을 순회할 수 있다. 이때 키는 `it.first`, 값은 `it.second`로 접근할 수 있다.
    - **이터레이터를 사용한 순회**: `for (auto it = mp.begin(); it != mp.end(); it++)`로 맵을 이터레이터를 통해 순회할 수 있다.