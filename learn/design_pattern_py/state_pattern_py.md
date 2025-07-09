# 🔄 State Pattern — “상태별로 행동을 바꾼다”

> **키워드**
> 객체의 **내부 상태**를 객체로 분리해, 상태가 바뀔 때 **행동(메서드 구현)** 도 자동으로 바뀌도록 한다.

---

## 1. 써야 할 때?

| 시나리오                                       | 문제                         |
| ------------------------------------------ | -------------------------- |
| 게임 캐릭터 – `Idle` / `Running` / `Jumping`    | `if self.mode == …` 조건문 폭발 |
| 네트워크 커넥션 – `Closed` / `Open` / `Error`     | 상태마다 다른 API 허용·거부 필요       |
| 워크플로 엔진 – `Draft` / `Review` / `Published` | 단계별 행동과 전이 로직이 뒤엉킴         |

**State** 패턴으로 상태별 클래스를 분리 → 조건문 제거 + 새 상태 추가 쉬움.

---

## 2. 구조 그림

```
Context (Connection)
  ├─ state: State
  └─ request() → state.handle()

State (interface / ABC)
  └─ handle(context)

ConcreteStateA / ConcreteStateB …
  └─ handle(context)  # 상태별 행동 + 다음 상태로 전이 가능
```

* **Context** : 상태를 보관, 작업 요청을 상태 객체에 위임
* **State** : 공통 인터페이스(`handle()` 등)
* **ConcreteState** : 실제 작업 로직 + 필요하면 `context.state = 다른State()`로 전이

---

## 3. Python 예제 — **문서 워크플로**

```python
from __future__ import annotations
from abc import ABC, abstractmethod


# ---------- State Interface ----------
class State(ABC):
    @abstractmethod
    def edit(self, ctx: "Document"): ...
    
    @abstractmethod
    def publish(self, ctx: "Document"): ...


# ---------- Concrete States ----------
class Draft(State):
    def edit(self, ctx):               # 허용
        print("✏️  문서 수정함 (Draft)")
    
    def publish(self, ctx):
        print("📤 리뷰 상태로 보냄")
        ctx.state = Review()           # 상태 전이


class Review(State):
    def edit(self, ctx):
        print("⛔ 리뷰 중엔 편집 금지!")
    
    def publish(self, ctx):
        print("✅ 승인되어 Published 상태")
        ctx.state = Published()


class Published(State):
    def edit(self, ctx):
        print("🔒 이미 발행됨, 편집 불가")
    
    def publish(self, ctx):
        print("🔔 독자에게 알림 전송")


# ---------- Context ----------
class Document:
    def __init__(self):
        self.state: State = Draft()    # 초기 상태

    def edit(self):
        self.state.edit(self)

    def publish(self):
        self.state.publish(self)


# ---------- Client ----------
if __name__ == "__main__":
    doc = Document()
    doc.edit()       # Draft 편집
    doc.publish()    # → Review
    doc.edit()       # 편집 금지
    doc.publish()    # → Published
    doc.publish()    # 알림

```