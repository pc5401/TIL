# 🐑 Prototype Pattern (프로토타입) 노트 — Python 예제 중심

> **정의**
> “*이미 존재하는 객체* 를 **복제**해 새 인스턴스를 만든다.”
> 복잡 초기화·대용량 데이터 로딩 같은 **생성 비용**을 아껴 주는 생성 패턴.

---

## 1. 핵심 아이디어

| 포인트                | 설명                                           |
| ------------------ | -------------------------------------------- |
| **원형(Prototype)**  | 복제의 근거가 되는 객체. `clone()`(또는 `copy`) 메서드를 제공. |
| **얕은 복사 vs 깊은 복사** | 내부에 **가변 참조**가 있으면 `copy.deepcopy` 필요.       |
| **캐시/레지스트리**       | 자주 복제하는 프로토타입을 **저장소**에 보관해 빠르게 꺼낸다.         |

---

## 2. Python 구현 예제

### 2-1) 단순 값 객체 (얕은 복사)

```python
from __future__ import annotations
import copy
from typing import Protocol

class Prototype(Protocol):
    def clone(self) -> "Prototype": ...

class BasicDocument:
    def __init__(self, title: str, content: str) -> None:
        self.title, self.content = title, content

    def clone(self) -> "BasicDocument":
        # 값만 복사 ⇒ 얕은 복사 OK
        return copy.copy(self)

    def __str__(self) -> str:
        return f"<Doc '{self.title}' : {self.content[:15]}…>"
```

### 2-2) 복합 객체 (깊은 복사)

```python
class ComplexDoc:
    def __init__(self, metadata: dict, pages: list[str]) -> None:
        self.metadata = metadata        # 가변 객체
        self.pages = pages

    def clone(self) -> "ComplexDoc":
        # 내부 리스트·딕셔너리까지 재귀 복제
        return copy.deepcopy(self)

    def add_page(self, text: str):      # 상태 변경 메서드
        self.pages.append(text)

    def __str__(self) -> str:
        return f"{self.metadata['title']}({len(self.pages)} pages)"
```

### 2-3) 프로토타입 레지스트리 & 사용

```python
class PrototypeRegistry:
    _registry: dict[str, Prototype] = {}

    @classmethod
    def register(cls, name: str, proto: Prototype):
        cls._registry[name] = proto

    @classmethod
    def create(cls, name: str) -> Prototype:
        return cls._registry[name].clone()


# ---- 초기 등록 ----
doc_proto = ComplexDoc({"title": "Template"}, ["Cover", "Intro"])
PrototypeRegistry.register("doc", doc_proto)

# ---- 클라이언트 복제 ----
new_doc = PrototypeRegistry.create("doc")
new_doc.metadata["title"] = "Project Plan"
new_doc.add_page("Timeline")

print(doc_proto)   # Template(2 pages)
print(new_doc)     # Project Plan(3 pages)
```

> 원형과 복제본은 **독립** — 원형 수정 없이 새 상태를 빠르게 생성.

---
