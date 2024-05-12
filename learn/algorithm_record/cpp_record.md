# cpp로 알고리듬 풀면서 배움점

> 평소에 python 으로 풀다가 종종 cpp 로 풀어보기로 다짐했다,



## 실수로 나눗셈 결과 출력하기

실수로 나눗셈의 결과를 얻기 위해 정수를 `double`로 캐스팅 한다. 그러나 몇 가지 주의사항이 있다.

1. **나누는 수 확인**: `b`가 0인 경우, 프로그램은 런타임 에러를 일으킨다. 0으로 나누는 것을 방지하기 위해 조건문을 사용한다.
2. **출력 형식 지정**: `cout`을 사용할 때 `fixed`와 `setprecision`을 이용하여 출력할 소수점의 자리수를 지정할 수 있다.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    if (b == 0) { // 보통 문제에서 0 이 입력으로 나오지는 않는
        cout << "Division by zero error!" << endl;
        return 1;
    }

    cout << fixed << setprecision(9);
    cout << (double)a / b << endl;

    return 0;
}


```

이 코드는 `b`가 0일 경우 에러 메시지를 출력하고, 소수점 아래로 9자리까지 출력한다.

## `float` vs. `double`

`float`과 `double` 자료형은 둘 다 부동 소수점 수를 저장하지만, 메모리 크기와 표현할 수 있는 정밀도에서 차이가 있다.

- **float**: 32비트 메모리 사용, 유효 숫자는 대략 7자리, 10−7에서 10−8 정밀도
- **double**: 64비트 메모리 사용, 유효 숫자는 대략 15~17자리, 10−15에서 10−17 정밀도

정밀도 요구사항이 높은 경우 10−9 이하의 오차를 허용하기 때문에 `double` 자료형을 사용하는 것이 적합하다.

## C++의 정수형 자료형 정리
C++에서 사용되는 다양한 정수형 자료형들은 저장할 수 있는 값의 범위와 메모리 사용 크기에 따라 구분된다.

- `short`: 16비트 메모리를 사용하며, -32,768에서 +32,767의 범위를 가진다.
- `unsigned short`: 부호 없는 16비트 정수형으로, 0에서 65,535까지의 범위를 가진다.
- `int`: 일반적으로 32비트를 사용하며, -2억에서 +2억까지의 범위의 값을 저장할 수 있다.
- `unsigned int`: 부호 없는 32비트 정수형으로, 0에서 약 40억까지의 범위의 값을 저장할 수 있다.
- `long` (플랫폼에 따라 다름): 일반적으로 32비트 또는 64비트. 32비트 시스템에서는 int와 동일하며, 64비트 시스템에서는 더 큰 범위를 제공한다.
- `unsigned long`: 32비트 또는 64비트 시스템에 따라 범위가 달라진다. 부호 없는 정수형으로 더 큰 양의 숫자를 저장할 수 있다.
- `long long`: 64비트를 사용하며, -9경에서 +9경까지의 매우 큰 범위의 값을 저장할 수 있다.
- `unsigned long long`: 부호 없는 64비트 정수형으로, 0에서 약 1.8경까지의 범위의 값을 저장할 수 있다.
각 자료형은 사용하는 범위에 따라 선택되어야 하며, 특히 알고리즘 문제를 풀 때는 범위를 넘어서는 연산을 피하기 위해 적절한 타입을 사용하는 것이 중요하다.

```cpp
#include <iostream>

int main() {
    short a = 32767;
    unsigned short b = 65535;
    int c = 2000000000;
    unsigned int d = 4000000000U;
    long e = 2000000000L;
    unsigned long f = 4000000000UL;
    long long g = 9000000000000000000LL;
    unsigned long long h = 18000000000000000000ULL;

    std::cout << "short: " << a << std::endl;
    std::cout << "unsigned short: " << b << std::endl;
    std::cout << "int: " << c << std::endl;
    std::cout << "unsigned int: " << d << std::endl;
    std::cout << "long: " << e << std::endl;
    std::cout << "unsigned long: " << f << std::endl;
    std::cout << "long long: " << g << std::endl;
    std::cout << "unsigned long long: " << h << std::endl;

    return 0;
}

```


## include <iomanip>에 대해
> <iomanip> 헤더는 C++에서 입출력 조작을 위한 기능들을 제공한다. 이를 통해 출력 형식을 세밀하게 조정할 수 있다.

주요 기능:
- setw(int n): 다음에 출력할 항목을 n 글자 폭으로 출력하도록 설정한다.
- setfill(char c): setw로 설정된 폭이 전체 글자 수보다 클 경우, 남는 공간을 c 문자로 채운다.
예를 들어, 숫자를 5자리로 맞추고 빈 자리를 0으로 채우려면 다음과 같이 작성할 수 있다:

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int number = 42;
    cout << setfill('0') << setw(5) << number << endl;
    return 0;
}
```
> 이 코드는 00042를 출력한다.

### C++에서 전역 변수 선언과 const 사용
전역 변수는 프로그램의 어느 곳에서나 접근할 수 있는 변수다. C++에서는 전역 변수를 선언할 때, 가능한 `const` 키워드를 사용해 상수로 만드는 것이 좋다. const를 사용하면 변수가 프로그램 실행 도중에 변경되지 않음을 보장하며, 이는 코드의 안정성과 예측 가능성을 높인다.

C++에는 let 키워드가 없으며, const가 그 역할을 대신한다. JavaScript 등 다른 언어에서 let을 사용하는 것과 달리, C++에서는 변수의 범위와 수정 가능성을 제어하기 위해 const, static 등의 키워드를 사용한다.

```cpp
#include <iostream>
using namespace std;

const int LIMIT = 100;

int main() {
    cout << "The limit is " << LIMIT << endl;
    // LIMIT = 200; // 컴파일 에러가 발생한다
    return 0;
}
```
> 이 예제는 전역 상수 LIMIT을 선언하고 사용하는 방법을 보여준다. 만약 LIMIT의 값을 변경하려고 하면 컴파일 에러가 발생한다.