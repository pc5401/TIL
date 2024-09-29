# 타입을 파라미터로 입력하는 Generic

함수를 만들 때 보통 `()` 안에 파라미터를 입력한다. 하지만 타입스크립트를 사용하면 파라미터로 타입을 입력할 수도 있다. `<>` 안에 타입을 넣으면 된다.

> 함수의 반환값 타입이 애매할 때
> 

예를 들어, **1.** 어떤 배열을 입력하면 **2.** 그 배열의 첫 번째 요소를 그대로 출력해주는 함수를 만들어보자.

```tsx
function 함수(x: unknown[]) {
  return x[0];
}

let a = 함수([4, 2]);
console.log(a);
```

이렇게 하면 콘솔창에 `4`가 출력된다. 하지만 `a`의 타입을 확인해보면 숫자가 아닌 `unknown` 타입이다. 이는 입력하는 배열도 `unknown[]` 타입이기 때문이다.

여기서 중요한 포인트는 **타입스크립트는 타입을 알아서 변경해주지 않는다.** 숫자가 반환되면 "number 타입입니다~", 문자가 반환되면 "string 타입입니다~" 이렇게 자동으로 처리해주지 않는다는 것이다.

```tsx
function 함수(x: unknown[]) {
  return x[0];
}

let a = 함수([4, 2]);
console.log(a + 1);
```

그래서 이런 연산도 에러가 난다. `a`는 사람이 보기에 분명히 숫자지만, 타입은 `unknown`이다. 함수의 반환 타입을 `:number`처럼 명시적으로 지정하지 않는 한, 타입은 변하지 않는다.

따라서 함수에 불확실한 `unknown`, `any`, `union` 타입을 입력하면 반환값도 그에 따라 불확실한 타입이 되어 문제가 생긴다. 예를 들어, "함수가 10을 반환하는데 타입이 `unknown`이라서 마음대로 조작을 못하네" 같은 문제다.

해결책은 두 가지다:

1. **Narrowing**을 잘 하면 된다. 하지만 귀찮을 수 있다.
2. 함수에 타입을 파라미터로 미리 입력하는 방법이 있다. 원하는 곳에 가변적으로 타입 지정이 가능하다.

두 번째 방법을 **Generic**이라고 부른다.

> Generic 적용한 함수 만들기
> 

함수에 `<>`를 사용하면 타입 파라미터를 입력할 수 있다. 여기 안에는 타입만 입력할 수 있다.

```tsx
function 함수<MyType>(x: MyType[]): MyType {
  return x[0];
}

let a = 함수<number>([4, 2]);
let b = 함수<string>(['kim', 'park']);
```

함수를 사용할 때 `<>` 안에 타입을 입력할 수 있다. `함수<number>()` 이렇게 쓰는 순간 `MyType`에 `number`가 들어간다. 그러면 `function 함수(x: number[]): number { }`와 동일하게 동작한다.

이렇게 하면 반환되는 타입이 명확해진다. `b` 변수의 타입은 `string`이다.

결론적으로, Generic을 사용하면 원하는 타입을 반환하는 함수를 만들 수 있다. `<>` 문법만 잘 쓰면 된다.

```tsx
function 함수<MyType>(x: MyType[]): MyType {
  return x[0];
}

let a = 함수([4, 2]);
let b = 함수(['kim', 'park']);
```

사실 함수 사용 시 `<>`를 생략해도 타입스크립트가 타입을 추론해준다.

참고:

- 타입 파라미터는 자유롭게 작명할 수 있다. 보통 `<T>`를 많이 사용한다.
- 일반 파라미터처럼 타입 파라미터도 여러 개 사용할 수 있다.

> 그런데 왜 - 1은 불가능한가?
> 

다음과 같은 함수를 만들었는데 에러가 난다.

```tsx
function 함수<MyType>(x: MyType) {
  return x - 1;
}

let a = 함수<number>(100);
```

`<MyType>` 자리에 `number`를 넣으면 `MyType` 붙은 곳에 모두 `number`가 들어간다면서, 왜 `x - 1`은 안 되는 걸까?

이유는 에러 메시지를 보면 알 수 있다:

```arduino
Operator '-' cannot be applied to types 'MyType' and 'number'.
```

`MyType`에 `number` 말고도 다른 타입이 들어올 수 있으므로, 타입스크립트는 미리 에러를 내준다.

해결책은 두 가지다:

1. **Narrowing**을 사용한다.
2. **Generic 타입 제한**을 사용한다.

> Generic 타입 제한하기 (Constraints)
> 

`extends` 문법을 사용하면 타입 파라미터에 넣을 수 있는 타입을 제한할 수 있다. `MyType extends number`라고 쓰면 `MyType`은 `number` 타입이거나 그 서브타입이어야 한다.

```tsx
function 함수<MyType extends number>(x: MyType) {
  return x - 1;
}

let a = 함수<number>(100); // 잘 된다
```

이렇게 하면 에러 없이 잘 동작한다. 반환 타입 지정을 따로 하지 않아도 타입스크립트가 추론해준다.

> 커스텀 타입도 extends 가능하다
> 

예를 들어, 문자열을 입력하면 그 길이를 출력해주는 함수를 만들고 싶다.

```tsx
function 함수<MyType>(x: MyType) {
  return x.length;
}

let a = 함수<string>('hello');
```

하지만 이 코드는 에러가 난다. `MyType`에 `string`을 넣었지만, 나중에 `number` 같은 다른 타입을 넣을 수도 있기 때문에 타입스크립트가 에러를 내준다.

그래서 `extends`를 사용해 `MyType`을 제한하면 된다. 이번에는 인터페이스를 만들어보자.

```tsx
interface LengthCheck {
  length: number;
}

function 함수<MyType extends LengthCheck>(x: MyType) {
  return x.length;
}

let a = 함수<string>('hello'); // 가능
let b = 함수<number>(1234);     // 에러
```

1. `length` 속성을 가진 `LengthCheck` 인터페이스를 만들었다.
2. `MyType`이 `LengthCheck`를 상속하도록 했다.
3. 따라서 `MyType`은 반드시 `length` 속성을 가져야 하며, `x.length`를 사용할 수 있다.

참고로, 클래스에서도 Generic을 사용할 수 있다.

```tsx
class Person<T> {
  name: T;
  constructor(a: T) {
    this.name = a;
  }
}

let a = new Person<string>('kim');
a.name; // string 타입
```

`type` 키워드로 타입 변수에도 사용할 수 있다.

```tsx
type Age<T> = T;
```

**추가로**

Generic은 타입을 마치 함수의 파라미터처럼 받아서 사용할 수 있게 해준다. 이를 통해 코드의 재사용성과 타입 안정성을 높일 수 있다. 특히 복잡한 타입 간의 관계를 표현하거나, 다양한 타입에 대응하는 함수나 클래스를 만들 때 유용하다.

타입 파라미터를 사용할 때는 가능한 한 제한을 두는 것이 좋다. 즉, `extends`를 사용해 타입의 범위를 지정하면 코드의 안정성이 높아진다.