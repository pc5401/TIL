# TypeScript의 #을 사용한 private 필드 선언

TypeScript에서 `#`을 사용하여 private 속성을 선언하는 것은 ECMAScript에 의해 도입된 private class field 문법이다. 이는 TypeScript의 생성자 매개변수에 사용할 수 없다. 생성자 매개변수에서 private 접근 제어자를 사용하려면 `private`나 `protected` 키워드를 사용해야 한다.

예를 들어, TypeScript에서 생성자 매개변수를 private로 선언할 때는 아래와 같이 `private` 키워드를 사용한다.

## private vs #

```typescript
import { Controller, Get } from '@nestjs/common';
import { BoardsService } from './boards.service';

@Controller('boards')
export class BoardsController {
  constructor(private boardsService: BoardsService) {}
}
```
반면, 클래스 내부에서 #을 사용하여 private 필드를 선언하고 싶다면, 아래와 같이 사용할 수 있다.

```typescript
class ExampleClass {
  #privateField: string;

  constructor(value: string) {
    this.#privateField = value;
  }

  getPrivateField() {
    return this.#privateField;
  }
}
```
이 방식은 ECMAScript 표준에 따라 런타임에서 완전히 private하게 보장된다. #은 클래스 외부에서 접근이 불가하며, 생성자 매개변수에는 사용할 수 없다.

## `private`와 `#`의 차이점 및 장단점

TypeScript에서 `private` 키워드와 ECMAScript의 `#`을 사용한 private 필드 선언 방식에는 다음과 같은 차이점과 장단점이 있다.

### `private` 키워드

- **차이점**: `private` 키워드는 TypeScript의 접근 제어자로, 컴파일 시점에서만 접근을 제한한다. 런타임에서는 여전히 접근이 가능하다.
- **장점**:
    - 생성자 매개변수에서 간편하게 사용할 수 있다. 별도의 필드 선언 없이 생성자에서 바로 private 속성을 선언할 수 있다.
    - TypeScript의 풍부한 타입 시스템과 잘 통합되어 있다.
- **단점**:
    - 런타임에서 완전한 은닉이 보장되지 않는다. JavaScript로 컴파일된 후에도 속성에 접근할 수 있다.
    - ECMAScript 표준이 아닌 TypeScript 고유의 기능이므로, JavaScript 환경과의 호환성에 제약이 있을 수 있다.

### `#` (Private Class Fields)

- **차이점**: `#`을 사용한 private 필드는 ECMAScript 표준의 일부로, 실제 런타임에서 완전히 은닉된 필드를 제공한다. TypeScript에서도 지원되지만, 생성자 매개변수에서는 사용할 수 없다.
- **장점**:
    - 런타임에서도 완전히 은닉된 필드를 제공하여 보안성이 높다.
    - JavaScript 표준의 일부로, TypeScript 외의 환경에서도 일관되게 동작한다.
- **단점**:
    - 생성자 매개변수에서 사용할 수 없어, 별도의 필드 선언이 필요하다.
    - 기존 코드와의 호환성 문제나, 일부 레거시 환경에서는 지원되지 않을 수 있다.
    - `#`을 사용한 필드는 클래스 내부에서만 접근할 수 있으며, 클래스 외부에서는 전혀 접근할 수 없기 때문에 유연성이 떨어질 수 있다.

### 요약

`private` 키워드는 TypeScript의 타입 시스템과 통합되어 편리하게 사용할 수 있으나, 런타임 보안 측면에서는 한계가 있다. 반면, `#`을 사용한 private 필드는 ECMAScript 표준을 따르며 런타임에서도 완전한 은닉을 제공하지만, 사용에 있어 약간의 제약이 존재한다. 프로젝트의 요구사항에 따라 적절한 방식을 선택하여 사용하는 것이 중요하다.