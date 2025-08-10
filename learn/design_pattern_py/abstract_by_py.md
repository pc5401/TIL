# 🏭 추상 팩토리 패턴 (Abstract Factory)

## 0) 서문

여러 플랫폼(UI/DB/클라우드)에서 **서로 연관된 객체 묶음(제품군)**을 통째로 갈아끼우는 요구가 반복된다. 이때 클라이언트 코드를 건드리지 않고 교체 가능하게 만드는 패턴이 추상 팩토리이다. 학습 과정에서 가장 헷갈렸던 지점은 **“새 *제품군* 추가”와 “새 *제품 종류* 추가”의 난이도 차이**이다. 결론적으로, 추상 팩토리는 전자에 강하고 후자에 약하다.

---

## 1) 한 줄 정의

> **서로 연관된 객체 묶음(제품군)**을 생성하는 **통일된 인터페이스**를 제공해서, 런타임에 벤더/테마/플랫폼을 **일괄 교체**할 수 있게 한다.

---

## 2) 내가 교정한 포인트 (중요)

* **제품군 추가는 쉽다.** Windows → macOS → Web 같은 새 “군”을 넣을 때는 **구체 팩토리만** 추가하면 된다. 클라이언트 수정이 없다.
* **제품 *종류* 추가는 어렵다.** 예를 들어 `Slider`라는 새 타입이 늘면, **추상 팩토리 인터페이스, 모든 구체 팩토리, 클라이언트 사용처**가 연쇄적으로 바뀐다. OCP가 깨지기 쉽다. 이 패턴의 본질적 트레이드오프이다.

---

## 3) 구조 (텍스트 다이어그램)

```
┌──────────────┐       ┌─────────────┐
│ GUIFactory   │──────▶│ Button      │
│ (Abstract)   │       └─────────────┘
│ +createBtn() │       ┌─────────────┐
│ +createChk() │─────▶ │ Checkbox    │
└──────────────┘       └─────────────┘
      ▲
      │                 (각 제품군 별 구체 제품)
┌─────┴─────────┐   ┌────────┐   ┌────────┐
│ WindowsFactory│→  │WinBtn  │   │WinChk  │
└───────────────┘   └────────┘   └────────┘
┌───────────────┐   ┌────────┐   ┌────────┐
│ MacFactory    │→  │MacBtn  │   │MacChk  │
└───────────────┘   └────────┘   └────────┘
```

---

## 4) Python 예시 (Protocol + 레지스트리 + 런타임 선택)

ABC도 가능하지만, **`typing.Protocol`**로 구조적 서브타이핑을 쓰면 유연해진다. 또한 **레지스트리**로 팩토리를 이름 기반 선택이 된다.

```python
from __future__ import annotations
from typing import Protocol, runtime_checkable, Dict, Type
import os

# 1) Abstract Products
@runtime_checkable
class Button(Protocol):
    def click(self) -> str: ...

@runtime_checkable
class Checkbox(Protocol):
    def check(self) -> str: ...

# 2) Concrete Products
class WinButton:
    def click(self) -> str:
        return "✅ Windows 버튼 클릭"

class MacButton:
    def click(self) -> str:
        return "🍎 Mac 버튼 클릭"

class WinCheckbox:
    def check(self) -> str:
        return "☑️ Windows 체크"

class MacCheckbox:
    def check(self) -> str:
        return "🔘 Mac 체크"

# 3) Abstract Factory
class GUIFactory(Protocol):
    def create_button(self) -> Button: ...
    def create_checkbox(self) -> Checkbox: ...

# 4) Concrete Factories
class WindowsFactory:
    def create_button(self) -> Button: return WinButton()
    def create_checkbox(self) -> Checkbox: return WinCheckbox()

class MacFactory:
    def create_button(self) -> Button: return MacButton()
    def create_checkbox(self) -> Checkbox: return MacCheckbox()

# 5) Registry & Selector
FACTORIES: Dict[str, Type[GUIFactory]] = {
    "windows": WindowsFactory,
    "mac": MacFactory,
}

def get_factory(name: str | None = None) -> GUIFactory:
    key = (name or os.getenv("APP_THEME") or "windows").lower()
    if key not in FACTORIES:
        raise ValueError(f"Unknown factory '{key}'. available={list(FACTORIES)}")
    return FACTORIES[key]()  # type: ignore[call-arg]

# 6) Client
def render_gui(factory: GUIFactory) -> None:
    btn = factory.create_button()
    chk = factory.create_checkbox()
    print(btn.click())
    print(chk.check())

if __name__ == "__main__":
    render_gui(get_factory("windows"))
    render_gui(get_factory("mac"))
```

### 테스트 메모 (pytest)

제품군 일관성만 검증하면 된다. 파라미터라이즈드 테스트로 간결해진다.

```python
import pytest

from myapp.gui import WindowsFactory, MacFactory, GUIFactory, Button, Checkbox

@pytest.mark.parametrize("factory_cls", [WindowsFactory, MacFactory])
def test_family_consistency(factory_cls: type[GUIFactory]):
    f = factory_cls()
    btn: Button = f.create_button()
    chk: Checkbox = f.create_checkbox()
    assert isinstance(btn.click(), str)
    assert isinstance(chk.check(), str)
```

---

## 5) TypeScript 미니 예시 (웹/프론트엔드 감각)

DI(inversify/tsyringe)나 환경별 번들 스플리팅과 조합하면 플랫폼 스왑이 자연스럽다.

```ts
interface Button { click(): string }
interface Checkbox { check(): string }

class WebButton implements Button { click() { return "🌐 Web 버튼"; } }
class WebCheckbox implements Checkbox { check() { return "☑️ Web 체크"; } }
class MobileButton implements Button { click() { return "📱 Mobile 버튼"; } }
class MobileCheckbox implements Checkbox { check() { return "🔘 Mobile 체크"; } }

interface GUIFactory {
  createButton(): Button;
  createCheckbox(): Checkbox;
}

class WebFactory implements GUIFactory {
  createButton() { return new WebButton(); }
  createCheckbox() { return new WebCheckbox(); }
}
class MobileFactory implements GUIFactory {
  createButton() { return new MobileButton(); }
  createCheckbox() { return new MobileCheckbox(); }
}

function render(f: GUIFactory) {
  const b = f.createButton(); const c = f.createCheckbox();
  console.log(b.click(), c.check());
}

render(new WebFactory());
render(new MobileFactory());
```

---

## 6) 현업 적용 메모

* **DI와 결합**: FastAPI `Depends(get_factory)`로 주입하면 라우트/서비스가 구체 타입을 모른다.
* **플러그인화**: 파이썬 `importlib.metadata.entry_points()`로 “팩토리 플러그인” 자동 등록이 가능하다.
* **무상태 팩토리**: 보통 무상태이다. 싱글턴으로 써도 된다(테스트 편의는 유지한다).
* **가족 규약**: 접근성 토큰, 테마 토큰, 국제화 정책을 “가족 규약”으로 문서화하면 교차 혼용을 방지한다.

---

## 7) 언제 쓰고, 언제 피하나

**쓴다**

* 멀티 플랫폼/테마에서 **묶음 교체**가 핵심 가치일 때
* DB/클라우드 **벤더 스왑**을 주기적으로 수행할 때
* **플러그인 생태계**로 확장할 때

**피한다**

* **제품 종류가 자주 늘어나는** 도메인일 때 (Strategy/단일 Factory Method/서비스 로케이터/DI 바인딩이 단순할 수 있다)
* 가족 일관성 가치가 낮아 **과설계**가 우려될 때
* 클래스 폭증이 유지보수에 부담이 될 때

---

## 8) 인접 패턴 비교

* **Factory Method**: 단일 제품 생성 책임을 서브클래스에 위임한다. “가족” 개념은 없다.
* **Builder**: 복잡한 객체를 단계적으로 조립한다. 목적이 다르다.
* **Strategy**: 알고리즘 교체(행위)이다. 추상 팩토리는 구조적 생성이다.
* **Bridge**: 추상과 구현을 분리해 조합을 늘린다. 조합 수가 많으면 Bridge + 추상 팩토리 혼용을 검토한다.

---

## 10) 회고

추상 팩토리는 “**묶음 교체**”라는 문제를 가장 깔끔하게 해결한다. 다만 인터페이스 표면적이 넓어서 **새 제품 종류**가 늘어날수록 변경 비용이 누적된다.즉 **벤더/테마 스왑 빈도가 높고, 제품 타입 셋이 비교적 안정적일 때 가장 빛난다.** 