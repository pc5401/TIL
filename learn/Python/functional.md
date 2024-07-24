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

## 3. 고차 함수(Higher-Order Function)
고차 함수는 함수를 인수로 받거나, 함수를 반환하는 함수이다. map, filter, reduce 등이 예이다.
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
