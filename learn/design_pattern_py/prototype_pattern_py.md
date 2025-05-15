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

### 단순 값 객체 (얕은 복사)

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
