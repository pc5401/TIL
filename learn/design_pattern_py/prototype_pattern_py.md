# 🐑 Prototype Pattern (프로토타입) 노트 — Python 예제 중심

> **정의**
> “*이미 존재하는 객체* 를 **복제**해 새 인스턴스를 만든다.”
> 복잡 초기화·대용량 데이터 로딩 같은 **생성 비용**을 아껴 주는 생성 패턴.

---

## 1. 핵심 아이디어

| 포인트                | 설명                                           |
| ------------------ | -------------------------------------------- |
| **원형(Prototype)**  | 복제의 근거가 되는 객체. `clone()`(또는 `copy`) 메서드를 제공. |
| **얕은 복사 vs 깊은 복사** | 내부에 **가변 참조**가 있으면 `copy.deepcopy` 필요.       |
| **캐시/레지스트리**       | 자주 복제하는 프로토타입을 **저장소**에 보관해 빠르게 꺼낸다.         |

---

## 2. Python 구현 예제

### 2-1) 단순 값 객체 (얕은 복사)

```python
from __future__ import annotations
import copy
from typing import Protocol

class Prototype(Protocol):
    def clone(self) -> "Prototype": ...

class BasicDocument:
    def __init__(self, title: str, content: str) -> None:
        self.title, self.content = title, content

    def clone(self) -> "BasicDocument":
        # 값만 복사 ⇒ 얕은 복사 OK
        return copy.copy(self)

    def __str__(self) -> str:
        return f"<Doc '{self.title}' : {self.content[:15]}…>"
```

### 2-2) 복합 객체 (깊은 복사)

```python
class ComplexDoc:
    def __init__(self, metadata: dict, pages: list[str]) -> None:
        self.metadata = metadata        # 가변 객체
        self.pages = pages

    def clone(self) -> "ComplexDoc":
        # 내부 리스트·딕셔너리까지 재귀 복제
        return copy.deepcopy(self)

    def add_page(self, text: str):      # 상태 변경 메서드
        self.pages.append(text)

    def __str__(self) -> str:
        return f"{self.metadata['title']}({len(self.pages)} pages)"
```

### 2-3) 프로토타입 레지스트리 & 사용

```python
class PrototypeRegistry:
    _registry: dict[str, Prototype] = {}

    @classmethod
    def register(cls, name: str, proto: Prototype):
        cls._registry[name] = proto

    @classmethod
    def create(cls, name: str) -> Prototype:
        return cls._registry[name].clone()


# ---- 초기 등록 ----
doc_proto = ComplexDoc({"title": "Template"}, ["Cover", "Intro"])
PrototypeRegistry.register("doc", doc_proto)

# ---- 클라이언트 복제 ----
new_doc = PrototypeRegistry.create("doc")
new_doc.metadata["title"] = "Project Plan"
new_doc.add_page("Timeline")

print(doc_proto)   # Template(2 pages)
print(new_doc)     # Project Plan(3 pages)
```

> 원형과 복제본은 **독립** — 원형 수정 없이 새 상태를 빠르게 생성.

---

## 3. 언제 쓰면 좋은가?

| 시나리오                    | 이유                                  |
| ----------------------- | ----------------------------------- |
| **대량 오브젝트 스폰** (게임 몬스터) | 초기화·텍스처 로딩 비용 절감                    |
| **문서/폼 템플릿**            | 기본 필드 유지 + 사용자 데이터만 변경              |
| **복잡 그래프 구조**           | DB 쿼리·API 호출로 새로 만드는 대신 메모리 내 깊은 복사 |
| **실험 객체**               | 기존 모델 파라미터를 복제해 하이퍼 파라미터 튜닝         |

---

## 4. 다른 생성 패턴과 비교

| 패턴            | 생성 방식              | 메모리 관점           |
| ------------- | ------------------ | ---------------- |
| **Prototype** | **복제** (`clone()`) | 같은 구조지만 *새 인스턴스* |
| Flyweight     | **공유** 캐시          | 동일 인스턴스 **재사용**  |
| Builder       | **단계별 조립**         | 매번 새 객체          |
| Factory       | **추상화된 new**       | 재사용 여부 관여 X      |
| Singleton     | **전역 하나**          | 인스턴스 1개 고정       |

---

## 5. 장·단점

| 👍 장점                  | ⚠️ 단점               |
| ---------------------- | ------------------- |
| 생성 시간·리소스 절감           | 깊은 복사 구현이 까다로울 수 있음 |
| 원형을 런타임에 등록해 **유연성** ↑ | 순환 참조·복합 객체 → 성능 ↓  |
| 서브클래스 없이도 새 유형 생성      | 클론 후 상태 초기화 코드 필요   |

---

## 6. 실무에서 쓴다면...

1. **`copy.copy` vs `copy.deepcopy`** : 내부에 불변(숫자, str)만 → 얕은 복사로 충분.
2. **슬롯/데이터클래스**는 사용자 정의 `__copy__`, `__deepcopy__` 오버라이드 가능.
3. **데이터베이스 ORM**: `obj.id = None; session.add(obj)` 로 복제 save.
4. 클론 후 **식별자(ID) 재발급**·타임스탬프 초기화 등 **후처리 메서드** 두기.

---

## 한 줄 정리

> “*비싼 생성* 대신 **복제**로 빠르게 새 객체를 얻는다” — 프로토타입 패턴은 **템플릿·대량 복사** 상황의 효율성을 극대화한다. 🐑💨
