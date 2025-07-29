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
