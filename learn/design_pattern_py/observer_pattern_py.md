# 👀 Observer Pattern — 이벤트를 “구독” · “발행”하는 디자인 패턴

> **핵심 한 줄**
> “*변화를 감지* 해서 **여러 객체**에게 **자동 알림**을 보내고 싶을 때.”

---

## 1. 왜 쓰나?

| 시나리오                      | 문제점(직접 호출)               | Observer 해결책                         |
| ------------------------- | ------------------------ | ------------------------------------ |
| GUI 버튼 → 클릭 시 여러 핸들러      | 버튼 코드가 핸들러를 **직접** 알아야 함 | 버튼 = **Subject**, 핸들러 = **Observer** |
| 데이터 모델 변경 → 그래프, 테이블 업데이트 | 모델이 뷰 레이어에 의존            | 모델은 **알림**만, 뷰는 **구독**만              |
| 멀티플레이 게임 → 상태 동기화         | 플레이어 객체끼리 강결합            | EventBus에 상태 변경 발행                   |

---

## 2. 패턴 구조

```
Subject
 ├─ attach(observer)
 ├─ detach(observer)
 └─ notify()

Observer (인터페이스)
 └─ update(subject)
```

* **Subject** : 상태 보유 + 변화 시 `notify`
* **Observer** : `update` 구현, 등록/해제 가능

---

## 3. Python 예제 — **주식 가격 알림**

```python
from __future__ import annotations
from typing import Protocol, List


# ---------- Observer 인터페이스 ----------
class Observer(Protocol):
    def update(self, subject: "Stock") -> None: ...


# ---------- Subject ----------
class Stock:
    def __init__(self, symbol: str, price: float) -> None:
        self.symbol, self._price = symbol, price
        self._observers: List[Observer] = []

    # 구독 관리
    def attach(self, obs: Observer) -> None:
        self._observers.append(obs)

    def detach(self, obs: Observer) -> None:
        self._observers.remove(obs)

    # 상태 변화
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new: float) -> None:
        if new != self._price:
            self._price = new
            self.notify()

    # 알림
    def notify(self) -> None:
        for obs in self._observers:
            obs.update(self)


# ---------- Concrete Observers ----------
class EmailAlert:
    def update(self, stock: Stock) -> None:
        print(f"[Email] {stock.symbol} price -> {stock.price}")

class SMSAlert:
    def update(self, stock: Stock) -> None:
        print(f"[SMS] {stock.symbol} price -> {stock.price}")


# ---------- Client ----------
if __name__ == "__main__":
    apple = Stock("AAPL", 150.0)
    email = EmailAlert()
    sms   = SMSAlert()

    apple.attach(email)
    apple.attach(sms)

    apple.price = 151.5   # 두 알림 모두 동작
    apple.detach(email)
    apple.price = 149.8   # SMS만 동작
```

---

## 4. 장 · 단점

| 👍 장점                               | ⚠️ 단점                               |
| ----------------------------------- | ----------------------------------- |
| **저결합** — Subject/Observer 서로 타입 모름 | 관찰자 수 ↑ → notify 비용 ↑               |
| 런타임 동적 구독·해제                        | 순환 참조 → 메모리 누수 주의                   |
| 동일 이벤트에 다양한 행동 추가                   | 복잡 이벤트, 순서 요구 시 더 고도화 필요 (EventBus) |

---

## 5. 실전 사용처

| 분야                 | 라이브러리 / API                                                             |
| ------------------ | ----------------------------------------------------------------------- |
| **GUI**            | PyQt `QObject/pyqtSignal`, Tkinter `trace`, Java Swing `ActionListener` |
| **Reactive 프로그래밍** | RxPy `Observable`, asyncio `Event`                                      |
| **Django ORM**     | `signals.post_save` / `pre_delete`                                      |
| **Redis Pub/Sub**  | 분산 Observer 구현                                                          |
| **Game Engine**    | Unity `C# event delegate`, Godot `Signal`                               |

---

## 6. 다른 패턴과 비교

| 패턴                          | 차이점                                                        |
| --------------------------- | ---------------------------------------------------------- |
| **Mediator**                | 모든 참가자 간 통신을 **허브 객체**가 중재 — Observer는 직접 Subject→Observer |
| **EventBus (Pub/Sub)**      | Observer 확장판; 주제(topic) 단위, 비동기 큐 사용 가능                    |
| **Chain of Responsibility** | 요청을 **순차 전파**하며 처리자 결정, Observer는 **모두에게 브로드캐스트**          |

---

## 7. 구현 팁 (Python)

1. **약한 참조**로 메모리 누수 방지

   ```python
   import weakref
   self._observers = set()
   self._observers.add(weakref.ref(obs))
   ```
2. **asyncio**와 조합 — `async def update()` + `await` notify
3. **형 힌트** : `typing.Protocol` 로 Observer 계약 명시 → 정적 검사 통과
4. **데코레이터** 활용 — `@subject.watch` 로 구독 쉽게

---

### 마무리

> “Observer = **이벤트 알림**의 기본기.”
> 콜백 헤더를 직접 들고 다니지 말고 **구독·발행 모델**로 바꾸면, 모듈이 깔끔히 분리된다! 🚀
