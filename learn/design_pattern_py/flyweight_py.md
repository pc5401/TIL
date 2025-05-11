# 🦋 Flyweight Pattern 노트

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
