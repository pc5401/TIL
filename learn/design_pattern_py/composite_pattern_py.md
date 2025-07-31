# 🌳 Composite Pattern — “트리 구조(부분-전체)를 한 타입으로 다루기”

> **의도**
> 객체들을 **트리 구조(부분-전체, part–whole)** 로 구성하고, **개별 객체(Leaf)** 와 **복합 객체(Composite)** 를 **같은 인터페이스**로 다루게 한다.

---

## 1. 언제 쓰나?

| 상황                | 문제                              | Composite로 해결                             |
| ----------------- | ------------------------------- | ----------------------------------------- |
| **파일 시스템**: 파일/폴더 | 파일과 폴더 API가 달라서 분기(`if is_dir`) | `Component` 하나로 `size()`, `render()` 등 통일 |
| **GUI 위젯 트리**     | 컨테이너/위젯이 서로 다른 방식으로 처리          | `draw()` 같은 공통 동작을 재귀 호출                  |
| **수식 트리(AST)**    | 노드 타입별 연산 중복                    | 공통 인터페이스 + 재귀 처리                          |

---

## 2. 구조 (텍스트)

```
Client
  │
  ▼
Component (공통 인터페이스)
  ├─ Leaf        (자식 없음)
  └─ Composite   (자식 보유, 재귀적으로 Component 호출)
```

* **Component**: 공통 연산(API) 정의
* **Leaf**: 실제 동작 구현. 자식 X
* **Composite**: 자식 목록을 보유하고, **자식에게 연산 위임(재귀)**

---

## 3. Python 예제 — 파일/디렉터리 트리

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# ---------- Component ----------
class FileSystemNode(ABC):
    @abstractmethod
    def size(self) -> int: ...
    @abstractmethod
    def show(self, indent: int = 0) -> None: ...


# ---------- Leaf ----------
class File(FileSystemNode):
    def __init__(self, name: str, bytes_: int) -> None:
        self.name = name
        self._bytes = bytes_

    def size(self) -> int:
        return self._bytes

    def show(self, indent: int = 0) -> None:
        print(" " * indent + f"📄 {self.name} ({self._bytes}B)")


# ---------- Composite ----------
class Directory(FileSystemNode):
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: List[FileSystemNode] = []

    def add(self, node: FileSystemNode) -> None:
        self.children.append(node)

    def remove(self, node: FileSystemNode) -> None:
        self.children.remove(node)

    def size(self) -> int:
        return sum(child.size() for child in self.children)

    def show(self, indent: int = 0) -> None:
        print(" " * indent + f"📁 {self.name}/")
        for child in self.children:
            child.show(indent + 2)


# ---------- Client ----------
if __name__ == "__main__":
    root = Directory("root")
    src = Directory("src")
    assets = Directory("assets")

    root.add(src)
    root.add(assets)
    src.add(File("main.py", 1200))
    src.add(File("utils.py", 800))
    assets.add(File("logo.png", 102400))

    root.show()
    print("Total size:", root.size(), "bytes")
```

**출력 예시**

```
📁 root/
  📁 src/
    📄 main.py (1200B)
    📄 utils.py (800B)
  📁 assets/
    📄 logo.png (102400B)
Total size: 104400 bytes
```

---

## 4. “안전(safe) vs 투명(transparent)” 인터페이스

* **투명(Transparent)**: `Component` 에 `add/remove` 까지 포함 → Leaf에서도 호출 가능(보통 `NotImplementedError` 던짐).

  * 장점: 클라이언트는 항상 같은 API 호출
  * 단점: Leaf가 의미 없는 메서드를 가진다
* **안전(Safe)**: `add/remove` 는 `Composite` 에만 둔다.

  * 장점: 타입 안전
  * 단점: 클라이언트가 Composite 타입을 알아야 함

위 예시는 **안전(Safe)** 쪽 (Leaf에는 `add/remove` 없음).

---

## 5. 장 · 단점

| 👍 장점                               | ⚠️ 단점                              |
| ----------------------------------- | ---------------------------------- |
| **재귀(트리)** 를 단일 인터페이스로 우아하게 처리      | 구조가 단순할 땐 과설계                      |
| 클라이언트 코드가 Leaf/Composite **구분 불필요** | 부모 참조, 삭제, 순회 등 라이프사이클 관리 어려울 수 있음 |
| 새로운 Component 타입 추가 용이 (OCP)        | 전체 트리 조작이 과도하게 느슨해져 제약 표현이 어려움     |

---

## 6. 다른 패턴과 비교

| 패턴            | 공통점            | 차이점                                                     |
| ------------- | -------------- | ------------------------------------------------------- |
| **Decorator** | 객체 래핑          | 기능을 “추가”하는 것에 집중, **트리(부분-전체)** 표현이 목적이 아님              |
| **Iterator**  | 트리 순회 지원 가능    | Composite는 구조 모델링, Iterator는 순회 방법 제공                   |
| **Visitor**   | 트리를 대상으로 연산 수행 | Visitor는 구조는 그대로 두고 **새 연산** 을 쉽게 추가 (Composite과 잘 어울림) |

---

## 7. 실무의 경우

* **HTML DOM**: `Element`(Composite), `TextNode`(Leaf)
* **GUI 툴킷**: `Container`(Composite), `Widget`(Leaf)
* **컴파일러 AST**: `Expression`(Composite/Leaf), `visit()` 연산은 Visitor로 분리
* **게임 엔진**: 씬 그래프(노드 트리) 구성

---

## 8. 적용 팁

1. **Visitor 패턴** 과 자주 함께 사용 → 연산을 구조 밖으로 빼고 확장성 높이기.
2. 인터페이스를 **불변(immutable) 트리**로 두면 동시성/테스트가 편해짐(새 구조 리턴).
3. Python에선 `__iter__` 제공해서 트리 순회를 자연스럽게 만들 수 있다.

---

### 결론

> “부분과 전체를 **동일한 타입**으로 취급하고, **재귀 호출**로 행동을 위임하자.”
> Composite는 트리 구조를 다루는 **표준 해법**이다. 🌲
