# 🦋 Flyweight Pattern

> **의도**
> “동일한 속성( *intrinsic state* )을 갖는 객체를 **중복 생성**하지 않고 **공유**해 **메모리 사용량**을 최소화한다.”

<br/>

## 1. 핵심 개념

| 용어                    | 설명                                                   |
| --------------------- | ---------------------------------------------------- |
| **Flyweight(플라이웨이트)** | 공유 가능한 객체. 변하지 않는 **고정 속성**(intrinsic state)을 품고 있다. |
| **Intrinsic state**   | 모든 상황에서 동일⁠·⁠공유 가능한 데이터<br/>ex) 글꼴 이름, 색상, 책 제목      |
| **Extrinsic state**   | 실행 시점마다 달라지는 외부 데이터<br/>ex) 글자의 좌표, 책 읽은 페이지         |
| **Flyweight Factory** | 이미 생성된 플라이웨이트를 캐싱하고, 동일 키 요청 시 **재사용**을 반환한다.        |

<br/>

## 2. Python 예제 — **도서 객체 공유**

```python
from __future__ import annotations
from typing import Dict


# 1) Flyweight ─ intrinsic state = title
class BookFlyweight:
    def __init__(self, title: str) -> None:
        self._title = title        # 공유 속성

    # extrinsic state(Page)를 받아 동작
    def read(self, page: int) -> None:
        print(f"[{self._title}] ... reading p.{page}")


# 2) Flyweight Factory
class BookFactory:
    _pool: Dict[str, BookFlyweight] = {}

    @classmethod
    def get(cls, title: str) -> BookFlyweight:
        if title not in cls._pool:
            print(f"📘  create new BookFlyweight: {title}")
            cls._pool[title] = BookFlyweight(title)
        else:
            print(f"↩️   reuse existing BookFlyweight: {title}")
        return cls._pool[title]


# 3) Client 사용
if __name__ == "__main__":
    b1 = BookFactory.get("Effective Python")
    b1.read(10)

    b2 = BookFactory.get("Effective Python")   # 캐시 재사용
    b2.read(120)

    b3 = BookFactory.get("Clean Code")         # 새 인스턴스
    b3.read(5)

    # 메모리 확인
    print(f"Pool size = {len(BookFactory._pool)}")   # 2
```

```
📘  create new BookFlyweight: Effective Python
[Effective Python] ... reading p.10
↩️   reuse existing BookFlyweight: Effective Python
[Effective Python] ... reading p.120
📘  create new BookFlyweight: Clean Code
[Clean Code] ... reading p.5
Pool size = 2
```

*클라이언트는 `title`(intrinsic) 이 동일하면 **같은 객체**를 공유하고,
`page`(extrinsic)는 매 호출마다 외부에서 전달한다.*

<br/>

## 3. 언제 쓰나?

| 신호                     | 설명                                      |
| ---------------------- | --------------------------------------- |
| **수십 · 수백만 개**의 객체가 필요 | 텍스트 편집기의 **문자 glyph**, 지형 편집기의 **나무·돌** |
| **객체 중 상당수가 동일 속성**    | 게임에서 같은 모델 + 다른 위치 캐릭터                  |
| 메모리·GC 압박으로 성능 저하      | 캐시로 교체하면 힙 점유 대폭↓                       |

> **주의** : intrinsic/extrinsic 분리가 **가능**하고 **명확**해야 한다.
> 상태가 섞여 있으면 플라이웨이트 적용 불가.

<br/>

## 4. 다른 패턴과 비교

| 패턴            | 인스턴스 관리                | 주요 차이                         |
| ------------- | ---------------------- | ----------------------------- |
| **Flyweight** | **공유**(같은 속성 == 같은 객체) | 목적 = **메모리 절약**               |
| Singleton     | 항상 **전역 하나**           | 목적 = 전역 접근점                   |
| Factory       | 생성 과정 **추상화**          | 재사용 여부는 신경 안 씀                |
| Prototype     | **복제**로 신속 생성          | 공유 아님, 새 객체 만듦                |
| Object Pool   | 미리 생성 후 **반납/대여**      | 주로 *비싼 생성 + 짧은 생명* 자원(DB 커넥션) |

<br/>

## 5. 장 · 단점

| 👍 이점            | ⚠️ 단점                        |
| ---------------- | ---------------------------- |
| **메모리 사용** 대폭 감소 | 코드 복잡도 증가                    |
| 객체 생성/GC 비용 감소   | intrinsic/extrinsic 구분이 까다롭다 |
| 캐시 히트 시 성능 ↑     | 동기화 필요 시(멀티스레드) 락 고려         |

<br/>

## 6. 라이브러리 & 실제 사례

| 분야         | 예                                                     |
| ---------- | ----------------------------------------------------- |
| **문자 렌더링** | 각 글꼴 glyph를 플라이웨이트로 공유 (`Qt`, `Skia`)                 |
| **Java**   | `Integer.valueOf()` (-128\~127) 캐시, `String.intern()` |
| **게임엔진**   | Unity `Flyweight` 패턴으로 대량 오브젝트 렌더                     |
| **웹 브라우저** | CSS 색상, 스타일 값 테이블 재사용                                 |

<br/>

## 7. 한 줄 결론

> 동일한 속성이 반복된다면 **“새로 만들지 말고 공유하라”** — Flyweight는 대량 객체 환경의 메모리 구원투수! 🚀
