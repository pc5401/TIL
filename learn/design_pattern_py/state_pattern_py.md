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

---

## 4. 장 · 단점

| 👍 장점                           | ⚠️ 단점                |
| ------------------------------- | -------------------- |
| 상태 전환 로직 **캡슐화** – 조건문 제거       | 상태 클래스 수 증가          |
| 새 상태 추가 시 다른 코드 수정 최소           | 간단 FSM이면 과설계         |
| Context는 **상태 인터페이스**만 의존 → OCP | 상태 객체 간 강결합 전이 로직 주의 |

---

## 5. 패턴 비교

| 패턴                          | 공통점              | 차이점                                              |
| --------------------------- | ---------------- | ------------------------------------------------ |
| **Strategy**                | 런타임 객체 교체로 행동 변경 | Strategy는 *사람(클라이언트)* 가 교체, State는 **내부 로직**이 전이 |
| **Observer**                | 상태 변화 알림 가능      | Observer는 외부에 브로드캐스트, State는 내부 행동 변경            |
| **Chain of Responsibility** | 요청을 다른 객체로 위임    | Chain은 순차 처리, State는 현재 상태 한 객체가 담당              |

---

## 6. 실무 적용 팁

1. **Enum + dict 매핑**으로 간단 FSM 대체. 복잡해질 때 State 클래스로 승격.
2. 전이표가 크면 `transitions` 라이브러리(간단 DSL)로 구현 가능.
3. 상태 객체는 **무상태(singleton)** 로 두거나, 상태별 데이터가 있으면 새로 생성.
4. 로그 필요 시 `context.log(f"{self} -> {new_state}")`.

---

### 한 줄 결론

> 상태마다 달라지는 행동이 `if/else` 지옥을 만든다면, **State 패턴**으로 **“상태 = 객체”** 로 바꿔 조건문을 지워 보자! 🌀
