# 🛠️ 팩토리 메서드 패턴 (Factory Method Pattern) — Python 위주 노트

> **의도**
> “*무엇을* 만들지는 **서브클래스**가 결정하고,
> **Creator**(부모)는 **공통 로직**만 보유한다.”

*객체 생성을 전담하는 `factory_method()`를 추출해
클래스 간 **결합도를 낮추고** / **확장성을 높여** 주는 생성 패턴.*

---

## 1. 구조 한눈 보기

| 역할                           | 책임                                                 |
| :--------------------------- | :------------------------------------------------- |
| **Product** *(인터페이스/추상 클래스)* | 생성될 객체의 공통 API 정의                                  |
| **ConcreteProduct**          | Product 구현 A, B, …                                 |
| **Creator** *(추상)*           | `factory_method()` 선언 + 공통 비즈니스 `some_operation()` |
| **ConcreteCreator**          | `factory_method()`를 오버라이드해 **어떤 Product를 만들지** 결정  |

```
Client ──▶ ConcreteCreatorA ──▶ factory_method() ──▶ ConcreteProductA
                ▲
                │ ConcreteCreatorB … → ConcreteProductB
```

---