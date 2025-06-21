# 🏭 추상 팩토리 패턴 (Abstract Factory)

> “**제품 군(family)** 단위로 객체를 **통일된 방식**으로 생성”
> UI 플랫폼·DB 드라이버처럼 **종류는 다르지만 서로 연관된 객체 묶음**을 상황(플랫폼, 공급자)에 따라 한꺼번에 교체할 수 있게 한다.

---

## 1. 패턴 핵심

| 포인트        | 설명                                 |
| ---------- | ---------------------------------- |
| **제품군 집합** | 버튼·체크박스·스크롤바처럼 *함께 작동* 해야 하는 객체 묶음 |
| **추상 팩토리** | 제품군을 생성하는 **인터페이스(혹은 추상 클래스)**     |
| **구체 팩토리** | 플랫폼·벤더별로 추상 팩토리를 구현 → 제품군 일괄 공급    |
| **클라이언트**  | 구체 클래스를 직접 new 하지 않고 **팩토리만 의존**   |

**효과**

* 런타임에 제품군을 통째로 교체 (Windows ↔ Mac ↔ Web)
* 새 제품군 추가 시 구체 팩토리만 확장 ⇒ 기존 클라이언트 수정 無

---

## 2. 구조 다이어그램 (텍스트)

```
┌──────────────┐       ┌─────────────┐
│ GUIFactory   │──────▶│ Button      │
│ (Abstract)   │       └─────────────┘
│ +create_btn()│        ▲         ▲
│ +create_chk()│        │         │
└──────────────┘   ┌────┴───┐ ┌───┴────┐
        ▲          │WinBtn  │ │MacBtn  │
        │          └────────┘ └────────┘
        │
┌───────┴────────┐
│ WindowsFactory │ … 같은 방식으로 Checkbox 도 연결
└────────────────┘
```

---

## 3. Python 구현 예시

```python
from __future__ import annotations
from abc import ABC, abstractmethod


# ===== 1) Abstract Products =====
class Button(ABC):
    @abstractmethod
    def click(self) -> str: ...


class Checkbox(ABC):
    @abstractmethod
    def check(self) -> str: ...


# ===== 2) Concrete Products =====
class WinButton(Button):
    def click(self) -> str:
        return "✅  Windows 버튼 클릭"


class MacButton(Button):
    def click(self) -> str:
        return "🍎  Mac 버튼 클릭"


class WinCheckbox(Checkbox):
    def check(self) -> str:
        return "☑️   Windows 체크"


class MacCheckbox(Checkbox):
    def check(self) -> str:
        return "🔘  Mac 체크"


# ===== 3) Abstract Factory =====
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...
    @abstractmethod
    def create_checkbox(self) -> Checkbox: ...


# ===== 4) Concrete Factories =====
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# ===== 5) Client Code =====
def render_gui(factory: GUIFactory) -> None:
    btn = factory.create_button()
    chk = factory.create_checkbox()
    print(btn.click())
    print(chk.check())


if __name__ == "__main__":
    # 플랫폼이 Windows일 때
    render_gui(WindowsFactory())
    # 플랫폼이 MacOS일 때
    render_gui(MacFactory())
```

**실행 결과**

```
✅  Windows 버튼 클릭
☑️   Windows 체크
🍎  Mac 버튼 클릭
🔘  Mac 체크
```

---

### 제품군 대응표

| 제품군     | Button 클래스  | Checkbox 클래스  |
| ------- | ----------- | ------------- |
| Windows | `WinButton` | `WinCheckbox` |
| macOS   | `MacButton` | `MacCheckbox` |

---

## 4. 패턴 적용 시나리오

| 도메인            | 적용 이유                                       |
| -------------- | ------------------------------------------- |
| **다중-플랫폼 UI**  | 데스크톱·웹·모바일 각각의 위젯 세트를 교체                    |
| **DB 연결 드라이버** | MySQL, PostgreSQL, SQLite 커넥터를 동일 인터페이스로 생성 |
| **클라우드 SDK**   | AWS vs Azure 객체 스토리지 클라이언트를 환경에 맞춰 주입       |
| **게임 엔진 스킨**   | 다양한 테마(판타지, SF) UI 셋을 런타임에 스위칭              |

---

## 5. 장 · 단점 요약

|          | 👍 장점                    | ⚠️ 단점           |
| -------- | ------------------------ | --------------- |
| **유지보수** | 제품군 추가 시 기존 코드 수정 없음     | 클래스 수 증가, 복잡도 ↑ |
| **일관성**  | 한 팩토리가 만드는 객체끼리는 *호환 보장* | 제품간 교차 조합 어려움   |
| **테스트**  | 팩토리 Mock 주입 → 단위 테스트 쉬움  |                 |

---

## 6. 파이썬 실전 Tip

* **의존성 주입(DI)** 컨테이너(`fastapi.Depends`, `injector`)에 구체 팩토리 바인딩.
* **플러그인 구조** : 각 플러그인을 “팩토리 모듈”로 등록 → 런타임 `entry_points` 로 탐색.
* **dataclass + Protocol** 로 제품 인터페이스 간소화 가능.

---

### 결론

> 추상 팩토리는 **“플랫폼별·벤더별로 묶어서 갈아끼우는”** 상황에서 코드 수정 0 으로 제품군을 교체하게 해 준다. 🚀
