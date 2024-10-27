# NestJS 데코레이터 정리

참고 : [NestJS로 배우는 백엔드 프로그래밍](https://product.kyobobook.co.kr/detail/S000200383301)

NestJS는 데코레이터를 적극 활용하여 코드의 가독성과 유지보수성을 높이고, 횡단 관심사(Cross-Cutting Concerns)를 분리하여 관점 지향 프로그래밍(Aspect-Oriented Programming)을 구현한다. 데코레이터는 TypeScript의 실험적인 기능으로, 클래스, 메서드, 접근자, 속성, 매개변수에 적용할 수 있다.

## 데코레이터의 개념

데코레이터는 `@expression` 형태로 사용하며, 여기서 `expression`은 데코레이터된 선언부(클래스, 메서드 등)에 대한 정보를 받아 런타임에 호출되는 함수이다. 데코레이터를 통해 대상의 정의를 읽거나 수정할 수 있으며, 메타데이터를 주입하여 기능을 확장할 수 있다.

## 데코레이터의 종류

TypeScript에서 지원하는 5가지 데코레이터는 다음과 같다.

1. **클래스 데코레이터**
2. **메서드 데코레이터**
3. **접근자 데코레이터**
4. **속성 데코레이터**
5. **매개변수 데코레이터**

---

### 1. 클래스 데코레이터

- **역할**: 클래스의 정의를 읽거나 수정한다.
- **호출 시 전달되는 인자**: `constructor` (클래스의 생성자 함수)
- **사용 위치**: 클래스 선언 바로 위
- **예시 코드**:
    
    ```tsx
    function ReportableClassDecorator<T extends { new (...args: any[]): {} }>(
      constructor: T,
    ) {
      return class extends constructor {
        reportingURL = 'http://www.example.com';
      };
    }
    
    @ReportableClassDecorator
    class BugReport {
      type = 'report';
      title: string;
    
      constructor(t: string) {
        this.title = t;
      }
    }
    
    const bug = new BugReport('Needs dark mode');
    console.log(bug);
    ```
    
- **설명**:
    - 클래스 데코레이터는 클래스의 생성자 함수를 받아 새로운 클래스를 반환할 수 있다.
    - 위 예시에서는 `reportingURL` 속성을 동적으로 추가했다.
    - **주의**: 타입 시스템에서는 새로 추가된 속성을 인식하지 못하므로, 직접 접근할 때 타입 에러가 발생할 수 있다.

---

### 2. 메서드 데코레이터

- **역할**: 메서드의 정의를 읽거나 수정한다.
- **호출 시 전달되는 인자**:
    - `target`: 클래스의 프로토타입 또는 생성자 함수
    - `propertyKey`: 메서드의 이름
    - `descriptor`: 메서드의 속성 디스크립터 (`PropertyDescriptor`)
- **사용 위치**: 메서드 선언 바로 위
- **예시 코드**:
    
    ```tsx
    function HandleError() {
      return function (
        target: any,
        propertyKey: string,
        descriptor: PropertyDescriptor,
      ) {
        const method = descriptor.value;
        descriptor.value = function () {
          try {
            method.apply(this);
          } catch (e) {
            // 에러 핸들링 로직
            console.error('Error caught:', e);
          }
        };
      };
    }
    
    class Greeter {
      @HandleError()
      hello() {
        throw new Error('Test error');
      }
    }
    
    const greeter = new Greeter();
    greeter.hello();
    ```
    
- **설명**:
    - 메서드 데코레이터는 메서드의 속성 디스크립터를 수정하여 기능을 확장할 수 있다.
    - 위 예시에서는 메서드 실행 중 발생한 에러를 캐치하여 처리하는 로직을 추가했다.

---

### 3. 접근자 데코레이터

- **역할**: 접근자(`get`, `set`)의 정의를 읽거나 수정한다.
- **호출 시 전달되는 인자**:
    - `target`: 클래스의 프로토타입 또는 생성자 함수
    - `propertyKey`: 접근자의 이름
    - `descriptor`: 접근자의 속성 디스크립터 (`PropertyDescriptor`)
- **사용 위치**: 접근자 선언 바로 위
- **예시 코드**:
    
    ```tsx
    function Enumerable(enumerable: boolean) {
      return function (
        target: any,
        propertyKey: string,
        descriptor: PropertyDescriptor,
      ) {
        descriptor.enumerable = enumerable;
      };
    }
    
    class Person {
      private _name: string;
    
      constructor(name: string) {
        this._name = name;
      }
    
      @Enumerable(true)
      get name() {
        return this._name;
      }
    
      @Enumerable(false)
      set name(newName: string) {
        this._name = newName;
      }
    }
    
    const person = new Person('Dexter');
    for (const key in person) {
      console.log(`${key}: ${person[key]}`);
    }
    ```
    
- **설명**:
    - 접근자 데코레이터를 사용하여 접근자의 열거 가능 여부를 설정했다.
    - `get name`은 열거 가능하도록, `set name`은 열거 불가능하도록 설정했다.
    - 출력 결과는 `name: Dexter`만 나타난다.

---

### 4. 속성 데코레이터

- **역할**: 속성의 정의를 읽는다.
- **호출 시 전달되는 인자**:
    - `target`: 클래스의 프로토타입 또는 생성자 함수
    - `propertyKey`: 속성의 이름
- **사용 위치**: 속성 선언 바로 위
- **예시 코드**:
    
    ```tsx
    function Format(formatString: string) {
      return function (target: any, propertyKey: string) {
        let value = target[propertyKey];
    
        const getter = () => `${formatString} ${value}`;
        const setter = (newVal: string) => {
          value = newVal;
        };
    
        Object.defineProperty(target, propertyKey, {
          get: getter,
          set: setter,
          enumerable: true,
          configurable: true,
        });
      };
    }
    
    class Greeter {
      @Format('Hello')
      greeting: string;
    
      constructor(message: string) {
        this.greeting = message;
      }
    }
    
    const greeter = new Greeter('World');
    console.log(greeter.greeting); // 출력: Hello World
    ```
    
- **설명**:
    - 속성 데코레이터를 사용하여 속성의 getter와 setter를 정의했다.
    - 속성 데코레이터는 반환값을 무시하지만, 위 예시에서는 `Object.defineProperty`를 통해 속성의 동작을 재정의했다.

---

### 5. 매개변수 데코레이터

- **역할**: 매개변수의 정보를 읽는다.
- **호출 시 전달되는 인자**:
    - `target`: 클래스의 프로토타입 또는 생성자 함수
    - `propertyKey`: 메서드의 이름
    - `parameterIndex`: 매개변수의 인덱스 (0부터 시작)
- **사용 위치**: 매개변수 선언 바로 앞
- **예시 코드**:
    
    ```tsx
    import { BadRequestException } from '@nestjs/common';
    
    function MinLength(min: number) {
      return function (target: any, propertyKey: string, parameterIndex: number) {
        const existingValidators =
          Reflect.getOwnMetadata('validators', target, propertyKey) || [];
        existingValidators.push((args: any[]) => {
          if (args[parameterIndex].length < min) {
            throw new BadRequestException(
              `${propertyKey}의 매개변수 길이는 최소 ${min}이어야 합니다.`,
            );
          }
        });
        Reflect.defineMetadata(
          'validators',
          existingValidators,
          target,
          propertyKey,
        );
      };
    }
    
    function Validate(
      target: any,
      propertyKey: string,
      descriptor: PropertyDescriptor,
    ) {
      const method = descriptor.value;
      descriptor.value = function (...args: any[]) {
        const validators =
          Reflect.getOwnMetadata('validators', target, propertyKey) || [];
        validators.forEach((validator: Function) => validator(args));
        return method.apply(this, args);
      };
    }
    
    class User {
      private name: string;
    
      @Validate
      setName(@MinLength(3) name: string) {
        this.name = name;
      }
    }
    
    const user = new User();
    user.setName('Dexter'); // 정상 동작
    user.setName('De'); // BadRequestException 발생
    ```
    
- **설명**:
    - 매개변수 데코레이터는 매개변수의 정보를 읽어 유효성 검사를 수행할 수 있다.
    - 메서드 데코레이터 `@Validate`와 함께 사용하여 매개변수에 대한 검증 로직을 구현했다.
    - `Reflect` 메타데이터를 활용하여 데코레이터 간의 데이터를 공유했다.

---

## 데코레이터의 특징 요약

| 데코레이터 종류 | 역할 | 호출 시 전달되는 인자 | 사용 불가능한 위치 |
| --- | --- | --- | --- |
| **클래스 데코레이터** | 클래스의 정의를 읽거나 수정 | `constructor` | 선언 파일(`.d.ts`), `declare` 클래스 |
| **메서드 데코레이터** | 메서드의 정의를 읽거나 수정 | `target`, `propertyKey`, `propertyDescriptor` | 선언 파일, `declare` 클래스, 오버로드 메서드 |
| **접근자 데코레이터** | 접근자의 정의를 읽거나 수정 | `target`, `propertyKey`, `propertyDescriptor` | 선언 파일, `declare` 클래스 |
| **속성 데코레이터** | 속성의 정의를 읽음 | `target`, `propertyKey` | 선언 파일, `declare` 클래스 |
| **매개변수 데코레이터** | 매개변수의 정의를 읽음 | `target`, `propertyKey`, `parameterIndex` | 선언 파일, `declare` 클래스 |
- **사용 불가능한 위치**:
    - **선언 파일(`.d.ts` 파일)**: 타입 선언만을 위한 파일로, 데코레이터를 적용할 수 없다.
    - **`declare` 클래스**: 구현이 없는 타입 선언 클래스에도 데코레이터를 적용할 수 없다.
    - **오버로드 메서드**: TypeScript에서 메서드 오버로딩 선언부에는 데코레이터를 적용할 수 없다.

## 참고 사항

- **TypeScript에서의 데코레이터**:
    - 데코레이터는 현재 **실험적인 기능**으로, `tsconfig.json`에서 `experimentalDecorators` 옵션을 `true`로 설정해야 사용 가능하다.
    - 많은 프로젝트에서 안정적으로 사용되고 있으며, NestJS에서도 적극 활용하고 있다.
- **데코레이터의 평가 순서**:
    - 여러 데코레이터를 적용할 때, 데코레이터 팩토리 함수는 **위에서 아래로** 평가되고, 데코레이터 함수는 **아래에서 위로** 호출된다.
    - 예를 들어 `@First`와 `@Second` 데코레이터를 적용하면, `Second`의 팩토리 함수가 먼저 평가되지만, `First`의 데코레이터 함수가 먼저 호출된다.
- **데코레이터의 반환값**:
    - 클래스, 메서드, 접근자 데코레이터는 반환값을 통해 대상의 정의를 변경할 수 있다.
    - 속성 데코레이터와 매개변수 데코레이터의 반환값은 **무시**된다.
- **주의 사항**:
    - 데코레이터를 사용하여 클래스나 메서드의 타입을 변경할 수 있지만, TypeScript의 타입 시스템은 이를 인식하지 못할 수 있다.
    - 타입 안전성을 유지하기 위해서는 인터페이스나 타입 선언을 명시적으로 변경해야 한다.

## 결론

데코레이터는 NestJS와 TypeScript에서 강력한 기능을 제공하여 코드의 재사용성과 가독성을 높여준다. 데코레이터를 활용하면 메타데이터를 주입하고, 기존의 코드를 수정하지 않으면서도 기능을 확장할 수 있다. 각 데코레이터의 특성과 사용 방법을 이해하고 적절히 활용하면, 효율적이고 유지보수하기 쉬운 코드를 작성할 수 있다.