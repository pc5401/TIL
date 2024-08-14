# 배열 
> cpp

## 정적 배열
정적 배열은 컴파일 타임에 크기가 정해지는 배열이다. 이 배열의 크기는 한 번 정해지면 변경할 수 없으며, 연속된 메모리 공간에 같은 타입의 요소들을 저장한다. 배열의 각 요소는 숫자 인덱스를 통해 접근할 수 있으며, 중복된 값을 허용한다. 이러한 배열은 접근 속도가 빠르다는 장점이 있다.

정적 배열의 선언 방식에는 C 스타일과 C++ 스타일이 있다. C 스타일에서는 int `a[10];`처럼 선언하고, C++ 스타일에서는 `std::array<int, 10> a;`와 같은 형식을 사용한다. 배열의 크기를 명시하지 않고도 초기화할 수 있으며, 컴파일러가 초기화된 요소들의 개수를 바탕으로 배열의 크기를 자동으로 결정한다.

### C++ 예시 코드
``` cpp
#include <iostream>
#include <array>

int main() {
    // C 스타일 배열 선언 및 초기화
    int c_array[3] = {1, 2, 3};
    
    // 배열의 크기를 컴파일러가 자동으로 결정
    int c_array_auto[] = {4, 5, 6, 7};

    // C++ 스타일 배열 선언 및 초기화
    std::array<int, 3> cpp_array = {8, 9, 10};

    // C 스타일 배열 출력
    for(int i = 0; i < 3; ++i) {
        std::cout << c_array[i] << " ";
    }
    std::cout << std::endl;

    // 자동 크기 배열 출력
    for(int i = 0; i < 4; ++i) {
        std::cout << c_array_auto[i] << " ";
    }
    std::cout << std::endl;

    // C++ 스타일 배열 출력
    for(int i = 0; i < cpp_array.size(); ++i) {
        std::cout << cpp_array[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}

```

## 동적 배열 (vector)
C++ STL 에서 지원하는 동적 배열인 `vector`는 실행 시점에 크기를 조절할 수 있는 배열이다. `vector`는 배열의 크기를 동적으로 늘리거나 줄일 수 있기 때문에, 사용해야 할 요소의 개수를 미리 알 수 없는 경우에 유용하다. vector도 정적 배열처럼 연속된 메모리 공간에 같은 타입의 요소들을 저장하며, 인덱스를 통해 요소에 접근할 수 있다.

`vector`는 다양한 메서드를 제공하여 배열의 끝에 요소를 추가하거나 제거하고, 특정 위치의 요소를 삭제하거나 검색할 수 있다. 또한, vector는 미리 크기를 지정하고 초기화할 수도 있다.

``` cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    // 빈 vector 선언
    std::vector<int> v;

    // 요소 추가
    for(int i = 1; i <= 5; ++i) {
        v.push_back(i);
    }

    // 요소 출력
    for(const int &n : v) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // 마지막 요소 제거
    v.pop_back();

    // 첫 번째 요소 삭제
    v.erase(v.begin());

    // 요소 출력
    for(const int &n : v) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // 모든 요소 100으로 초기화
    std::fill(v.begin(), v.end(), 100);

    // 요소 출력
    for(const int &n : v) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    return 0;
}
```
## vector 의 메서드

### 1. push_back()
`push_back()` 메서드는 vector의 마지막에 새로운 요소를 추가한다. 이 메서드는 동적 배열의 크기를 자동으로 늘려주며, vector에 요소를 쉽게 추가할 수 있게 해준다.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v;

    // 1부터 5까지의 숫자를 vector에 추가
    for(int i = 1; i <= 5; ++i) {
        v.push_back(i);
    }

    // vector의 모든 요소 출력
    for(const int &n : v) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    return 0;
}
```
출력 
```
1 2 3 4 5
```

### 2. pop_back()
`pop_back()` 메서드는 vector의 마지막 요소를 제거한다. 이 메서드는 마지막 요소를 제거하면서 vector의 크기를 1 줄인다.

``` cpp
코드 복사
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};

    // 마지막 요소 제거
    v.pop_back();

    // vector의 모든 요소 출력
    for(const int &n : v) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

출력 
```
1 2 3 4
```

### 3. erase()
`erase()` 메서드는 vector에서 특정 위치에 있는 요소를 제거하거나, 특정 범위의 요소를 제거할 때 사용한다. 두 가지 형식이 있다:

- `erase(position)` : 지정된 위치의 요소를 제거
- `erase(first, last)` : 지정된 범위 `[first, last)`의 요소를 제거

``` cpp
코드 복사
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};

    // 첫 번째 요소 제거
    v.erase(v.begin());

    // 중간의 두 요소 제거
    v.erase(v.begin() + 1, v.begin() + 3);

    // vector의 모든 요소 출력
    for(const int &n : v) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    return 0;
}
```
출력
```
2 5
```

### 4. clear()
`clear()` 메서드는 vector의 모든 요소를 제거한다. 이 메서드는 vector를 비워 크기를 0으로 만든다.

``` cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};

    // vector 비우기
    v.clear();

    // vector의 크기 출력
    std::cout << "Vector size after clear: " << v.size() << std::endl;

    return 0;
}
```
출력
```
Vector size after clear: 0
```

### 5. resize()
`resize()` 메서드는 vector의 크기를 조절한다. 만약 크기를 늘리면 새로운 요소는 기본값으로 초기화되며, 크기를 줄이면 나머지 요소는 제거된다.

``` cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};

    // vector의 크기를 7로 늘리기 (기본값으로 초기화)
    v.resize(7);

    // vector의 모든 요소 출력
    for(const int &n : v) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // vector의 크기를 3으로 줄이기
    v.resize(3);

    // vector의 모든 요소 출력
    for(const int &n : v) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    return 0;
}
```
출력
```
1 2 3 4 5 0 0 
1 2 3
```

### 6. insert()
`insert()` 메서드는 vector의 특정 위치에 새로운 요소를 삽입한다. 기존 요소들은 삽입된 요소 뒤로 밀려난다.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 4, 5};

    // 2번 인덱스 위치에 3 삽입
    v.insert(v.begin() + 2, 3);

    // vector의 모든 요소 출력
    for(const int &n : v) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    return 0;
}
```
출력:
```
1 2 3 4 5
```

### 7. emplace_back()
`emplace_back()` 메서드는 push_back()과 비슷하지만, 객체를 직접 생성하여 vector의 끝에 추가한다. 이 메서드는 복사나 이동 연산을 피할 수 있어 더 효율적일 수 있다.

```cpp
#include <iostream>
#include <vector>

struct Point {
    int x, y;
    Point(int x, int y) : x(x), y(y) {}
};

int main() {
    std::vector<Point> points;

    // Point 객체를 vector의 끝에 추가
    points.emplace_back(1, 2);
    points.emplace_back(3, 4);

    // vector의 모든 요소 출력
    for(const Point &p : points) {
        std::cout << "(" << p.x << ", " << p.y << ")" << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

출력
```
(1, 2) (3, 4)
```

### 8. swap()
`swap()` 메서드는 두 vector의 내용을 서로 교환한다.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v1 = {1, 2, 3};
    std::vector<int> v2 = {4, 5, 6};

    // v1과 v2의 내용 교환
    v1.swap(v2);

    // v1 출력
    std::cout << "v1: ";
    for(const int &n : v1) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    // v2 출력
    std::cout << "v2: ";
    for(const int &n : v2) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

출력
``` 
v1: 4 5 6 
v2: 1 2 3
```
