# 알고리듬을 위한 파이썬 모듈들

## math

math 모듈은 수학적인 함수와 상수를 제공한다. (그냥 파이썬 문법이 쌀집 계산기이면 math 쓰면 공학용 계산기다!!) 

1. `sqrt(x)`: x의 제곱근을 반환
   
   ```python
   import math
   
   print(math.sqrt(16))  # 4.0
   ```

2. `pow(x, y)`: x의 y제곱을 반환
   
   ```python
   import math
   
   print(math.pow(2, 3))  # 2의 3 승 ->  8.0
   ```

3. `factorial(x)`: x의 팩토리얼 값을 반환
   
   ```python
   import math
   
   print(math.gcd(60, 48))  # 12
   ```

4. `ceil(x)`와 `floor(x)`: 각각 x의 올림값과 내림값을 반환
   
   ```python
   import math
   
   print(math.ceil(2.3))  # 3
   print(math.floor(2.3))  # 2
   # round 함수는 반올림
   print(round(2.3)) # 2
   print(round(2.5)) # 3
   # int 형으로 하면 그냥 소수점을 삭제한다. 
   print(int(3.7))  # 결과: 3
   #int는 양수 일때는 floor와 결과가 동일하지만, 음수에서는 floor와 다름!!
   print(int(-3.7))  # 결과: -3
   print(math.floor(-3.7))  # 결과: -4
   ```

5. `log(x[, base])`: base가 주어지면 log_base(x)를, 그렇지 않으면 자연로그 log_e(x)를 반환
   
   ```python
   import math
   
   print(math.log(100, 10))  # 2.0
   print(math.log(2.71828))  # 1.0 (approximately)
   ```

6. `sin(x)`,` cos(x)`,` tan(x)`: 각각 x의 사인, 코사인, 탄젠트 값을 반환
   
   ```python
   import math
   
   print(math.sin(math.pi / 2))  # 1.0
   print(math.cos(math.pi))  # -1.0
   print(math.tan(math.pi / 4))  # 1.0
   ```

7. `pi`, `e`: 원주율(pi)와 자연상수(e)의 값을 제공
   
   ```python
   import math
   
   print(math.pi)  # 3.141592653589793
   print(math.e)  # 2.718281828459045
   ```

8. `gcd(x, y)`: x와 y의 최대공약수(GCD)를 반환
   
   ```python
   import math
   
   print(math.gcd(60, 48))  # 12
   ```

## itertools

- ineration + tools 의 합성어로 Python의 itertools 모듈은 효과적인 반복을 위한 여러 가지 함수를 제공한다.

- 이터레이션은 결과를 생성하기위한 프로세스의 반복
1. `itertools.permutations(iterable, r=None)`: 입력 iterable에서 r 개의 원소를 선택하여 순서를 고려한 순열을 생성한다. 만약 r이 지정되지 않으면, 모든 원소를 사용한 순열을 반환한다.
   
   ```python
   import itertools
   
   for p in itertools.permutations('ABC', 2):
       print(p)
   
   # 출력: ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')
   ```

2. `itertools.combinations(iterable, r)`: 입력 iterable에서 r 개의 원소를 선택하여 순서를 고려하지 않은 조합을 생성
   
   ```python
   import itertools
   
   for c in itertools.combinations('ABC', 2):
       print(c)
   
   # 출력: ('A', 'B'), ('A', 'C'), ('B', 'C')
   ```

3. `itertools.product(*iterables, repeat=1)`: 입력 iterables의 카르테시안 곱을 반환한다. repeat은 iterables가 반복되는 횟수를 지정하는 것
   
   ```python
   import itertools
   
   for p in itertools.product('AB', repeat=2):
       print(p)
   
   # 출력: ('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')
   ```

4. `itertools.chain(*iterables)`: 여러 iterables를 하나의 iterator로 결합
   
   ```python
   import itertools
   
   for c in itertools.chain('ABC', '123'):
       print(c)
   
   # 출력: 'A', 'B', 'C', '1', '2', '3'
   ```

5. `itertools.cycle(iterable)`: iterable의 원소들을 무한히 반복한다. 계속 돈다.
   
   ```python
   import itertools
   
   c = itertools.cycle('AB')
   for i in range(6):
       print(next(c))
   
   # 출력: 'A', 'B', 'A', 'B', 'A', 'B'
   ```

## collections

> Python의 **`collections`** 모듈은 다양한 유형의 데이터 컨테이너를 제공하며, 이 중 몇 가지는 코딩 테스트에서 특히 유용하다:

1. **`collections.Counter(iterable)`**: iterable의 원소들을 세어서, 각 원소를 키로 하고 그 개수를 값으로 하는 딕셔너리를 생성한다. 이 클래스는 원소의 빈도 수를 세는 데 매우 유용함.
   
   ```python
   from collections import Counter
   
   c = Counter('abcabc')
   print(c)  # 출력: Counter({'a': 2, 'b': 2, 'c': 2})
   ```

2. **`collections.defaultdict(default_type)`**: 디폴트 딕셔너리는 키가 없을 경우에 주어진 default_type의 기본값을 반환.
   
   ```python
   from collections import defaultdict
   
   d = defaultdict(int)
   print(d['key'])  # 출력: 0
   ```

3. **`collections.deque`**: 양쪽 끝에서 빠르게 추가 및 제거를 할 수 있는 큐를 구현한다. 스택과 큐의 기능을 모두 갖추고 있어 유용하다. `bfs` , `queue`, `우선순위 큐` 등에서 활용
   
   ```python
   from collections import deque
   
   dq = deque([1, 2, 3])
   dq.append(4)  # 끝에 추가
   dq.appendleft(0)  # 앞에 추가
   print(dq)  # 출력: deque([0, 1, 2, 3, 4])
   ```

4. **`collections.namedtuple(typename, field_names)`**: 각 필드에 이름을 부여할 수 있는 튜플의 서브클래스를 생성한다.
   
   ```python
   from collections import namedtuple
   
   Point = namedtuple('Point', ['x', 'y'])
   p = Point(11, 22)
   print(p.x, p.y)  # 출력: 11 22
   ```

5. **`collections.OrderedDict`**: 키의 추가 순서를 기억하는 딕셔너리.
   
   ```python
   from collections import OrderedDict
   
   od = OrderedDict()
   od['a'] = 1
   od['b'] = 2
   od['c'] = 3
   print(od)  # 출력: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
   ```

# **heapq**

> Python의 **`heapq`** 모듈은 힙 자료구조를 제공한다. 힙은 완전 이진 트리의 일종으로, 우선순위 큐를 구현하는 데 사용된다.

1. **`heapq.heappush(heap, item)`**: 힙에 새로운 요소를 추가한다.
   
   ```python
   import heapq
   
   h = []
   heapq.heappush(h, (5, 'write code'))
   heapq.heappush(h, (7, 'release product'))
   heapq.heappush(h, (1, 'write spec'))
   heapq.heappush(h, (3, 'create tests'))
   print(h)
   # 출력: [(1, 'write spec'), (3, 'create tests'), (5, 'write code'), (7, 'release product')]
   ```

2. **`heapq.heappop(heap)`**: 힙에서 가장 작은 요소를 제거하고 그 요소를 반환한다. 이것은 힙의 주요 기능인 '최솟값 추출'을 구현한다.
   
   ```python
   import heapq
   
   h = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
   heapq.heapify(h)
   print(heapq.heappop(h))  # 출력: 0
   ```

3. **`heapq.heapify(x)`**: 주어진 리스트 x를 즉시 힙으로 변환한다 (선형 시간).
   
   ```python
   import heapq
   
   h = [3, 5, 1, 4, 6, 7, 2, 0, 8, 9]
   heapq.heapify(h)
   print(h)  # 출력: [0, 2, 1, 4, 3, 7, 5, 3, 8, 9]
   ```

4. **`heapq.heapreplace(heap, item)`**: 힙에서 가장 작은 요소를 제거하고 새로운 item을 추가한다. 이 함수는 한 번의 연산으로 이 두 가지 작업을 수행하므로, heappop() 후 heappush()를 호출하는 것보다 더 효율적이다.
   
   ```python
   import heapq
   
   h = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
   heapq.heapify(h)
   heapq.heapreplace(h, -5)
   print(h)  # 출력: [-5, 0, 2, 4, 1, 3, 5, 6, 8, 9]
   ```

5. `heapq.nlargest(n, iterable[, key])`**와 `heapq.nsmallest(n, iterable[, key])`**: 데이터에서 가장 큰 n 개의 요소, 또는 가장 작은 n 개의 요소를 반환한.
   
   ```python
   import heapq
   
   nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
   print(heapq.nlargest(3, nums))  # 출력: [42, 37, 23]
   print(heapq.nsmallest(3, nums))  # 출력: [-4, 1, 2]
   ```

# **`bisect`**

> Python의 **`bisect`** 모듈은 이진 검색과 정렬된 리스트에 대한 요소 삽입을 제공합니다.

⚠️ **`bisect`** 모듈은 리스트가 이미 정렬되어 있는 경우에만 작동한다는 점을 명심

- **`bisect`** 모듈은 큰 데이터 집합에서 아이템을 빠르게 찾는 데 특히 유용하며, 리스트를 다시 정렬할 필요 없이 아이템을 삽입할 수 있다는 장점이 있습니다. 이러한 특성 때문에, **`bisect`** 모듈은 효율적인 코드 작성 및 알고리즘 최적화에 주로 사용
1. **`bisect.bisect_left(a, x, lo=0, hi=len(a))`**: 정렬된 순서를 유지하면서 리스트 a에 x를 삽입할 왼쪽 인덱스를 찾습니다. 즉, 리스트의 왼쪽부터 시작하여 x와 같거나 큰 첫 번째 요소의 인덱스를 반환합니다.
   
   ```python
   import bisect
   
   nums = [1, 3, 4, 4, 6, 8]
   print(bisect.bisect_left(nums, 4))  # 출력: 2
   ```

2. **`bisect.bisect_right(a, x, lo=0, hi=len(a))`** 또는 **`bisect.bisect(a, x, lo=0, hi=len(a))`**: 정렬된 순서를 유지하면서 리스트 a에 x를 삽입할 오른쪽 인덱스를 찾습니다. 즉, 리스트의 왼쪽부터 시작하여 x보다 큰 첫 번째 요소의 인덱스를 반환합니다.
   
   ```python
   import bisect
   
   nums = [1, 3, 4, 4, 6, 8]
   print(bisect.bisect(nums, 4))  # 출력: 4
   ```

3. **`bisect.insort_left(a, x, lo=0, hi=len(a))`**: x를 a에 오름차순으로 삽입합니다. a는 이미 정렬되어 있어야 합니다. x가 a에 이미 있으면, 삽입 위치는 기존 항목 앞(왼쪽)이 됩니다.
   
   ```python
   import bisect
   
   nums = [1, 3, 4, 4, 6, 8]
   bisect.insort_left(nums, 5)
   print(nums)  # 출력: [1, 3, 4, 4, 5, 6, 8]
   ```

4. **`bisect.insort_right(a, x, lo=0, hi=len(a))`** 또는 **`bisect.insort(a, x, lo=0, hi=len(a))`**: x를 a에 오름차순으로 삽입합니다. a는 이미 정렬되어 있어야 합니다. x가 a에 이미 있으면, 삽입 위치는 기존 항목 뒤(오른쪽)가 됩니다.

# **`functools`**

> **`functools`** 모듈은 **고차 함수**와 **콜러블 객체**에 대한 연산을 위한 것으로, 주로 함수를 조작하거나 관리하는 데 사용됩니다.

- 고차 함수
  
  - 고차 함수는 다른 함수를 인수로 받거나 결과로 반환하는 함수를 의미.
  
  - Python에서는 함수를 일급 객체로 취급하기 때문에, 고차 함수를 사용하는 것이 가능
  
  - 고차 함수는 코드의 가독성과 재사용성을 높이며, 함수형 프로그래밍 패러다임을 구현하는 데 사
    
    ### 예시 )
  1. 함수를 인자로 받는 경우: 고차 함수는 다른 함수를 인자로 받을 수 있습니다. 이를 통해, 특정 로직을 공통 함수로 작성하고, 그 함수를 다양한 함수에 적용하여 코드 중복을 줄일 수 있습니다. **`map`**, **`filter`**, **`reduce`** 등이 이에 해당합니다.
     
      예를 들어, **`map`** 함수는 함수와 리스트를 인자로 받아 리스트의 모든 요소에 함수를 적용한 결과를 반환합니다.
     
     ```python
     def square(x):
         return x ** 2
     
     numbers = [1, 2, 3, 4, 5]
     result = map(square, numbers)
     print(list(result))  # 출력: [1, 4, 9, 16, 25]
     ```
  
  2. 함수를 반환하는 경우: 고차 함수는 함수를 결과로 반환할 수 있습니다. 이를 통해, 필요에 따라 동적으로 함수를 생성하거나 수정할 수 있습니다.
     
      예를 들어, 함수를 반환하는 함수를 만들어보겠습니다:
     
     ```python
     -def make_multiplier(n):
         def multiplier(x):
             return x * n
         return multiplier
     
     times_two = make_multiplier(2)
     print(times_two(4))  # 출력: 8
     
     times_three = make_multiplier(3)
     print(times_three(4))  # 출력: 12
     ```
     
      여기서 **`make_multiplier`**는 고차 함수입니다. 이 함수는 **`multiplier`**라는 새로운 함수를 생성하고 반환합니다. 생성된 **`multiplier`** 함수는 **`make_multiplier`**에 전달된 인자에 따라 다르게 작동합니다.

- 콜러블 객체
  
  - 콜러블(Callable) 객체는 Python에서 "호출 가능"한 객체를 뜻함
  
  - 콜러블 객체는 호출 연산자인 괄호 **`()`**를 사용하여 호출
  
  - 어떤 종류의 연산이든 정의 가능
    
    ### 예시)
  1. **함수(Function)**: 함수는 가장 많이 사용되는 콜러블 객체입니다. 사용자 정의 함수뿐만 아니라 Python 내장 함수도 포함됩니다.
     
     ```python
     def call_me():
         print("Called!")
     
     call_me()  # 출력: "Called!"
     ```
  
  2. **메서드(Method)**: 클래스의 인스턴스에 바인딩된 함수를 말합니다.
     
     ```python
     class CallableClass:
         def call_me(self):
             print("Called!")
     
     instance = CallableClass()
     instance.call_me()  # 출력: "Called!"
     ```
  
  3. **클래스(Class)**: 클래스도 콜러블입니다. 클래스를 호출하면 그 결과로 해당 클래스의 인스턴스가 생성됩니다.
     
     ```python
     class CallableClass:
         def __init__(self):
             print("Instance Created!")
     
     instance = CallableClass()  # 출력: "Instance Created!"
     ```
  
  4. **클래스 인스턴스(Class Instances)**: 클래스 인스턴스는 그 클래스에 **`__call__`** 메서드가 구현되어 있을 때 콜러블합니다.
     
     ```python
     class CallableClass:
         def __call__(self):
             print("Instance Called!")
     
     instance = CallableClass()
     instance()  # 출력: "Instance Called!"
     ```
  
  5. **제너레이터(Generator)**: 제너레이터 함수는 호출될 때마다 일련의 값을 생성하는 콜러블입니다.
     
      콜러블 객체인지 확인하는 방법은 내장 함수인 **`callable()`**을 사용하면 됩니다.
     
     ```python
     print(callable(call_me))  # 출력: True
     print(callable(CallableClass))  # 출력: True
     print(callable(instance))  # 출력: True
     ```
1. **`functools.partial(func, *args, **keywords)`**: 부분 적용 함수를 생성합니다. 즉, 하나 이상의 인자를 이미 고정한 함수의 새 버전을 만듭니다.

```python
from functools import partial

def add(a, b):
    return a + b
add_five = partial(add, 5)
print(add_five(3))  # 출력: 8
```

2. **`functools.lru_cache(maxsize=128, typed=False)`**: 이 데코레이터는 최근에 사용한 입력과 그 결과를 캐시하므로 이전에 계산한 결과를 재사용할 수 있습니다. 동적 프로그래밍 문제에 유용합니다.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(10))  # 출력: 55
```

3. **`functools.reduce(function, iterable[, initializer])`**: 누적적으로 iterable의 항목에 function을 적용하여 하나의 출력을 만듭니다.

```python
from functools import reduce

print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))  # 출력: 120
```

4. **`functools.total_ordering`**: 이 클래스 데코레이터는 클래스가 비교 메서드 중 하나(**`__lt__`**, **`__le__`**, **`__gt__`**, **`__ge__`**)와 **`__eq__`** 메서드를 제공하면 나머지 비교 메서드를 자동으로 추가해줍니다.

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
    def __lt__(self, other):
        return self.name < other.name
```