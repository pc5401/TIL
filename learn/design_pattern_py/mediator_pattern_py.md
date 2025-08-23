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


# ---------- Colleague ----------
class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.mediator: ChatMediator | None = None

    # 동료는 중재자에게만 말한다
    def say(self, text: str) -> None:
        assert self.mediator
        self.mediator.notify(self, "banword", text)

    def dm(self, to: str, text: str) -> None:
        assert self.mediator
        self.mediator.notify(self, f"dm:{to}", text)

    def receive(self, text: str) -> None:
        print(f"{self.name} ◀ {text}")


# ---------- Client ----------
if __name__ == "__main__":
    room = ChatRoom()
    alice = User("Alice"); room.register(alice)
    bob   = User("Bob");   room.register(bob)
    chris = User("Chris"); room.register(chris)

    alice.say("안녕!")                 # 브로드캐스트
    bob.dm("Alice", "반가워!")         # DM
    chris.say("금지어 들어간 문장…")    # 정책에 의해 차단
```

**포인트**

* 사용자는 서로 참조하지 않고 `ChatRoom`만 안다.
* **룰(금지어, 라우팅)** 을 Mediator 가 들고 있어 **동료가 단순**해진다.

---

## 4) 장 · 단점

| 👍 장점                    | ⚠️ 단점                           |
| ------------------------ | ------------------------------- |
| 동료 간 결합도 ↓ (N\:N → 1\:N) | Mediator가 커지면 **God Object** 위험 |
| 상호작용 규칙을 한 곳에 캡슐화        | 디버깅 시 흐름이 모두 Mediator로 몰려 추적 필요 |
| 동료 클래스 단순·재사용 용이         | 잘못 설계하면 또 다른 단일 장애점(SPOF)       |

---

## 5) 다른 패턴과 비교

| 패턴                                  | 공통         | 차이                                                         |
| ----------------------------------- | ---------- | ---------------------------------------------------------- |
| **Observer**                        | 이벤트 중심 통신  | Observer는 **브로드캐스트**에 가깝고, Mediator는 **규칙 기반 라우팅/흐름 제어**   |
| **Facade**                          | 복잡성을 감춤    | Facade는 **외부 인터페이스 단순화**, 내부 객체 사이의 상호작용 **조율**은 아님        |
| **Publisher–Subscriber(Event Bus)** | 느슨한 결합 메시징 | Pub/Sub은 주제(topic) 기반 비지시적 전달, Mediator는 **의사결정·순서 제어** 책임 |

---

