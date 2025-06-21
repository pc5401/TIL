# 🏗️ 빌더 패턴 (Builder Pattern)

> **목적** : “**복잡한 객체**를 **단계별**로 조립하고, 같은 절차에서 **다른 구성**을 얻도록 분리한다.”

* 생성 로직(`Builder`) ⇆ 최종 표현(`Product`) 분리
* 조립 순서를 통제하는 **Director**(선택)
* 플루언트 체이닝·불변 객체 생성·SQL/HTML/JSON 빌더 등에 자주 쓰임

---

## 1. 구조 요약

```
Client ─┐
        │ uses
  ┌─────▼─────┐      ┌────────────┐
  │ Director  │─────▶│  Builder   │◀─┐  interface/ABC
  └────────────┘call │+step() ... │  │
                     └────────────┘  │implements
               builds ▲      ▲ builds│
              Product │      │       │
                     ┌┴──────┴───┐   │
                     │ConcreteBdr│───┘
                     └───────────┘
```

---

## 2. Python 구현

### 2-1) 제품 정의

```python
class Computer:
    """최종적으로 조립될 복합 객체"""
    def __init__(self) -> None:
        self.cpu: str | None = None
        self.ram: str | None = None
        self.storage: str | None = None

    def spec(self) -> str:
        return f"CPU={self.cpu}, RAM={self.ram}, STORAGE={self.storage}"
```

### 2-2) 빌더 인터페이스

```python
from abc import ABC, abstractmethod

class ComputerBuilder(ABC):
    @abstractmethod
    def add_cpu(self) -> "ComputerBuilder": ...
    @abstractmethod
    def add_ram(self) -> "ComputerBuilder": ...
    @abstractmethod
    def add_storage(self) -> "ComputerBuilder": ...
    @abstractmethod
    def build(self) -> Computer: ...
```

> 메서드가 `self`를 반환하도록 설계하면 **플루언트 체이닝** 가능.

### 2-3) 구체 빌더

```python
class GamingPCBuilder(ComputerBuilder):
    def __init__(self) -> None:
        self._pc = Computer()

    def add_cpu(self):
        self._pc.cpu = "Intel i9"
        return self

    def add_ram(self):
        self._pc.ram = "32GB DDR5"
        return self

    def add_storage(self):
        self._pc.storage = "2TB NVMe"
        return self

    def build(self) -> Computer:
        return self._pc
```

### 2-4) Director (선택 요소)

```python
class ComputerShop:
    """조립 순서를 고정—다른 빌더라도 같은 절차"""
    def construct_high_end(self, builder: ComputerBuilder) -> Computer:
        return (
            builder.add_cpu()
                   .add_ram()
                   .add_storage()
                   .build()
        )
```

### 2-5) 사용 예

```python
if __name__ == "__main__":
    shop = ComputerShop()
    gaming_pc = shop.construct_high_end(GamingPCBuilder())
    print(gaming_pc.spec())
    # → CPU=Intel i9, RAM=32GB DDR5, STORAGE=2TB NVMe
```

---

## 3. 플루언트 빌더(Director 없이)

```python
db_url = (
    QueryBuilder()
      .host("localhost")
      .port(5432)
      .database("app")
      .user("dev")
      .password("secret")
      .to_uri()
)
```

*하나의 빌더 객체가 체이닝으로 스스로 Director 역할을 수행.*

---

## 4. 실무 컨텍스트

| 영역                    | 이유 / 예시                                                 |
| --------------------- | ------------------------------------------------------- |
| **SQL / NoSQL Query** | SQLAlchemy, Django ORM : `QuerySet.filter().order_by()` |
| **UI 위젯**             | Flutter `WidgetBuilder`, Tkinter `MenuBuilder`          |
| **HTTP 요청**           | `requests.Request()` + `Session.prepare()`              |
| **테스트 픽스처**           | `factory_boy` : 객체 상태를 단계별로 쌓아 생성                       |
| **불변 DTO**            | Java Lombok `@Builder`, Kotlin `copy()` 체이닝             |

---

## 5. 장단점

| 👍 장점                        | ⚠️ 단점                |
| ---------------------------- | -------------------- |
| **가독성** – 단계별·체이닝으로 명시적 조립   | 클래스 수 늘어남            |
| **불변 규칙** – 완성 전까지 외부 노출 없음  | *단순 객체* 에 적용하면 과설계   |
| **제품 변형 용이** – 같은 절차 + 다른 빌더 | 필수 단계 누락 시 런타임 오류 가능 |

---

## 6. 결론

> **Builder**는 “*조립 절차*”를 코드에 기록해 **복잡 객체를 안전·읽기 좋게 생성**한다—특히 **플루언트 API·불변 모델**에서 빛난다. 🛠️
