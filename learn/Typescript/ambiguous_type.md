# 타입 애매할 때

변수에 어떤 타입의 값이 들어올지 애매할 때, TypeScript에서는 여러 가지 방법으로 타입을 지정할 수 있다.

## 유니언 타입 (Union Type)

변수에 **string**이나 **number** 타입이 들어올 수 있다면, `|` 연산자를 사용하여 유니언 타입으로 선언한다.

```tsx
let 이름: string | number = 'kim';
let 나이: string | number = 100;
```

배열이나 객체에도 유니언 타입을 적용할 수 있다.

```tsx
let 배열: (number | string)[] = [1, '2', 3];
let 객체: { data: number | string } = { data: '123' };
```

## any 타입

모든 타입의 값을 허용하고 싶다면 `any` 타입을 사용할 수 있다. 하지만 이는 타입 검사를 무력화시키므로, 타입스크립트를 사용하는 의미가 줄어든다.

```tsx
let 이름: any = 'kim';
이름 = 123;
이름 = undefined;
이름 = [];
```

## unknown 타입

`unknown` 타입은 `any`와 유사하지만, 타입 안전성을 조금 더 보장한다. 모든 타입의 값을 할당할 수 있지만, 해당 값을 사용할 때는 타입 검사가 필요하다.

```tsx
let 이름: unknown = 'kim';
이름 = 123;
이름 = undefined;
이름 = [];
```

다른 변수에 `unknown` 타입의 값을 할당하거나 연산을 수행하려고 하면 에러가 발생한다.

```tsx
let 변수1: string = 이름; // 에러 발생
이름 - 1; // 에러 발생
이름.data; // 에러 발생
```

`unknown` 타입은 아직 어떤 타입의 값이 들어올지 모를 때 유용하게 사용할 수 있다.