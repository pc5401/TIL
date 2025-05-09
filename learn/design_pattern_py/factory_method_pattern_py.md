# 🛠️ 팩토리 메서드 패턴 (Factory Method Pattern) — Python 위주 노트

> **의도**
> “*무엇을* 만들지는 **서브클래스**가 결정하고,
> **Creator**(부모)는 **공통 로직**만 보유한다.”

*객체 생성을 전담하는 `factory_method()`를 추출해
클래스 간 **결합도를 낮추고** / **확장성을 높여** 주는 생성 패턴.*

---

## 1. 구조 한눈 보기

| 역할                           | 책임                                                 |
| :--------------------------- | :------------------------------------------------- |
| **Product** *(인터페이스/추상 클래스)* | 생성될 객체의 공통 API 정의                                  |
| **ConcreteProduct**          | Product 구현 A, B, …                                 |
| **Creator** *(추상)*           | `factory_method()` 선언 + 공통 비즈니스 `some_operation()` |
| **ConcreteCreator**          | `factory_method()`를 오버라이드해 **어떤 Product를 만들지** 결정  |

```
Client ──▶ ConcreteCreatorA ──▶ factory_method() ──▶ ConcreteProductA
                ▲
                │ ConcreteCreatorB … → ConcreteProductB
```

---

## 2. Python 예제 📄

```python
from abc import ABC, abstractmethod


# --- 1) Product 계층 -----------------------------
class Transport(ABC):                 # Product
    @abstractmethod
    def deliver(self) -> str: ...


class Truck(Transport):               # ConcreteProduct
    def deliver(self) -> str:
        return "도로로 화물 배송"


class Ship(Transport):
    def deliver(self) -> str:
        return "해상으로 화물 배송"


# --- 2) Creator 계층 -----------------------------
class Logistics(ABC):                 # Creator
    @abstractmethod
    def factory_method(self) -> Transport: ...

    def plan_delivery(self) -> str:   # 공통 로직
        vehicle = self.factory_method()
        return f"[계획] {vehicle.deliver()}"


class RoadLogistics(Logistics):       # ConcreteCreator
    def factory_method(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def factory_method(self) -> Transport:
        return Ship()


# --- 3) Client 코드 ------------------------------
def client_code(creator: Logistics):
    print(creator.plan_delivery())


if __name__ == "__main__":
    client_code(RoadLogistics())      # [계획] 도로로 화물 배송
    client_code(SeaLogistics())       # [계획] 해상으로 화물 배송
```

\*Creator는 \*\*배송 절차(plan\_delivery)\**만 알고
실제 운송 수단(Truck/Ship)은 **서브클래스가 주입**.*

---

## 3. 언제 쓰나? 🧐

| 시나리오          | 이유                                              |
| ------------- | ----------------------------------------------- |
| **플러그인·확장**   | 새 제품을 추가할 때 *Creator 서브클래스*만 작성 → 클라이언트 건드리지 않음 |
| **테스트 더블**    | 테스트에서 `TestCreator` 주입해 목·스텁 제품 생성              |
| **라이브러리 ↔ 앱** | 라이브러리(Creator) + 앱(ConcreteCreator) 분리로 커스텀 가능  |

---

## 4. 장·단점

| 👍 이점                                    | ⚠️ 주의                              |
| ---------------------------------------- | ---------------------------------- |
| **Open/Closed**: 새 제품 추가 시 Creator 수정 없음 | 클래스 수 증가                           |
| Creator 공통 코드 재사용                        | 제품 종류가 적으면 과설계                     |
| 런타임에 Creator 교체 가능                       | 생성 단계가 단순하면 \_Simple Factory\_가 충분 |

---

## 5. 관련 패턴 비교

| 패턴                   | 핵심 차이                    |
| -------------------- | ------------------------ |
| **Simple Factory**   | 정적 함수로 분기 → *패턴이 아닌 관용구* |
| **Abstract Factory** | **제품군 묶음**을 생성           |
| **Builder**          | **단계별** 조립 + 플루언트 API    |
| **Prototype**        | 기존 객체를 **복제**            |

---

## 6. 한 줄 정리

> **“생성 책임을 서브클래스로 위임해, ‘무엇을 만들지’ 결정을 늦춘다.”**
> 덕분에 **새 제품**이 늘어나도 **Creator 코드**는 그대로! 🚀
