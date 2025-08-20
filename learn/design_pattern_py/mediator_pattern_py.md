# 🕸️ Mediator Pattern — “객체들이 **중재자**를 통해 대화하게 하라”

> **의도**
> 객체들(동료, colleague) 사이의 **복잡한 N\:N 상호작용**을
> 한 곳의 **중재자(Mediator)** 로 모아 **결합도**를 낮추고, **통신 규약**을 캡슐화한다.

---

## 1) 언제 쓰나?

| 상황             | 문제                  | Mediator로 해결              |
| -------------- | ------------------- | ------------------------- |
| 채팅방(유저↔유저 다대다) | 유저끼리 직접 참조 → 연결망 복잡 | `ChatRoom`(중재자)이 라우팅      |
| 항공 관제(항공기↔항공기) | 충돌 방지 로직이 각 기체에 분산  | `ATC` 가 관제/슬롯 배정          |
| 폼 위젯 상호작용      | 위젯끼리 서로 값을 바꿈       | `FormMediator` 가 흐름 규칙 보유 |

**핵심**: 동료 객체는 서로를 모르고 **중재자만 안다**.

---

## 2) 구조

```
Colleague ─┐
Colleague ─┼──▶ Mediator ◀── Colleague
Colleague ─┘        ▲
                (규칙/라우팅)
```

* **Mediator** : 상호작용 규칙/흐름을 보관 (`notify(sender, event, payload)`)
* **Colleague** : 작업 발생 시 **중재자에게만 통지**. 다른 동료에게 직접 호출 X

---

## 3) Python 예제 — 간단 **채팅방** 중재

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict


# ---------- Mediator Interface ----------
class ChatMediator(ABC):
    @abstractmethod
    def register(self, user: "User") -> None: ...
    @abstractmethod
    def notify(self, sender: "User", event: str, payload: str) -> None: ...


# ---------- Concrete Mediator ----------
class ChatRoom(ChatMediator):
    def __init__(self) -> None:
        self._users: Dict[str, User] = {}

    def register(self, user: "User") -> None:
        self._users[user.name] = user
        user.mediator = self

    def notify(self, sender: "User", event: str, payload: str) -> None:
        if event == "broadcast":
            for name, u in self._users.items():
                if u is not sender:
                    u.receive(f"{sender.name}: {payload}")
        elif event.startswith("dm:"):
            _, to = event.split(":", 1)
            if to in self._users:
                self._users[to].receive(f"[DM] {sender.name}: {payload}")
        elif event == "banword":
            # 예: 욕설 필터/정책 집행 같은 룰도 Mediator가 가짐
            if "금지어" in payload:
                sender.receive("⚠️ 금지어가 포함되어 전송되지 않았습니다.")
            else:
                self.notify(sender, "broadcast", payload)

```