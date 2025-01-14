# BOJ 1528 금민수의 합
참고 링크
https://www.acmicpc.net/problem/1528

금민수는 4와 7로만 이루어진 수를 의미한다. 예를 들어, 4, 7, 44, 47, 74, 77, 444 등이 있다.

N(1 ≤ N ≤ 1,000,000)을 입력받아, 금민수의 합으로 N을 만들 수 있는 방법 중 다음 조건을 만족하는 해를 구하는 문제이다.

1. 사용할 금민수의 개수가 최소여야 한다.
2. 같은 개수라면, 사전순으로 앞서는 해를 출력한다.
3. 만들 수 없다면 -1을 출력한다.

아래 코드는 BFS(너비 우선 탐색)를 사용해 풀이했다. BFS를 사용할 때, 중간 경로(=사용한 수 전체)를 큐에 넣지 않고,

- `predecessor[x]`: x라는 합을 만들기 직전에 만들었던 합
- `choice[x]`: x라는 합을 만들 때 사용한 금민수

이 두 배열을 이용해 경로를 역추적(backtrack)한다. 이렇게 하면 메모리를 절약할 수 있고, N에 도달했을 때 즉시 답을 얻을 수 있다.

---

## 접근 방식

1. **금민수 목록 생성**
    - N의 자릿수를 기준으로 1자리부터 최대 6자리(왜냐하면 1,000,000 이하이므로 7자리 금민수는 고려하지 않아도 됨)까지 모든 금민수를 만든다.
    - 이 금민수 후보들을 오름차순으로 정렬한다(코드에서는 생성 후 바로 쓰이기 때문에, 필요 시 정렬 가능).
2. **BFS로 탐색**
    - `0`부터 시작해서, 현재 합 `curr_val`에 가능한 금민수를 더해 `next_val`을 만든다.
    - 아직 방문하지 않은 `next_val`이면, `predecessor[next_val]`와 `choice[next_val]`를 설정하고 `visited[next_val]`를 True로 만든 뒤 큐에 넣는다.
    - `next_val`이 N에 도달하면 즉시 역추적으로 답을 복원하고 종료한다.
3. **경로 복원**
    - `predecessor[N]`부터 시작해서 0에 이를 때까지 역추적한다.
    - `choice[x]`가 “x를 만들기 위해 사용한 금민수”이므로, 이를 모아 뒤집으면 (개수 최소 + 사전순 앞선) 해가 완성된다.
4. **결과**
    - 만들 수 있으면 금민수를 순서대로 출력한다.
    - 만들 수 없으면 -1을 출력한다.

---

## 초기 코드(경로 복원 사용X)

처음에는 금민수를 생성하고 bfs로 접근했다. 당연하게도 메모리와 시간이 초과 되었다.

```python
import sys
import collections
input = sys.stdin.readline

def get_number(length: int) -> list[int]:
    if length >= 7:
        length = 6
    rtn = []

    for bitmask in range(1 << length):
        num_str = ""
        # 각 비트를 확인하며 0이면 '4', 1이면 '7'
        for j in range(length):
            if bitmask & (1 << j):
                num_str = "7" + num_str
            else:
                num_str = "4" + num_str
        rtn.append(int(num_str))

    return rtn

def solve(n: int, numbers: list[int]) -> int:
    Q = collections.deque([i] for i in range(len(numbers)))
    

    while Q:
        lst = Q.popleft()
        sumV = 0

        for i in lst:
            sumV += numbers[i]
        
        for i in range(i, len(numbers)):
            if sumV + numbers[i] == n:
                lst.append(i)
                return [numbers[i] for i in lst]
            elif sumV + numbers[i] < n:
                new_lst = lst[:]
                new_lst.append(i)
                Q.append(new_lst)

    return [-1]

if __name__=="__main__":
    # 입력
    N = input().rstrip()

    # 풀이
    numbers = []
    for i in range(1, len(N)+1):
        numbers.extend(get_number(i))
    result = solve(int(N), numbers)
    
    # 출력
    print(*result)
```

이후 풀이를 연구한 결과 **경로 복원 방식에 대해서 알게 되었다. 유니온 파인드와 비슷한 원리라고 느꼈다.**

## 전체 코드

```python
import sys
import collections
input = sys.stdin.readline

def get_number(length: int) -> list[int]:
    # 최대 6자리까지만 생성
    if length >= 7:
        length = 6
    rtn = []
    for bitmask in range(1 << length):
        num_str = ""
        # 각 비트를 확인하며 0이면 '4', 1이면 '7'
        for j in range(length):
            if bitmask & (1 << j):
                num_str = "7" + num_str
            else:
                num_str = "4" + num_str
        rtn.append(int(num_str))
    return rtn

def backtrack(N, predecessor, choice):
    # predecessor[N] == -1이면 N을 만들 수 없음을 의미
    if predecessor[N] == -1:
        return [-1]

    result = []
    cur = N
    while cur != 0:
        result.append(choice[cur])
        cur = predecessor[cur]

    result.reverse()
    return result

def solve(n: int, numbers: list[int]) -> list[int]:
    predecessor = [-1] * (n+1)
    choice = [-1] * (n+1)
    visited = [False] * (n+1)

    Q = collections.deque()
    Q.append(0)
    visited[0] = True

    while Q:
        curr_val = Q.popleft()
        for num in numbers:
            next_val = curr_val + num
            # N보다 커지면 break
            if next_val > n:
                break
            if not visited[next_val]:
                visited[next_val] = True
                predecessor[next_val] = curr_val
                choice[next_val] = num
                Q.append(next_val)
                if next_val == n:
                    # N에 도달하면 바로 경로 복원
                    return backtrack(n, predecessor, choice)

    return [-1]

if __name__=="__main__":
    N = input().rstrip()
    n_int = int(N)

    # 생성 가능한 금민수 모으기
    numbers = []
    for i in range(1, len(N)+1):
        numbers.extend(get_number(i))
    numbers.sort()

    # BFS 풀이
    result = solve(n_int, numbers)

    # 출력
    print(*result)
```

---

## 풀이 과정 요약

1. **금민수 생성**
    - 1부터 len(N)까지 비트마스크를 사용해 ‘4’와 ‘7’의 모든 조합을 만든다.
    - 예를 들어 2자리라면, (4,4), (4,7), (7,4), (7,7)에 해당하는 44, 47, 74, 77 등을 생성한다.
2. **BFS 초기화**
    - `0`에서 시작한다(`visited[0] = True`).
    - 큐에는 합(=정수)만을 넣는다.
3. **확장**
    - 큐에서 하나씩 꺼내서, 금민수를 더해 새로운 합을 만든다.
    - 아직 방문하지 않은 합이면, `predecessor`와 `choice`를 기록하고 큐에 넣는다.
4. **목표 도달**
    - 합이 N에 도달하면, 즉시 `backtrack` 함수를 이용해 경로를 추적하고 반환한다.
5. **불가능한 경우**
    - BFS를 전부 탐색해도 N에 도달하지 못하면 -1을 출력한다.

---

## 깨달음

- **BFS에서 경로 전체를 큐에 담으면 메모리를 많이 사용한다**
    
    따라서, `predecessor` 배열을 사용해 방금 전 상태만 저장하고, 결과가 나오면 역추적하는 방식을 이용한다.
    
- **금민수는 6자리까지만 고려하면 충분하다**
    
    N이 최대 1,000,000이므로, 7자리 금민수는 최소가 4,444,444 > 1,000,000이 되어 버린다.
    
- **사전순 우선 탐색**
    
    금민수를 생성한 뒤 정렬하면, BFS에서 자연스럽게 사전순이 보장된다.
    
- **시간 복잡도와 메모리**
    
    N이 최대 1,000,000일 때, 각 상태마다 6자리 이하 금민수를 모두 시도하므로, 최악의 경우가 다소 크다.
    
    그래도 `predecessor`와 `choice` 배열을 이용하면, 큐에 담기는 것은 `N+1`개 상태가 최대치이다.
    
    파이썬에서 시간과 메모리를 잘 관리해야 한다.
    

---

## 마무리

- BFS + 역추적(predecessor) 방식을 통해 메모리를 크게 아낄 수 있었다.
- 금민수를 생성할 때 비트마스크를 사용하면 간편하게 4, 7 조합을 만들 수 있다.
- 최소 개수를 우선하는 BFS, 그리고 사전순을 보장하는 정렬된 금민수를 차례로 시도함으로써 문제 요구사항을 충족한다.