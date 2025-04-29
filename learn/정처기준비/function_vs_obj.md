## 함수형 프로그래밍 핵심 노트 🧩
_파이썬 예제 중심, 개념·예시·장단점을 모두 담은 한 곳 정리_

---

### 목차
1. 함수형 프로그래밍이란?  
2. 핵심 개념  
    2-1. 순수 함수  
    2-2. 불변성  
    2-3. 고차 함수  
    2-4. 재귀  
    2-5. 익명 함수  
    2-6. 클로저  
    2-7. 함수 합성  
3. 장 점 vs 단 점  
4. OOP vs FP 비교  
5. 실무 활용 가이드  

---

## 1. 함수형 프로그래밍이란?
- **정의** : 프로그램을 _값을 계산하는 **함수**의 조합_ 으로 표현하는 패러다임.  
- **목표** : 부수 효과 최소화, 예측 가능성 극대화, 선언형 데이터 흐름.  
- **Python** : OOP 언어이지만 `lambda`, `map / filter`, `functools`, 불변 자료구조로 FP 스타일을 지원.

---

## 2. 핵심 개념

### 2-1. 순수 함수 (Pure Function)
| 규칙 | 설명 |
| :-- | :-- |
| **① 동일 입력 → 동일 출력** | 시간·난수·글로벌 상태 X |
| **② 부수 효과 0** | 파일/DB/전역 변수 변경 X |

```python
def pure_add(x: int, y: int) -> int:
    return x + y
```

<details>
<summary>비순수 예 (전역 상태·I/O·랜덤·시간)</summary>

```python
import random, time, pathlib
counter = 0

def impure():
    global counter
    counter += 1                 # 전역 변경
    pathlib.Path("log.txt").write_text("hit")  # I/O
    return counter + random.randint(0, 5) + time.time()
```
</details>

---

### 2-2. 불변성 (Immutability)
- **의미** : 생성된 데이터는 변경되지 않는다.  
- **이점** :  
  1. 상태 추적·디버깅 용이  
  2. 스레드 안전 → 병렬 처리 부담 ↓  
  3. 참조 투명성 확보

```python
orig = (1, 2, 3)                # 튜플은 불변
def add_item(seq, item):
    return (*seq, item)

print(orig)          # (1, 2, 3)
print(add_item(orig, 4))  # (1, 2, 3, 4)
```

불변 컬렉션 예 : 튜플, `frozenset`, `types.MappingProxyType`, `pyrsistent` 패키지.

---

### 2-3. 고차 함수 (Higher-Order Function)
> **함수를 인수로 받거나, 함수를 반환**

```python
from functools import reduce
nums = [1, 2, 3, 4]

squares = list(map(lambda x: x**2, nums))
evens   = list(filter(lambda x: x % 2 == 0, nums))
total   = reduce(lambda a, b: a + b, nums)
```
- **재사용** ↑, **추상화** ↑, **코드량** ↓

---

### 2-4. 재귀 (Recursion)
```python
def fact(n: int) -> int:
    return 1 if n == 0 else n * fact(n - 1)
```
> **꼬리 재귀 최적화**는 CPython에 없으므로 큰 깊이에서는 반복·스택 제한에 주의.

---

### 2-5. 익명 함수 (Lambda)
```python
add = lambda a, b: a + b
print((lambda x: x**2)(5))
```
- 한 줄 연산·고차 함수 인수로 간결 사용.  
- 복잡 로직 → `def`로 명시.

---

### 2-6. 클로저 (Closure)
> 내부 함수가 **자신을 둘러싼 스코프의 변수**를 기억

```python
def make_pow(exp):
    def power(base):            # exp를 기억
        return base ** exp
    return power

square, cube = make_pow(2), make_pow(3)
print(square(4), cube(2))       # 16 8
```

---

### 2-7. 함수 합성 (Function Composition)
```python
def compose(f, g):
    return lambda x: f(g(x))

def inc(x):     return x + 1
def double(x):  return x * 2

inc_then_double = compose(double, inc)
print(inc_then_double(3))       # 8
```
> `functools.partial` · `operator.methodcaller`로 **커링**·부분 적용도 가능.

---

## 3. 함수형 패러다임 — 장·단점

| | 장점 | 단점 |
| :-- | :-- | :-- |
| **FP** | 예측 가능, 테스트·병렬·리팩터 친화 | 학습 곡선, 불변 복사 비용, 디버깅 난해 |
| **OOP** | 현실 모델·상태 캡슐화 | 공유 상태 → 버그, 동시성 복잡 |

---

## 4. OOP vs FP 비교 표

| 구분 | 객체지향(OOP) | 함수형(FP) |
| :-- | :-- | :-- |
| **단위** | 객체(데이터+행동) | 순수 함수 |
| **상태** | 가변 (메서드로 변경) | 불변 (새 인스턴스 반환) |
| **재사용** | 상속·다형성 | 합성·고차 함수 |
| **부수 효과** | 일반적 | 최소화 |
| **병렬 처리** | 락·동기화 필요 | 비교적 안전 |
| **주요 키워드** | 클래스, self, encapsulation | lambda, map/filter/reduce, immutable |

---

## 5. 실무 활용 가이드

1. **비즈니스 로직** → 가능하면 순수 함수·불변 자료구조.  
2. **I/O·DB·로그**는 **경계 어댑터**로 모아 부수 효과 격리.  
3. `dataclasses.replace`, `typing.NamedTuple`, `pydantic`(immutable=True) 등으로 파이썬에서 불변 지원.  
4. OOP 도메인 객체에 FP 유틸(합성·고차 함수) 투입 ⇒ 가독성·테스트성 급상승.  
5. 병렬 처리 시 `multiprocessing.Pool(map)` / `concurrent.futures` + 불변 데이터 구조.

---

### 핵심 한 줄
> **순수 함수 + 불변 데이터 + 합성** — 세 가지만 지켜도 버그는 줄고, 테스트·병렬 처리는 훨씬 수월해진다.