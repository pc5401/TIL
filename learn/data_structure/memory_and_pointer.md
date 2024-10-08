
# 메모리와 포인터 학습 내용 정리

## 1. 메모리와 주소

C++에서 변수를 선언하면, 컴퓨터는 해당 변수에 필요한 메모리 공간을 할당한다. 예를 들어, `int i;`라는 코드를 작성하면, 4바이트 크기의 메모리 공간이 할당된다. 이 메모리 공간은 연속된 메모리 셀로 이루어져 있으며, 각 셀은 고유한 주소를 가진다. 

변수 `i`의 메모리 주소를 출력하려면, C++에서 `&` 연산자(앰퍼샌드)를 사용하여 변수의 메모리 주소를 얻을 수 있다.

### C++ 코드 예시
```cpp
#include <iostream>
using namespace std;

int i;

int main(){
    cout << &i << '\n'; // 변수 i의 메모리 주소 출력
    return 0;
}

```
**출력 예시:** `0x100bbc000`  
(메모리 주소는 실행 시점에 따라 달라질 수 있음)

변수에 값을 할당해도 해당 변수의 메모리 주소는 변하지 않는다.

### C++ 코드 예시
```cpp
#include <iostream>
using namespace std;

int i;

int main(){
    cout << &i << '\n'; // 변수 i의 메모리 주소 출력
    i = 0;              // 변수 i에 0 할당
    cout << &i << '\n'; // 변수 i의 메모리 주소 재출력
    return 0;
}
```
**출력 예시:**  
```
0x100f28000
0x100f28000
```

## 2. 포인터

포인터는 변수의 메모리 주소를 저장하는 특수한 타입이다. C++에서는 개발자가 직접 메모리를 관리할 수 있으며, 포인터를 통해 동적 메모리 할당, 함수 매개변수로의 효율적인 데이터 전달, 그리고 구조체나 클래스의 연결 등이 가능하다.

포인터는 `<타입> *` 형태로 선언되며, 특정 변수의 메모리 주소를 담는다.

### C++ 코드 예시
```cpp
#include <iostream>
using namespace std;

int i;
string s = "kundol";

int main(){
    i = 0;
    int *a = &i;       // 변수 i의 주소를 담는 포인터 a
    cout << a << '\n'; // 포인터 a가 가리키는 메모리 주소 출력

    string *b = &s;    // 변수 s의 주소를 담는 포인터 b
    cout << b << '\n'; // 포인터 b가 가리키는 메모리 주소 출력

    return 0;
}
```

포인터의 크기는 운영체제의 비트 수에 따라 달라진다. 32비트 운영체제에서는 4바이트, 64비트 운영체제에서는 8바이트의 크기를 가지며, 타입에 상관없이 고정된 크기를 가진다.

## 3. 역참조 연산자

C++에서 `*` 연산자는 다양한 용도로 사용될 수 있다. 그중 하나는 포인터를 역참조하여 메모리 주소에 저장된 값을 읽거나 수정하는 기능이다.

### C++ 코드 예시
```cpp
#include <iostream>
using namespace std;

int main(){
    string a = "abcda";
    string *b = &a;

    cout << b << "\n";    // 포인터 b가 가리키는 메모리 주소 출력
    cout << *b << "\n";   // 포인터 b를 역참조하여 값 출력

    return 0;
}
```
**출력 예시:**  
```
0x6ffdf0
abcda
```

## 4. Array to Pointer Decay

배열의 이름을 포인터처럼 사용할 수 있다는 사실은 "Array to Pointer Decay"라고 불리는 현상 때문이다. 배열의 이름은 배열의 첫 번째 요소의 주소를 가리키며, 배열 전체의 크기 정보는 사라지게 된다. 이는 배열의 이름을 포인터에 할당할 때 발생하며, 배열의 크기 정보가 소실되고 배열의 첫 번째 요소의 주소가 바인딩된다.

### C++ 코드 예시
```cpp
#include <iostream>
using namespace std;

int a[3] = {1, 2, 3};

int main(){
    int *c = a;           // 배열 이름을 포인터에 할당 (첫 번째 요소의 주소가 바인딩됨)
    
    cout << c << "\n";    // 포인터 c 출력 (첫 번째 요소의 주소)
    cout << &a[0] << "\n"; // 배열의 첫 번째 요소 주소 출력

    cout << c + 1 << "\n"; // 포인터를 증가시켜 두 번째 요소 주소 출력
    cout << &a[1] << "\n"; // 배열의 두 번째 요소 주소 출력

    return 0;
}
```
**출력 예시:**  
```
0x472010
0x472010
0x472014
0x472014
```

이와 같이, 배열의 이름은 배열의 첫 번째 요소의 주소로 사용될 수 있으며, 이는 포인터와 동일하게 작동한다. 하지만 `vector` 같은 동적 배열에는 먹히지 않는다.
