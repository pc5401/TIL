# 함수 타입 지정

함수는 긴 코드를 짧게 축약하거나, 어떤 자료를 입력하면 다른 자료를 반환하는 역할을 한다. 예를 들어, 2를 입력하면 4를 반환하고, 4를 입력하면 8을 반환하는 곱셈 기계를 만들고 싶다면 함수를 사용하면 된다.

```tsx
function multiplyByTwo(x) {
  return x * 2;
}

multiplyByTwo(2); // 4
multiplyByTwo(4); // 8
```

여기서 소괄호 안에 들어가는 `x` 같은 값을 **파라미터**라고 부르고, `return` 오른쪽에 있는 값을 **리턴값**이라고 한다.

1. **파라미터**를 정의하면 함수를 사용할 때 소괄호 안에 값을 넣을 수 있다.
2. **리턴값**은 함수가 실행된 후 그 자리에 남는 값이다.

`내함수(2)` 이렇게 쓰면 실제로 그 자리에 `return` 우측에 있던 값이 남는다.

## 함수에 타입 지정하는 방법

함수는 총 두 군데에 타입 지정을 할 수 있다.

1. 함수로 들어오는 자료 (**파라미터**)
2. 함수에서 나가는 자료 (**리턴값**)

```tsx
function multiplyByTwo(x: number): number {
  return x * 2;
}
```

1. **파라미터 타입 지정**은 파라미터 옆에 적는다.
2. **리턴값 타입 지정**은 함수명 우측에 `:` 다음에 적는다.

이렇게 타입을 지정하면, 파라미터와 리턴값이 예상한 타입과 다를 경우 타입스크립트가 에러를 발생시킨다.

- **주의**: 파라미터에 타입을 지정하면 **필수 파라미터**가 된다. 즉, 해당 파라미터를 반드시 전달해야 한다.

### `void` 타입

함수의 리턴값이 없을 경우 `void` 타입을 사용할 수 있다. `void`는 '아무것도 없음'을 뜻하는 타입이다.

```tsx
function logMessage(msg: string): void {
  console.log(msg);
}

logMessage('안녕하세요'); // '안녕하세요' 출력
```

이렇게 하면 함수에서 `return`을 사용할 수 없게 된다. `void` 타입은 함수의 리턴값을 방지하고 싶을 때 활용할 수 있다.

### 파라미터가 옵션일 경우

함수의 파라미터가 필수가 아닌 경우, 즉 옵션인 경우에는 파라미터명 옆에 `?`를 붙여서 타입을 지정한다.

```tsx
function printNumber(x?: number) {
  console.log(x);
}

printNumber();    // undefined 출력
printNumber(2);   // 2 출력
```

여기서 `x?: number`는 `x: number | undefined`와 동일한 의미이다. 즉, `x`에는 `number` 또는 `undefined`가 들어올 수 있다.

### 엄격한 타입 검사와 Union 타입

타입스크립트는 함수의 파라미터나 변수의 타입이 확실하지 않으면 연산을 수행할 수 없다.

예를 들어, 숫자 또는 문자를 입력하면 그 값에 1을 더해주는 함수를 만들고 싶다고 하자.

```tsx
function add(x: number | string) {
  // return x + 1; // 에러 발생
}
```

이렇게 하면 타입스크립트는 에러를 발생시킨다. `x`의 타입이 `number | string`이라서, 어떤 타입이 올지 확실하지 않기 때문이다. 이럴 때는 **타입 좁히기(Narrowing)**를 사용해야 한다.

```tsx
function add(x: number | string) {
  if (typeof x === 'number') {
    return x + 1;
  } else {
    return String(Number(x) + 1);
  }
}

add(2);       // 3
add('2');     // '3'
```

또는 타입 어서션(Type Assertion)을 사용할 수 있지만, 이는 타입스크립트의 엄격한 검사를 무시하므로 권장되지 않는다.

```tsx
function add(x: number | string) {
  return (x as number) + 1;
}
```

### 옵션 파라미터와 `undefined`

옵션 파라미터는 `number | undefined` 타입을 가지므로, 함수 내부에서 해당 파라미터를 사용할 때는 타입 검사를 해야 한다.

```tsx
function multiplyOrDefault(x?: number): number {
  if (x !== undefined) {
    return x * 2;
  } else {
    return 0;
  }
}
```

또는 파라미터의 기본값을 지정할 수도 있다.

```tsx
function multiplyOrDefault(x: number = 10): number {
  return x * 2;
}

multiplyOrDefault();    // 20
multiplyOrDefault(5);   // 10
```