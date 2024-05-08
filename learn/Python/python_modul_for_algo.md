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
