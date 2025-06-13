# 🎀 Decorator Pattern — 런타임에 ‘포장지’ 씌워 기능 확장하기

> **핵심 문장**
> “클래스를 *상속* 하지 않고, **객체를 감싸면서(add-on)** 행위를 동적으로 더한다.”

---

## 0. 왜 쓰나?

| 증상                                        | 데코레이터 솔루션                      |
| ----------------------------------------- | ------------------------------ |
| “로그도 찍고, 캐시도 넣고, 압축도 해야 한다… 그런데 조합이 늘어난다” | 기본 객체에 **필요한 기능만 체인**으로 래핑     |
| 클래스 상속 트리가 ‘폭발’                           | 기능 X, Y, Z를 다형 조합하기보다 **컴퍼지션** |
| 미들웨어 / 파이프라인 계층 필요                        | 요청을 **순차 포장**해 각 계층 책임 수행      |

---

## 1. 구조 그림 (텍스트)

```
Client → ConcreteComponent
              ▲
              │ wraps
      ┌──── Decorator (abstract) ──────┐
      │    • comp: Component           │
      │    • operation() → comp.op()   │
      └────────────────────────────────┘
          ▲                 ▲
          │                 │
   LoggingDecorator   CompressionDecorator  …
```

* **Component** : 기본 인터페이스
* **ConcreteComponent** : 원본 기능
* **Decorator** : Component를 **구성요소로 보유**하고, 호출 전후에 추가 작업 수행
* **ConcreteDecorator** : 실제 부가기능 구현 (로깅, 캐싱, 권한 체크…)

---

## 2. Python 예제 — **파일 I/O 기능 확장**

```python
from __future__ import annotations
from abc import ABC, abstractmethod
import gzip, logging, functools


# 1) Component
class DataSource(ABC):
    @abstractmethod
    def write(self, data: bytes) -> None: ...
    @abstractmethod
    def read(self) -> bytes: ...


# 2) ConcreteComponent
class FileDataSource(DataSource):
    def __init__(self, filename: str):
        self._filename = filename

    def write(self, data: bytes) -> None:
        with open(self._filename, "wb") as f:
            f.write(data)

    def read(self) -> bytes:
        with open(self._filename, "rb") as f:
            return f.read()


# 3) Base Decorator
class DataSourceDecorator(DataSource):
    def __init__(self, wrappee: DataSource):
        self._wrappee = wrappee

    def write(self, data: bytes) -> None:
        self._wrappee.write(data)

    def read(self) -> bytes:
        return self._wrappee.read()


# 4) Concrete Decorators
class CompressionDecorator(DataSourceDecorator):
    def write(self, data: bytes) -> None:
        print("→ 압축 후 저장")
        super().write(gzip.compress(data))

    def read(self) -> bytes:
        print("→ 압축 해제 후 리턴")
        return gzip.decompress(super().read())


class LoggingDecorator(DataSourceDecorator):
    def write(self, data: bytes) -> None:
        logging.info("write %d bytes", len(data))
        super().write(data)

    def read(self) -> bytes:
        result = super().read()
        logging.info("read %d bytes", len(result))
        return result


# 5) 클라이언트 구성
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # 베이스 컴포넌트
    source: DataSource = FileDataSource("note.bin")

    # 단계별 데코레이션 (순서 자유)
    source = LoggingDecorator(CompressionDecorator(source))

    # 사용
    source.write(b"Hello Decorator Pattern!" * 5)
    print(source.read())
```

```
INFO:root:write 140 bytes
→ 압축 후 저장
→ 압축 해제 후 리턴
INFO:root:read 140 bytes
b'Hello Decorator Pattern!...'
```

*기능을 더 붙이고 싶으면 **새 데코레이터를 만들고 체인**에 꽂으면 끝.*

---

## 3. 장 · 단점 정리

| 👍 장점                     | ⚠️ 단점                     |
| ------------------------- | ------------------------- |
| 상속 없이 **조합**만으로 기능 확장     | 데코레이터 수가 많으면 체인 추적 어려움    |
| 기능 조합 **런타임 변경** 가능       | 디버깅 시 중첩 깊이 파악 필요         |
| 단일 책임 원칙 ↔ 각 데코레이터 하나의 책임 | 클라이언트가 **순서**를 알맞게 연결해야 함 |

---

## 4. 실무에서 자주 보는 데코레이터

| 분야                    | 예                                                |
| --------------------- | ------------------------------------------------ |
| **Python @decorator** | 함수에 로깅, 캐시, 권한 체크                                |
| **웹 미들웨어**            | Django / Flask request ↦ response 체인             |
| **Java I/O Streams**  | `BufferedInputStream(new GZIPInputStream(sock))` |
| **React HOC**         | `withAuth(Component)`                            |
| **.NET Stream**       | CryptoStream, DeflateStream (서로 래핑)              |

---
