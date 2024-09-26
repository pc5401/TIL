# `never` 타입

### `never` 타입을 알아보자

TypeScript에서 `never` 타입은 특정 함수가 절대 값을 반환하지 않거나, 함수 실행이 끝나지 않는 경우에 사용된다. 이는 주로 예외를 던지거나 무한 루프와 같은 상황에서 활용된다.

### `never` 타입의 조건

`never` 타입을 사용하려면 다음 두 가지 조건을 모두 만족해야 한다:

1. **절대 값을 반환하지 않아야 한다.**
2. **함수 실행이 끝나지 않아야 한다.** (전문용어로 "end point가 없어야 한다")

실제로 조건 1과 조건 2는 동일한 의미를 가지며, 함수가 종료되지 않음을 의미한다.

```tsx
function infiniteLoop(): never {
  while (true) {
    console.log('무한 루프 중...');
  }
}
```

위의 함수는 무한 루프를 실행하므로 종료되지 않으며, 따라서 `never` 타입을 반환 타입으로 지정할 수 있다.

### `throw`를 사용하는 함수

함수가 예외를 던지면 함수는 종료되지 않으므로 `never` 타입을 반환할 수 있다.

```tsx
function throwError(message: string): never {
  throw new Error(message);
}
```

이 함수는 항상 예외를 던지기 때문에 어떤 값도 반환하지 않는다.

### `never` 타입의 사용 사례

### 잘못된 타입 좁히기

타입 좁히기(Type Narrowing)를 할 때, 불가능한 경우를 처리하기 위해 `never` 타입이 사용될 수 있다. 이는 코드의 안전성을 높이고, 모든 가능한 경우를 처리하도록 강제한다.

```tsx
function processValue(value: string | number) {
  if (typeof value === 'string') {
    console.log(`문자열 길이: ${value.length}`);
  } else if (typeof value === 'number') {
    console.log(`숫자 값: ${value}`);
  } else {
    // 이 경우는 절대 발생하지 않으므로 `never` 타입을 사용하여 에러를 발생시킨다.
    const exhaustiveCheck: never = value;
    throw new Error(`Unhandled type: ${exhaustiveCheck}`);
  }
}
```

위 함수에서 `value`는 `string` 또는 `number` 타입만 가질 수 있으므로, `else` 블록은 실행되지 않아야 한다. 그러나 TypeScript는 모든 가능한 타입을 처리했는지 확인하기 위해 `never` 타입을 사용한다.

### 타입 배열 초기화 시 `never`

TypeScript의 엄격한 타입 검사(`strict` 옵션)를 활성화하면, 빈 배열을 초기화할 때 타입을 명확히 지정하지 않으면 `never[]` 타입이 할당될 수 있다.

```tsx
let arr: never[] = [];
// arr.push(1); // 에러: Type '1' is not assignable to type 'never'
```

이 경우, 배열의 타입을 명확히 지정하여 해결할 수 있다.

```tsx
let numbers: number[] = [];
numbers.push(1); // 정상 동작
```

### 자동으로 `never` 타입이 할당되는 경우

TypeScript는 특정 상황에서 자동으로 `never` 타입을 할당할 수 있다. 예를 들어, 함수 표현식에서 반환 타입을 명시하지 않고 예외를 던지거나 무한 루프를 실행하는 경우이다.

```tsx
// 함수 선언문
function terminate(): never {
  throw new Error('종료!');
}

// 함수 표현식
const terminateFunc = function (): never {
  while (true) {}
}
```

### `never` 타입을 사용하는 이유

`never` 타입은 코드의 안전성을 높이고, 예기치 않은 타입 오류를 방지하는 데 도움을 준다. 이를 통해 모든 가능한 타입을 처리하도록 강제하고, 코드의 완전성을 확보할 수 있다.

### 연습 과제 1: `terminate` 함수 작성

다음 조건을 만족하는 `terminate` 함수를 작성하라.

1. 함수는 절대 값을 반환하지 않는다.
2. 함수 내부에서 예외를 던진다.

**예제 구현:**

```tsx
function terminate(message: string): never {
  throw new Error(message);
}

terminate('프로그램을 종료합니다.');
```

### 연습 과제 2: 타입 좁히기에서 `never` 사용

다음 함수에서 `never` 타입을 활용하여 모든 가능한 타입을 처리하도록 수정하라.

```tsx
function handleInput(input: string | number) {
  if (typeof input === 'string') {
    console.log(`입력된 문자열: ${input}`);
  } else if (typeof input === 'number') {
    console.log(`입력된 숫자: ${input}`);
  } else {
    // 여기에 `never` 타입을 사용하여 에러를 던지도록 수정하라.
    const exhaustiveCheck: never = input;
    throw new Error(`Unhandled type: ${exhaustiveCheck}`);
  }
}
```

**설명:**

1. `input`의 타입이 `string` 또는 `number`인 경우를 처리한다.
2. 다른 타입이 들어올 경우는 없으므로 `never` 타입을 사용하여 에러를 던진다.

### 결론

TypeScript의 `never` 타입은 특정 함수가 절대 값을 반환하지 않거나, 함수 실행이 끝나지 않는 경우에 사용된다. 이는 코드의 안전성을 높이고, 모든 가능한 타입을 처리하도록 강제함으로써 예기치 않은 오류를 방지하는 데 중요한 역할을 한다. `never` 타입을 적절히 활용하여 더욱 견고한 코드를 작성할 수 있다.