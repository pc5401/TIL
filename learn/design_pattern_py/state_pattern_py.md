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
