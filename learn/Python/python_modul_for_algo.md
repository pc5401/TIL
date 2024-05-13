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
