# 🌉 Bridge Pattern — “추상과 구현을 독립적으로 확장하기”

> **키워드**
> 행위를 정의하는 **추상(Abstraction)** 과
> 실제 일하는 **구현(Implementation)** 을 **별도 계층으로 분리** →
> 둘을 **런타임에 브리지(다리)** 로 연결한다.

---

## 1. 왜 쓰나?

| 증상                                                     | 문제                                   |
| ------------------------------------------------------ | ------------------------------------ |
| 기능 계층(A·B·C) × 플랫폼(Windows·Mac·Linux) → **N×M 클래스 폭발** | 클래스 상속만 쓰면 “기능 + 플랫폼” 조합별 하위 클래스가 필요 |
| ‘UI 위젯’ 계열과 ‘스킨/테마’ 계열이 독립 진화                          | 하나 바꿀 때 다른 계층도 코드 수정                 |
| 라이브러리(저수준)와 애플리케이션(고수준)을 느슨하게 결합                       | 완전한 인터페이스 구조체 필요한데, 두 계층 추가·교체 쉽지 않음 |

**Bridge** 패턴은 *기능 계층* 과 *플랫폼 계층* 을 **별도 상속 계층**으로 두고
객체 합성(HAS-A)으로 런타임 연결 → **조합 폭발을 해결**.

---

## 2. 구조 도식

```
Abstraction                Implementation
--------------            ------------------
Shape (abstract)    ⟂    Renderer (interface)
   │                         ▲
   ├─ Circle               RasterRenderer
   └─ Square               VectorRenderer
```

* **Abstraction** : 고수준 인터페이스. `self.impl`(Implementation)을 **참조**만.
* **RefinedAbstraction** : 구체 기능 클래스(예: `Circle`)
* **Implementation** : 플랫폼/저수준 작업 인터페이스
* **ConcreteImplementation** : 실제 렌더링, DB, OS 호출 등

---

## 3. Python 예제 — **도형 그리기 (벡터 vs 래스터)**

```python
from __future__ import annotations
from abc import ABC, abstractmethod
import math


# ---------- Implementation 계층 ----------
class Renderer(ABC):
    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float): ...


class VectorRenderer(Renderer):
    def draw_circle(self, x, y, radius):
        print(f"🔶 Draw VECTOR circle at ({x},{y}) r={radius}")


class RasterRenderer(Renderer):
    def draw_circle(self, x, y, radius):
        print(f"🖼️  Draw RASTER circle at ({x},{y}) r={radius}")


# ---------- Abstraction 계층 ----------
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self._r = renderer

    @abstractmethod
    def draw(self): ...
    @abstractmethod
    def resize(self, factor: float): ...


class Circle(Shape):
    def __init__(self, renderer: Renderer, x: float, y: float, radius: float):
        super().__init__(renderer)
        self.x, self.y, self.radius = x, y, radius

    def draw(self):
        self._r.draw_circle(self.x, self.y, self.radius)

    def resize(self, factor: float):
        self.radius *= factor


# ---------- Client ----------
if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()

    circle1 = Circle(vector, 0, 0, 5)
    circle2 = Circle(raster, 2, 3, 10)

    circle1.draw()                 # 🔶 vector
    circle2.draw()                 # 🖼️ raster

    circle1.resize(2)
    circle1.draw()                 # radius 10, vector 그대로
```
