# 🔗 Chain of Responsibility Pattern — “요청을 *연쇄*로 흘려보내기”

> **정의**
> 하나의 요청을 처리할 수 있는 *여러 핸들러*를 **체인(연결)** 으로 묶고,
> 각 핸들러가 **자기가 처리 가능한지 검사** 후
>   - 가능하면 처리하고 **종료**,
>   - 아니면 **다음 핸들러**에게 넘겨준다.

---

## 1. 언제 쓰면 유용할까?

| 현실-시나리오                        | 문제점(직접 if/elif)       |
| ------------------------------ | --------------------- |
| HTTP 미들웨어: 인증 → 캐싱 → 로깅        | 컨트롤러에 조건문 난무·순서 하드코딩  |
| 기술 지원 티켓: 1차 상담 → 2차 기술팀 → 관리자 | 단일 객체가 모든 규칙을 알아야     |
| GUI 이벤트 전파: 버튼 → 패널 → 윈도우 → …  | 부모가 자식 이벤트 처리 세부를 알아야 |

**CoR**(Chain of Responsibility) 로
핸들러를 체인으로 엮으면 **열·삽입·순서 재배치** 모두 간단!

---

## 2. 구조 미리보기

```
Client → HandlerA → HandlerB → HandlerC → … → (끝)
           ▲
           └─ BaseHandler (handle() / set_next())
```

* **Handler (interface / ABC)**:
  `handle(request)` — 요청 처리 여부 결정, 못하면 `next.handle(request)` 호출
* **ConcreteHandler**: 실제 처리 로직
* **Client**: 체인의 *첫* 핸들러에만 요청

---

## 3. Python 예제 — 간단 **스팸-메일 필터** 체인

```python
from __future__ import annotations
from abc import ABC, abstractmethod

class Email:
    def __init__(self, sender: str, subject: str, body: str):
        self.sender, self.subject, self.body = sender, subject, body


# ---------- Handler 인터페이스 ----------
class Filter(ABC):
    def __init__(self):
        self._next: Filter | None = None

    def set_next(self, nxt: "Filter") -> "Filter":
        self._next = nxt
        return nxt                                # 체인 조립 편하게 반환

    def handle(self, mail: Email):
        if self._process(mail):                  # 자기가 처리했으면 return
            return
        if self._next:
            self._next.handle(mail)              # 못하면 패스 다운

    @abstractmethod
    def _process(self, mail: Email) -> bool:
        """True = 내가 처리하고 체인 종료"""

```