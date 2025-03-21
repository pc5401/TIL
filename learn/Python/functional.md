# 함수형 기본 개념 정리
- 함수형 프로그래밍(functional programming)은 프로그램을 함수의 계산으로 구성하는 프로그래밍 패러다임이다. 
- 함수형 프로그래밍의 핵심 개념은 순수 함수(pure function), 불변성(immutability), 고차 함수(higher-order function), 재귀(recursion) 등이다. Python은 객체 지향 프로그래밍 언어이지만, 함수형 프로그래밍의 개념을 지원한다.

## 1. 순수 함수(Pure Function)
순수 함수는 동일한 입력에 대해 항상 동일한 출력을 반환하고, 함수 외부의 상태를 변경하지 않는 함수이다.
``` python
def pure_function(x, y):
    return x + y

# 동일한 입력에 대해 항상 동일한 출력 반환
print(pure_function(2, 3))  # 5
print(pure_function(2, 3))  # 5
```

## 1. 순수 함수(Pure Function)
순수 함수는 동일한 입력에 대해 항상 동일한 출력을 반환하고, 함수 외부의 상태를 변경하지 않는 함수이다.
``` python
def pure_function(x, y):
    return x + y

# 동일한 입력에 대해 항상 동일한 출력 반환
print(pure_function(2, 3))  # 5
print(pure_function(2, 3))  # 5
```

### 순수 함수가 아닌 예시(비순수 함수)
> 그럼 무엇이 함수를 순수하지 못하게 만드는가?
> 
```python
counter = 0

def impure_function_increment():
    global counter
    counter += 1
    return counter

print(impure_function_increment())  # 1
print(impure_function_increment())  # 2 (전역 변수 변경)
```
- 전역 변수를 변경하는 함수

```python
def impure_function_append(lst, value):
    lst.append(value)
    return lst

sample_list = [1, 2, 3]
print(impure_function_append(sample_list, 4))  # [1, 2, 3, 4]
print(impure_function_append(sample_list, 5))  # [1, 2, 3, 4, 5] (원본 리스트 수정)
```
- 리스트를 인플레이스(in-place)로 수정하는 함수

```python
def impure_function_write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
    return True

print(impure_function_write_to_file("sample.txt", "Hello World!"))  # True
print(impure_function_write_to_file("sample.txt", "Hello Again!"))  # True (파일 내용 변경)
```
- 파일에 데이터를 쓰는 함수

```python
import random

def impure_function_random_addition(x):
    return x + random.randint(1, 10)

print(impure_function_random_addition(5))  # 5 + 랜덤 값
print(impure_function_random_addition(5))  # 5 + 랜덤 값 (매번 다른 결과)

```
- 내부적으로 난수를 사용하는 함수
- 동일한 입력에 대해 항상 동일한 출력을 반환X

```python
import time

def impure_function_time_based_greeting(name):
    current_hour = time.localtime().tm_hour
    if current_hour < 12:
        return f"Good morning, {name}!"
    elif current_hour < 18:
        return f"Good afternoon, {name}!"
    else:
        return f"Good evening, {name}!"

print(impure_function_time_based_greeting("Alice"))  # 시간에 따라 다른 인사말
print(impure_function_time_based_greeting("Alice"))  # 시간에 따라 다른 인사말
```
- 내부적으로 시간을 사용하는 함수
- 동일한 입력에 대해 항상 동일한 출력을 반환X


## 2. 불변성(Immutability)
불변성은 데이터가 변경되지 않음을 의미한다. 함수형 프로그래밍에서는 변수의 상태를 변경하지 않고, 새로운 값을 생성하여 반환한다.
``` python
# 예: 불변 리스트를 생성하여 기존 리스트를 변경하지 않고 새 리스트를 반환
original_list = [1, 2, 3]

def add_element(lst, element):
    return lst + [element]

new_list = add_element(original_list, 4)
print(original_list)  # [1, 2, 3]
print(new_list)       # [1, 2, 3, 4]
```

### 불변성을 위반하는 예시

```python
original_list = [1, 2, 3]

def impure_add_element(lst, element):
    lst.append(element)
    return lst

new_list = impure_add_element(original_list, 4)
print(original_list)  # [1, 2, 3, 4]
print(new_list)       # [1, 2, 3, 4] (원본 리스트 수정)
```
- 리스트 요소의 인플레이스 추가

```python
original_dict = {'a': 1, 'b': 2}

def impure_add_entry(d, key, value):
    d[key] = value
    return d

new_dict = impure_add_entry(original_dict, 'c', 3)
print(original_dict)  # {'a': 1, 'b': 2, 'c': 3}
print(new_dict)       # {'a': 1, 'b': 2, 'c': 3} (원본 딕셔너리 수정)
```
- 딕셔너리의 인플레이스 수정

#### 불변성을 유지하는 이점
1. 예측 가능성: 동일한 입력에 대해 항상 동일한 출력을 반환하므로, 함수의 동작을 예측할 수 있다.
2. 디버깅 용이성: 데이터의 상태가 변경되지 않으므로, 특정 시점의 데이터 상태를 쉽게 추적할 수 있다.
3. 병렬 처리: 불변 데이터는 동시에 여러 스레드에서 접근하더라도 안전하므로, 병렬 처리를 용이하게 한다.

### 불변성을 유지하는 방법

```python
def add_entry(d, key, value):
    new_dict = d.copy()
    new_dict[key] = value
    return new_dict
```
- 데이터 복사: 기존 데이터를 변경하지 않고, 새로운 데이터 구조를 생성하여 반환한다.

```python
original_set = frozenset([1, 2, 3])

def add_element(s, element):
    return s.union([element])

new_set = add_element(original_set, 4)
print(original_set)  # frozenset({1, 2, 3})
print(new_set)       # frozenset({1, 2, 3, 4})
```
- 함수형 자료 구조 사용: 함수형 프로그래밍 언어에서 제공하는 불변 자료 구조를 사용한다. 예를 들어, Python의 `frozenset`은 불변 집합을 제공한다.

> 불변성을 유지함으로써 코드의 안전성과 예측 가능성을 높일 수 있다.


## 3. 고차 함수(Higher-Order Function)
고차 함수는 함수를 인수로 받거나, 함수를 반환하는 함수이다. 추상화를 높이는 데 유용하다. map, filter, reduce 등이 예이다.
``` python
# map 예제
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # [1, 4, 9, 16]

# filter 예제
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4]

# reduce 예제
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # 10
```

### 고차 함수의 이점
- 코드 재사용성 증가: 같은 기능을 다양한 상황에서 재사용할 수 있다.
- 추상화: 코드의 추상화 수준을 높여 복잡한 로직을 간단하게 표현할 수 있다.
- 가독성 향상: 코드의 가독성을 높여 이해하기 쉬운 코드를 작성할 수 있다.

## 4. 재귀(Recursion)
함수형 프로그래밍에서는 루프 대신 재귀를 사용하는 경우가 많다.
``` python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120
```

## 5. 익명 함수(Anonymous Function)
익명 함수는 이름이 없는 함수로, lambda 키워드를 사용하여 정의한다.
``` python
# 익명 함수 사용 예제
add = lambda x, y: x + y
print(add(2, 3))  # 5
```

## 6. 클로저(Closure)
클로저는 함수가 자신의 범위 밖에 있는 변수를 기억하고, 접근할 수 있게 하는 기능이다.
``` python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120
```

## 7. 함수 합성(Function Composition)
함수 합성은 여러 함수를 결합하여 새로운 함수를 만드는 것이다.
``` python
def compose(f, g):
    return lambda x: f(g(x))

def double(x):
    return x * 2

def increment(x):
    return x + 1

new_function = compose(double, increment)
print(new_function(3))  # 8 (increment(3) -> 4, double(4) -> 8)

```
## 함수형 프로그래밍 방식의 장점과 단점

### 함수형 프로그래밍(Functional Programming)

함수형 프로그래밍은 상태와 부수 효과를 최소화하고, 순수 함수와 불변 데이터를 강조하는 프로그래밍 패러다임이다. 이 방식은 프로그램을 함수의 조합으로 구성하여 데이터의 흐름을 제어하고, 명령형 프로그래밍과 달리 선언적으로 문제를 해결한다.

### 함수형 프로그래밍의 장점

1. **예측 가능성**: 순수 함수는 동일한 입력에 대해 항상 동일한 출력을 반환하므로, 함수의 동작이 예측 가능하다. 이는 디버깅과 테스트를 쉽게 만든다.
2. **불변성**: 불변 데이터를 사용하면 데이터의 변경이 발생하지 않아, 상태 변화를 추적하기 쉽다. 이는 버그를 줄이고 코드의 안정성을 높인다.
3. **함수 조합**: 작은 함수들을 조합하여 복잡한 동작을 구현할 수 있어, 코드의 재사용성과 모듈화가 용이하다.
4. **병렬 처리 용이**: 부수 효과가 없으므로 병렬 처리와 동시성을 쉽게 구현할 수 있다.
5. **테스트 용이성**: 순수 함수는 외부 상태에 의존하지 않으므로, 독립적으로 테스트할 수 있다. 이는 단위 테스트 작성과 유지보수를 용이하게 한다.
6. **가독성**: 선언형 코드는 무엇을 하는지에 초점을 맞추기 때문에, 코드의 의도를 파악하기 쉽다. 이는 가독성을 높여준다.

### 함수형 프로그래밍의 단점

1. **초기 학습 곡선**: 함수형 프로그래밍은 기존 명령형 프로그래밍과 개념이 다르기 때문에, 초기 학습 곡선이 가파를 수 있다.
2. **성능 문제**: 불변 데이터 구조와 함수의 잦은 복사는 성능에 영향을 미칠 수 있다. 특히, 대규모 데이터 처리를 할 때 성능 저하가 발생할 수 있다.
3. **디버깅 어려움**: 고차 함수와 복잡한 함수 조합으로 인해 디버깅이 어려울 수 있다.
4. **가독성 저하**: 함수형 프로그래밍에 익숙하지 않은 개발자에게는 코드가 난해하고 이해하기 어려울 수 있다.
5. **메모리 사용 증가**: 불변성을 유지하기 위해 데이터 구조를 복사하는 과정에서 메모리 사용량이 증가할 수 있다.
6. **디버깅 도구 부족**: 함수형 프로그래밍을 지원하는 디버깅 도구가 상대적으로 부족하여, 문제 해결이 어려울 수 있다.

## 객체지향 프로그래밍과 함수형 프로그래밍을 대비해서 공통점과 차이점을 정리

### 객체지향 프로그래밍(Object-Oriented Programming, OOP)

객체지향 프로그래밍은 데이터와 데이터를 조작하는 메서드를 하나의 객체로 묶어 프로그램을 구성하는 방식이다. 객체지향 프로그래밍의 주요 개념으로는 클래스, 객체, 상속, 다형성, 캡슐화, 추상화 등이 있다.

### 함수형 프로그래밍(Functional Programming, FP)

함수형 프로그래밍은 상태와 부수 효과를 최소화하고, 순수 함수와 불변 데이터를 강조하는 프로그래밍 패러다임이다. 함수형 프로그래밍은 프로그램을 함수의 조합으로 구성하여 데이터를 처리하고, 명령형 프로그래밍과 달리 선언적으로 문제를 해결한다.

### 공통점

1. **추상화**: 두 패러다임 모두 추상화를 통해 복잡성을 줄이고, 코드의 재사용성을 높인다. OOP는 클래스를 통해 추상화하고, FP는 함수를 통해 추상화한다.
2. **모듈화**: 코드의 모듈화를 통해 유지보수성과 가독성을 높인다. OOP는 객체와 클래스로 모듈화를 하고, FP는 함수와 모듈로 모듈화를 한다.
3. **재사용성**: 코드의 재사용성을 높이는 방법을 제공한다. OOP는 상속과 다형성을 통해, FP는 고차 함수와 함수 조합을 통해 재사용성을 높인다.
4. **캡슐화**: 정보를 숨기고 인터페이스를 통해 접근을 제한하는 개념을 사용한다. OOP는 객체의 속성과 메서드를 캡슐화하고, FP는 클로저를 통해 상태를 캡슐화한다.
5. **테스트 용이성**: 두 패러다임 모두 테스트 용이성을 중요시한다. OOP는 객체의 상태와 행동을 테스트하고, FP는 순수 함수를 테스트하는 방식이다.

### 차이점

1. **상태 관리**
    - **OOP**: 객체의 상태를 변경하면서 동작하는 방식이다. 상태와 행동이 객체 내부에 캡슐화되어 있다.
    - **FP**: 불변성을 유지하면서 상태를 관리한다. 상태를 변경하는 대신 새로운 상태를 생성하여 반환한다.
2. **부수 효과**
    - **OOP**: 객체의 메서드가 객체의 상태를 변경할 수 있다. 이는 부수 효과를 발생시킬 수 있다.
    - **FP**: 순수 함수는 부수 효과가 없으며, 동일한 입력에 대해 항상 동일한 출력을 반환한다.
3. **데이터와 함수의 관계**
    - **OOP**: 데이터와 데이터를 조작하는 메서드를 하나의 객체로 묶는다. 데이터는 객체의 속성으로, 행동은 객체의 메서드로 구현된다.
    - **FP**: 데이터와 함수는 분리되어 있다. 함수는 입력 데이터를 받아서 처리한 후 새로운 데이터를 반환한다.
4. **코드 구조**
    - **OOP**: 클래스와 객체를 중심으로 코드가 구조화된다. 상속, 다형성, 인터페이스를 통해 코드 구조를 구성한다.
    - **FP**: 함수를 중심으로 코드가 구조화된다. 고차 함수, 함수 조합, 커링을 통해 코드 구조를 구성한다.
5. **병렬 처리**
    - **OOP**: 상태가 변경되므로 병렬 처리가 복잡할 수 있다. 동기화와 잠금 메커니즘을 사용해야 할 때가 많다.
    - **FP**: 상태가 불변이므로 병렬 처리가 상대적으로 용이하다. 부수 효과가 없으므로 동기화가 필요 없다.
6. **주요 개념**
    - **OOP**: 클래스, 객체, 상속, 다형성, 캡슐화, 추상화 등.
    - **FP**: 순수 함수, 고차 함수, 불변성, 함수 조합, 커링 등.

## 결론

객체지향 프로그래밍과 함수형 프로그래밍은 서로 다른 철학과 접근 방식을 가지지만, 코드의 재사용성과 유지보수성을 높이기 위해 공통적으로 추구하는 목표를 가지고 있다. 각 패러다임의 장단점을 이해하고, 상황에 맞게 적절히 활용하는 것이 중요하다. 객체지향 프로그래밍은 상태와 행동을 객체로 묶어 관리하고, 함수형 프로그래밍은 순수 함수와 불변성을 통해 예측 가능한 코드를 작성하는 데 중점을 둔다. 두 패러다임을 적절히 조합하면 더욱 강력하고 유연한 코드를 작성할 수 있다.