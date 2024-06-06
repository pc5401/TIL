# **추상 팩토리 패턴**(Abstract Factory Pattern)

> 생성 패턴, 연관성이 있는 **객체 군**이 여러개 있을 경우 이들을 묶어 추상화하고, 어떤 구체적인 상황이 주어지면 팩토리 객체에서 집합으로 묶은 객체 군을 구현화 하는 생성 패턴

- 추상 팩토리의 핵심은 **제품 군집합**을 타입 별로 찍어낼수 있다는 점이 핵심



예시)

```ts
// Abstract Products 추상적인 제품에 대한 인터페이스를 정의
interface Button { // 추상적인 제품 = 버튼
  click(): string;
}

interface Checkbox { // 추상적인 제품 = 체크 박스
  check(): string;
}

// Concrete Products 구체적인 제품
class WindowsButton implements Button {
  public click(): string {
    return "Windows 버튼 클릭";
  }
}

class MacButton implements Button {
  public click(): string {
    return "Mac 버튼 클릭";
  }
}

class WindowsCheckbox implements Checkbox {
  public check(): string {
    return "Windows 체크박스 체크";
  }
}

class MacCheckbox implements Checkbox {
  public check(): string {
    return "Mac 체크박스 체크";
  }
}

// Abstract Factory
interface GUIFactory {
  createButton(): Button;
  createCheckbox(): Checkbox;
}

// Concrete Factories
class WindowsFactory implements GUIFactory {
  public createButton(): Button {
    return new WindowsButton();  // window 버튼
  }

  public createCheckbox(): Checkbox {
    return new WindowsCheckbox();  // window 체크박스
  }
}

class MacFactory implements GUIFactory {
  public createButton(): Button {
    return new MacButton(); // Mac 버튼
  }

  public createCheckbox(): Checkbox {
    return new MacCheckbox(); // Mac 체크박스
  }
}

// 메인
const windowsFactory: GUIFactory = new WindowsFactory();
const winButton: Button = windowsFactory.createButton();
const winCheckbox: Checkbox = windowsFactory.createCheckbox();

console.log(winButton.click());  // "Windows 버튼 클릭"
console.log(winCheckbox.check());  // "Windows 체크박스 체크"

const macFactory: GUIFactory = new MacFactory();
const macButton: Button = macFactory.createButton();
const macCheckbox: Checkbox = macFactory.createCheckbox();

console.log(macButton.click());  // "Mac 버튼 클릭"
console.log(macCheckbox.check());  // "Mac 체크박스 체크"
```

- 코드를 표로 정리하면 다음과 같다.

| 제품군   | 버튼            | 체크박스            |
| ----- | ------------- | --------------- |
| 윈도우   | WindowsButton | WindowsCheckbox |
| MacOS | MacButton     | MacCheckbox     |

### 예시

1. **다중 플랫폼 UI 라이브러리**: Windows, Mac, Linux 등 다양한 플랫폼에 대해 통일된 UI 요소를 생성할 때 사용됩니다.
2. **데이터베이스 연결**: 다양한 종류의 데이터베이스에 연결할 때 연결을 생성하는 팩토리를 구현할 수 있습니다.
3. **API 클라이언트 생성**: 다양한 API 서비스를 동일한 인터페이스로 관리하기 위해 추상 팩토리를 사용할 수 있습니다.

### 유명 라이브러리

1. **Qt**: C++로 작성된 크로스 플랫폼 UI 라이브러리에서 추상 팩토리 패턴을 볼 수 있습니다.
2. **Java's Swing**: Java의 GUI 라이브러리에서도 추상 팩토리 패턴이 적용되어 있습니다.
3. **Spring Framework**: Java의 스프링 프레임워크에서 다양한 방식으로 추상 팩토리 패턴이 적용되어 있습니다.

이러한 패턴을 적용하면, 여러 객체를 생성하는 로직을 캡슐화하여 유지보수가 쉬워지고, 확장성이 높아집니다.
