# Narrowing & Assertion

## Narrowing & Assertion: 타입 확정하기

TypeScript에서 타입 좁히기(`Narrowing`)와 타입 단언(`Assertion`)은 코드의 안정성을 높이고, 예기치 않은 타입 관련 오류를 방지하는 데 중요한 역할을 한다. 타입 좁히기는 제어 흐름을 통해 타입을 명확히 하는 반면, 타입 단언은 개발자가 타입을 확신할 때 사용하여 컴파일러의 타입 체크를 우회한다. 이 두 가지 기법을 적절히 활용하여 보다 안전하고 견고한 코드를 작성할 수 있다.

### 타입 확정을 위한 Narrowing

다음 함수는 숫자 또는 문자열을 입력받아 `1`을 더하는 함수이다.

```typescript
function increment(value: number | string) {
  return value + 1; // 에러 발생
}
```

위 코드는 다음과 같은 에러를 발생시킨다.

```arduino
Operator '+' cannot be applied to types 'string | number' and 'number'.
```

`number | string`과 같은 유니언 타입은 모호성을 방지하기 위해 일반적인 조작을 제한한다. 이 문제를 해결하기 위해서는 타입을 하나로 좁히거나 타입 단언(`Type Assertion`)을 사용해야 한다.

### Type Narrowing

Type Narrowing은 `if` 문과 같은 제어 흐름 구조를 사용하여 유니언 타입 변수의 특정 타입을 결정하는 방법이다.

```typescript
function increment(value: number | string) {
  if (typeof value === 'number') {
    return value + 1;
  } else if (typeof value === 'string') {
    return value + '1';
  } else {
    return 0;
  }
}
```

이 예제에서는 `typeof` 연산자를 사용하여 `value`의 타입이 `number`인지 `string`인지를 확인하고, 각 타입에 맞는 연산을 수행한다. TypeScript는 모든 가능한 타입을 처리하도록 요구하므로, `else` 블록이 필요하다. 이는 잠재적인 버그를 방지하기 위한 것이다.

- **참고 사항**:
    - `in`이나 `instanceof`와 같은 다른 연산자도 타입 좁히기에 사용할 수 있다.
    - 타입 좁히기를 위한 제어 흐름 문에서 마지막 `else` 블록을 생략하면 컴파일 에러가 발생하여 모든 가능한 타입이 처리되었는지 확인한다.

### Type Assertion

타입 단언(Type Assertion)은 개발자가 변수의 타입을 명시적으로 지정하여 TypeScript의 타입 추론을 무시하는 방법이다.

```typescript
function increment(value: number | string) {
  return (value as number) + 1;
}

console.log(increment(123)); // 출력: 124
```

위 예제에서 `value as number`는 `value`를 `number` 타입으로 단언하여 더하기 연산을 가능하게 한다. 그러나 이는 런타임 시점의 타입을 변경하지 않는다.

**타입 단언의 특징**:

1. **타입 축소(Type Reduction)**: 복잡한 타입을 더 구체적인 타입으로 좁히는 역할을 한다. 예를 들어, `number` 타입을 `string`으로 단언하려고 하면 에러가 발생한다.
2. **임시 무시**: 타입 단언은 단지 컴파일러에게 특정 타입을 사용하겠다고 알리는 것이며, 실제 코드 실행에는 영향을 미치지 않는다.

**주의 사항**:

- 개발자가 변수의 타입을 정확히 알고 있을 때만 타입 단언을 사용해야 한다.
- 과도하거나 잘못된 타입 단언은 런타임 에러를 유발할 수 있다.

**사용 예**:

타입 단언은 다음과 같은 상황에서 유용하게 사용할 수 있다.

1. **임시 에러 해결**: 복잡한 타입 에러를 일시적으로 해결할 때.
2. **확실한 타입 지식**: 개발자가 변수의 타입을 명확히 알고 있을 때, 컴파일러의 타입 체크를 우회할 때.

**예제: 타입 캐스팅 유틸리티 함수 생성**

```typescript
type Person = {
  name: string;
};

function castToType<T>(data: string): T {
  return JSON.parse(data) as T;
}

const john = castToType<Person>('{"name":"John"}');
```

위 예제에서 `castToType` 함수는 JSON 문자열을 파싱하고 이를 지정된 제네릭 타입 `T`로 단언한다. 이는 유연하고 재사용 가능한 타입 캐스팅을 가능하게 하지만, 입력 데이터의 정확성에 대한 확신이 필요하다.

### 적용 예시

### 예시 1: 혼합 타입 배열 클리닝

숫자와 숫자를 나타내는 문자열이 섞인 배열을 입력받아 모든 요소를 숫자로 변환하는 함수를 작성하기

**예제**:

```typescript
cleanArray(['1', 2, '3']); // 반환: [1, 2, 3]
```

**함수 요구 사항**:

- 입력 타입: `(number | string)[]`
- 반환 타입: `number[]`
- 문자열로 표현된 숫자를 실제 숫자로 변환

**예제 구현**:

```typescript
function cleanArray(arr: (number | string)[]): number[] {
  return arr.map(element => typeof element === 'string' ? Number(element) : element);
}

console.log(cleanArray(['1', 2, '3'])); // 출력: [1, 2, 3]
```

### 예시 2: 선생님 객체에서 마지막 과목 추출

다음과 같은 선생님 객체가 있을 때, 각 선생님이 가르치는 과목 중 마지막 과목을 반환하는 함수를 작성하기

**예제 데이터**:

```typescript
const teacherA = { subject: 'math' };
const teacherB = { subject: ['science', 'english'] };
const teacherC = { subject: ['science', 'art', 'korean'] };
```

**함수 요구 사항**:

- 입력 타입: `{ subject: string | string[] }`
- 반환 타입: `string`
- 단일 과목은 그대로 반환
- 다중 과목은 마지막 과목을 반환
- 예상치 못한 구조의 객체는 타입 에러를 발생

**예제 구현**:

```typescript
function extractLastSubject(teacher: { subject: string | string[] }): string {
  if (typeof teacher.subject === 'string') {
    return teacher.subject;
  } else if (Array.isArray(teacher.subject)) {
    return teacher.subject[teacher.subject.length - 1];
  } else {
    throw new Error('Invalid teacher object');
  }
}

console.log(extractLastSubject({ subject: ['english', 'art'] })); // 출력: 'art'
console.log(extractLastSubject({ subject: 'math' })); // 출력: 'math'
console.log(extractLastSubject({ hello: 'hi' })); // 타입 에러 발생
```

### 추가 참고 사항

타입 좁히기와 타입 단언에 대한 자세한 정보는 TypeScript 핸드북을 참고

### 콘솔 로그 출력 방법

변수를 콘솔에 출력하려면 `console.log()` 함수를 사용한다. 이를 위해서는 HTML 파일에 컴파일된 JavaScript 파일을 포함시켜야 한다.

**예제 HTML 설정**:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>TypeScript 콘솔</title>
</head>
<body>
  <script src="index.js"></script>
</body>
</html>
```

TypeScript 파일을 JavaScript로 컴파일한 후, HTML 파일을 브라우저에서 열고 개발자 도구의 콘솔을 통해 출력 결과를 확인할 수 있다. 또는 TypeScript 파일을 직접 실행할 수 있는 에디터 확장 기능을 사용하는 것도 방법이다.