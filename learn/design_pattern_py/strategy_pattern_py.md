# 🎯 Strategy Pattern — “행동을 갈아끼우는” 디자인 패턴 노트

> **목적**
> “알고리즘(행동)을 **캡슐화**해 런타임에 **교체**할 수 있게 한다.”
> `if‐elif` 바다나 상속 폭발 대신 **객체 조합**으로 유연성 확보!

---

## 1. 등장 배경 & 실무 감각

| 시나리오                  | 문제점                           |
| --------------------- | ----------------------------- |
| 결제 시스템 – 카드/계좌/포인트    | `if payment_type == …` 조건문 난무 |
| 압축 유틸 – ZIP/LZMA/Gzip | 새 알고리즘 추가 때마다 클래스 수정          |
| AI 게임 – 초보/중급/프로 AI   | 난이도별 로직이 서로 뒤엉킴               |

전략 패턴으로 **동일 인터페이스 + 교체 가능한 객체**로 분리한다.

---

## 2. 구조

```
Context (Payment) ── has ──▶ Strategy (PayStrategy)
                               ▲            ▲
                               │            │
                     ConcreteStrategyA  ConcreteStrategyB
```

* **Context** : 전략 **객체를 보유**해 필요 시 호출.
* **Strategy** : 행동(알고리즘) 인터페이스.
* **ConcreteStrategy** : 실제 구현 A, B, C …

---

## 3. Python 예제 – **정렬 알고리즘 스위치**

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint

# 1) Strategy interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]: ...


# 2) Concrete strategies
class QuickSort(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[0]
        left  = [x for x in data[1:] if x < pivot]
        right = [x for x in data[1:] if x >= pivot]
        return self.sort(left) + [pivot] + self.sort(right)

class BubbleSort(SortStrategy):
    def sort(self, data):
        arr = data[:]           # 얕은 복사
        for i in range(len(arr)):
            for j in range(len(arr)-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


# 3) Context
class DataSet:
    def __init__(self, data: list[int], strategy: SortStrategy):
        self._data = data
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self):
        print(f"▶  Using {self._strategy.__class__.__name__}")
        self._data = self._strategy.sort(self._data)
        return self._data


# 4) Client
if __name__ == "__main__":
    nums = [randint(0, 99) for _ in range(10)]
    ds = DataSet(nums, QuickSort())
    print(ds.sort())            # 퀵정렬

    ds.set_strategy(BubbleSort())
    print(ds.sort())            # 버블정렬 (학습/디버그용)
```
