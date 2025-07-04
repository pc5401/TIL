# 🔌 Adapter Pattern — “호환 안 되는 인터페이스 맞춰 주는 변환 어댑터”

> **의도**
> 기존 코드(Client)가 기대하는 인터페이스와 **맞지 않는 클래스**를
> **중간 변환기(Adapter)** 로 감싸 - **수정 없이** 함께 쓰게 만든다.

---

## 1. 사용하는 이유

| 상황                        | 문제점                   | Adapter 해결책                   |
| ------------------------- | --------------------- | ----------------------------- |
| 레거시 DB 드라이버 vs 새 코드       | 메서드 시그니처가 다름          | 드라이버를 감싼 **어댑터** 제공           |
| 서드파티 API (e.g. AWS ↔ GCP) | 호출 규약 상이 → if/else 난무 | 공통 인터페이스 + **Adapter**        |
| 파이썬 타입 시스템 도입             | 오래된 dict 기반 객체        | `__getattr__` 로 래핑하여 속성 방식 지원 |

---

## 2. 구조 한눈

```
Client ──▶ Target (원하는 인터페이스)
                    ▲
                    │ implements
            ┌───────┴────────┐
            │   Adapter      │───▶  Adaptee (호환 안됨)
            │   (wraps)      │        기존 / 서드파티 클래스
            └────────────────┘
```

* **Target** : 클라이언트가 기대하는 인터페이스
* **Adaptee** : 이미 존재, 수정 어려움, 인터페이스 불일치
* **Adapter** : Adaptee → Target 로 **변환** (위임·변환·매핑)

---

## 3. Python 예제 — **JSON ↔ XML 파서 호환**

> 기존 코드(클라이언트)는 `parse()` 로 `dict` 를 돌려 받기를 기대한다.
> XML 라이브러리는 `XMLParser().load_xml()` 만 지원 → **Adapter** 투입!

```python
from __future__ import annotations
import xml.etree.ElementTree as ET
import json


# -------- Target Interface --------
class DataParser:
    def parse(self, raw: str) -> dict: ...
    

# -------- Adaptee  (제3자 라이브러리) --------
class XMLParser:
    def load_xml(self, raw: str) -> ET.Element:
        return ET.fromstring(raw)


# -------- Adapter --------
class XMLAdapter(DataParser):
    def __init__(self, adaptee: XMLParser) -> None:
        self._adaptee = adaptee

    def parse(self, raw: str) -> dict:
        root = self._adaptee.load_xml(raw)
        # 간단 변환: <item key="x">y</item> .. → {key: text}
        return {child.get("key"): child.text for child in root}


# -------- Concrete Target --------
class JSONParser(DataParser):
    def parse(self, raw: str) -> dict:
        return json.loads(raw)


# -------- Client 코드 --------
def client_code(parser: DataParser, raw: str):
    print("Result >>", parser.parse(raw))


if __name__ == "__main__":
    json_raw = '{"name":"Alice","age":30}'
    client_code(JSONParser(), json_raw)

    xml_raw = """<root>
                   <item key="name">Bob</item>
                   <item key="age">25</item>
                 </root>"""
    client_code(XMLAdapter(XMLParser()), xml_raw)
```

```
Result >> {'name': 'Alice', 'age': 30}
Result >> {'name': 'Bob', 'age': '25'}
```

*클라이언트는 `DataParser` 만 알면 되고, XML 라이브러리 구현은 그대로.*

---

## 4. 클래식 vs 객체(Adapter) 방식

| 종류               | 특징                                                              |
| ---------------- | --------------------------------------------------------------- |
| **객체 어댑터** (위 예) | 어댑터 **인스턴스**가 Adaptee를 **합성**(HAS-A)                            |
| **클래스 어댑터**      | 다중 상속 언어(C++)에서 `class Adapter : public Target, public Adaptee` |

파이썬은 다중 상속 가능하지만 *구성* 방식이 일반적.

---

## 5. 장·단점

| 👍 장점                      | ⚠️ 단점              |
| -------------------------- | ------------------ |
| 레거시·서드파티 코드를 **수정 없이 재사용** | 어댑터 수 증가 → 관리 비용   |
| 클라이언트는 **하나의 API**만 의존     | 성능 오버헤드(래핑∙변환)     |
| 점진적 마이그레이션 가능              | 복잡 매핑 로직 → 유지보수 주의 |

---

## 6. 다른 패턴과 비교

| 패턴            | 공통           | 차이점                            |
| ------------- | ------------ | ------------------------------ |
| **Decorator** | 객체를 래핑       | 목적: **기능 추가**, 인터페이스 동일        |
| **Proxy**     | 래핑해 호출 가로채기  | 목적: 접근 제어/지연로딩 등               |
| **Facade**    | 서브시스템 API 통합 | 내부 로직 숨기고 간단 인터페이스 제공 (새 기능 X) |

---

## 7. 실무 tip

1. **typing.Protocol** 로 Target 정의 → 정적 타입 안정.
2. **Pydantic v2** `model_config['json_encoders']` 도 내부 어댑터 역할.
3. AWS ↔ Azure 호환 시 `StorageAdapter` 계층 두어 클라우드 변경 대비.
4. 어댑터가 커지면 **변환 유틸 함수**로 분리해 SRP 유지.

---

### 결론

> “바꿀 수 없는 *Adaptee* 를 억지로 뜯지 말고, **얇은 Adapter** 입혀서 손쉽게 ‘호환성 레이어’를 완성하자!” 🔌
