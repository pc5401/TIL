# 🛡️ Proxy Pattern — “진짜 객체 대신 대리인으로 제어하기”

> **한 줄 정의**
> “주요 객체(Real Subject)에 접근하기 전, **대리 객체(Proxy)** 를 세워 **제어·보호·지연** 등의 부가 동작을 끼워 넣는다.”

---

## 1. 왜 쓰는가?

| 시나리오                   | 문제                          | Proxy가 하는 일                 |
| ---------------------- | --------------------------- | --------------------------- |
| **원격 서비스** (RPC, gRPC) | 네트워크 통신 세부 구현을 클라이언트가 알아야 함 | \_원격 프록시\_가 로컬 메서드처럼 감싸기    |
| **대용량 객체** (이미지, PDF)  | 첫 로드 시 메모리·시간 비용 큼          | \_가상 프록시\_가 **지연 로딩(lazy)** |
| **보안·권한** (파일 시스템)     | 클라이언트가 직접 민감 자원 접근          | \_보호 프록시\_가 권한 체크 후 위임      |
| **캐싱·로깅**              | 공통 부가 기능을 매번 삽입             | \_스마트 프록시\_에서 사전/사후 로직 수행   |

---

## 2. 구조 다이어그램

```
Client ──▶ Proxy ──▶ RealSubject
              ▲
      동일 인터페이스 (Subject)
```

* **Subject** : 공용 인터페이스 (`request()`)
* **RealSubject** : 실제 작업 수행
* **Proxy** : RealSubject 레퍼런스를 보관, 필요 시 생성/호출/검증 등 추가 로직

---

## 3. Python 예제 — **가상 프록시로 이미지 지연 로딩**

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