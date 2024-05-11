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
