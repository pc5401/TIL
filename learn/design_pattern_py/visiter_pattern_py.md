# 🧭 Visitor Pattern — “객체 구조는 그대로, **새 연산**만 계속 추가”

> **핵심**
> 안정적인 **객체 구조(트리/그래프)** 위에, 구조를 건드리지 않고 **새 연산(행동)** 을 추가하고 싶을 때.
> → 각 요소가 `accept(visitor)`로 **방문자**를 받아들이고, 방문자는 요소 타입별 메서드(`visit_*`)로 작업한다.
> *= 더블 디스패치 기법.*

---

## 1) 언제 쓰나?

| 상황                     | 문제                                 | Visitor로 해결                          |
| ---------------------- | ---------------------------------- | ------------------------------------ |
| **AST(수식/파서)**         | 평가, 최적화, pretty print 등 연산이 계속 늘어남 | 구조(노드 클래스)는 고정, 방문자만 새로 추가           |
| **파일/폴더 트리**           | 크기 합, 권한 검사, 인덱싱 등 각기 다른 연산        | `SizeVisitor`, `IndexVisitor` 등으로 분리 |
| **컴포지트(Composite) 구조** | 연산이 클래스 안에 퍼짐 → SRP 위반             | 연산을 Visitor 밖으로 빼 SRP 회복             |

---

## 2) 구조 (텍스트)

```
Element (Node)
 ├─ accept(visitor)  ────────► Visitor
 │                            ├─ visit_File(File)
 ├─ File (Leaf)               └─ visit_Directory(Directory)
 └─ Directory (Composite)
```

* **Element**: `accept(visitor)` 만 제공 (자기 자신을 방문자에게 넘김)
* **Visitor**: 요소 타입별 `visit_*` 메서드 보유
* **ConcreteVisitor**: 실제 연산 구현 (크기 합산, 렌더링, 검증 등)

---

## 3) Python 예제 — 파일/디렉터리에 **두 가지 연산** 추가

> 구조는 그대로 두고, **(1) 총 용량 계산**, **(2) 트리 출력** 두 연산을 Visitor로 구현

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# ---------- Elements (파일 트리) ----------
class Node(ABC):
    @abstractmethod
    def accept(self, visitor: "Visitor") -> None:
        ...


class File(Node):
    def __init__(self, name: str, bytes_: int) -> None:
        self.name, self.bytes = name, bytes_

    def accept(self, visitor: "Visitor") -> None:
        visitor.visit_file(self)


class Directory(Node):
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: List[Node] = []

    def add(self, node: Node) -> None:
        self.children.append(node)

    def accept(self, visitor: "Visitor") -> None:
        visitor.visit_directory(self)   # 방문자가 순회 시점을 결정


# ---------- Visitor 인터페이스 ----------
class Visitor(ABC):
    @abstractmethod
    def visit_file(self, f: File) -> None: ...
    @abstractmethod
    def visit_directory(self, d: Directory) -> None: ...


# ---------- Concrete Visitors ----------
class SizeVisitor(Visitor):
    """트리의 총 바이트 수 계산"""
    def __init__(self) -> None:
        self.total = 0

    def visit_file(self, f: File) -> None:
        self.total += f.bytes

    def visit_directory(self, d: Directory) -> None:
        for child in d.children:
            child.accept(self)  # 재귀 순회 (전위/후위는 자유)


class PrintTreeVisitor(Visitor):
    """트리를 이쁘게 출력"""
    def __init__(self) -> None:
        self._depth = 0

    def visit_file(self, f: File) -> None:
        print("  " * self._depth + f"📄 {f.name} ({f.bytes}B)")

    def visit_directory(self, d: Directory) -> None:
        print("  " * self._depth + f"📁 {d.name}/")
        self._depth += 1
        for ch in d.children:
            ch.accept(self)
        self._depth -= 1


# ---------- Client ----------
if __name__ == "__main__":
    root = Directory("root")
    src = Directory("src")
    root.add(src)
    src.add(File("main.py", 1200))
    src.add(File("utils.py", 800))
    root.add(File("logo.png", 102400))

    # (1) 사이즈 계산
    s = SizeVisitor()
    root.accept(s)
    print("Total size:", s.total, "bytes")

    # (2) 트리 프린트
    printer = PrintTreeVisitor()
    root.accept(printer)
```

**출력 예**

```
Total size: 104,400 bytes
📁 root/
  📁 src/
    📄 main.py (1200B)
    📄 utils.py (800B)
  📄 logo.png (102400B)
```

> 같은 구조에서 **방문자만 바꿔** 서로 다른 연산을 수행.

---

## 4) 장 · 단점 요약

| 👍 장점                                  | ⚠️ 단점                                       |
| -------------------------------------- | ------------------------------------------- |
| **새 연산 추가가 쉬움** — Element 건드리지 않음(OCP) | **새 Element 타입 추가가 어려움** — 모든 Visitor를 수정해야 |
| 연산 로직을 외부로 분리 → **SRP** 향상             | 이중 디스패치 패턴/순회 시점 이해 필요                      |
| 복잡한 트리 연산(수집/변환/검사)을 한 곳에 캡슐화          | 순회 상태(깊이/경로) 관리 코드가 장황해질 수 있음               |

---
