# 알고리듬용 C++ STL 정리

## `std::vector`

`std::vector`는 C++ 표준 템플릿 라이브러리(STL)에서 제공하는 동적 배열 컨테이너이다. 이는 크기가 가변적이고 연속된 메모리 블록을 사용하여 효율적으로 요소에 접근할 수 있는 장점을 가지고 있다.

## 기본 사용법

### 벡터 선언 및 초기화

```cpp
#include <vector>
#include <iostream>

int main() {
    // 빈 벡터 선언
    std::vector<int> vec1;

    // 초기 크기와 기본값으로 벡터 선언
    std::vector<int> vec2(10, 0); // 크기 10, 모든 요소는 0으로 초기화

    // 초기화 리스트를 사용한 벡터 선언
    std::vector<int> vec3 = {1, 2, 3, 4, 5};

    // 기존 벡터를 복사한 벡터 선언
    std::vector<int> vec4(vec3);

    return 0;
}

```
### 요소 접근

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // 인덱스를 이용한 접근
    std::cout << "첫 번째 요소: " << vec[0] << std::endl;

    // at() 메서드를 이용한 접근 (범위 검사 포함)
    std::cout << "두 번째 요소: " << vec.at(1) << std::endl;

    // front()와 back() 메서드를 이용한 접근
    std::cout << "첫 번째 요소: " << vec.front() << std::endl;
    std::cout << "마지막 요소: " << vec.back() << std::endl;

    return 0;
}

```

### 요소 추가 및 제거

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec;

    // push_back()을 이용한 요소 추가
    vec.push_back(10);
    vec.push_back(20);

    // emplace_back()을 이용한 요소 추가 (더 효율적일 수 있음)
    vec.emplace_back(30);

    // pop_back()을 이용한 요소 제거
    vec.pop_back();

    for(int i : vec) {
        std::cout << i << " ";
    }

    return 0;
}
```

### 벡터의 크기와 용량

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    std::cout << "벡터의 크기: " << vec.size() << std::endl;
    std::cout << "벡터의 용량: " << vec.capacity() << std::endl;
    std::cout << "벡터가 비어 있는가: " << std::boolalpha << vec.empty() << std::endl;

    // 벡터의 크기 변경
    vec.resize(3);
    std::cout << "변경된 벡터의 크기: " << vec.size() << std::endl;

    // 용량 확보
    vec.reserve(10);
    std::cout << "변경된 벡터의 용량: " << vec.capacity() << std::endl;

    return 0;
}
```

### 반복자 사용

``` cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // 정방향 반복자 사용
    std::cout << "벡터 요소 (정방향): ";
    for(auto it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    // 역방향 반복자 사용
    std::cout << "벡터 요소 (역방향): ";
    for(auto rit = vec.rbegin(); rit != vec.rend(); ++rit) {
        std::cout << *rit << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

#### 요약
std::vector는 동적 배열로서의 역할을 충실히 수행하며, 다양한 기능을 통해 효율적인 데이터 관리를 지원한다.

## 벡터의 고급 기능

### 삽입 및 삭제

벡터에서 특정 위치에 요소를 삽입하거나 삭제할 수 있다.

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // 특정 위치에 요소 삽입
    vec.insert(vec.begin() + 2, 10);

    // 특정 위치에 여러 요소 삽입
    vec.insert(vec.end(), {6, 7, 8});

    // 특정 위치의 요소 삭제
    vec.erase(vec.begin() + 3);

    // 특정 범위의 요소 삭제
    vec.erase(vec.begin() + 1, vec.begin() + 3);

    for(int i : vec) {
        std::cout << i << " ";
    }

    return 0;
}
```

### 벡터의 메모리 관리
벡터는 내부적으로 메모리를 관리한다. shrink_to_fit 메서드를 사용하여 벡터의 용량을 현재 크기에 맞출 수 있다.

``` cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // 벡터의 용량을 늘림
    vec.reserve(100);

    std::cout << "벡터의 크기: " << vec.size() << std::endl;
    std::cout << "벡터의 용량: " << vec.capacity() << std::endl;

    // 벡터의 용량을 크기에 맞춤
    vec.shrink_to_fit();

    std::cout << "shrink_to_fit 후 벡터의 용량: " << vec.capacity() << std::endl;

    return 0;
}
```

### 벡터의 2차원 배열
벡터를 사용하여 2차원 배열을 만들 수 있다.

``` cpp
#include <vector>
#include <iostream>

int main() {
    // 2차원 벡터 선언 및 초기화
    std::vector<std::vector<int>> vec2D(3, std::vector<int>(4, 0));

    // 2차원 벡터 요소 접근 및 수정
    vec2D[1][2] = 5;

    for(const auto& row : vec2D) {
        for(int val : row) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
```

### 벡터 정렬 및 탐색
벡터의 요소를 정렬하거나 특정 값을 탐색할 수 있다.

``` cpp
#include <vector>
#include <iostream>
#include <algorithm>

int main() {
    std::vector<int> vec = {4, 2, 5, 1, 3};

    // 벡터 정렬
    std::sort(vec.begin(), vec.end());

    // 벡터 출력
    for(int i : vec) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    // 이진 탐색 (벡터가 정렬된 상태여야 함)
    if (std::binary_search(vec.begin(), vec.end(), 3)) {
        std::cout << "3이 벡터에 존재합니다." << std::endl;
    } else {
        std::cout << "3이 벡터에 존재하지 않습니다." << std::endl;
    }

    return 0;
}

```

이 문서는 C++ Reference를 참조하여 작성함