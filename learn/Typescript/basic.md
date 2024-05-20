# 기본적인 사용법

## **기본 타입 지정**

```ts
// String type
const userName: string = 'kim';
let country: string = 'korea';

// Number type
const userAge: number = 39;
let temperature: number = 25.5;

// Boolean type
const isActive: boolean = true;
let hasLicense: boolean = false;

// BigInt type
const largeNumber: bigint = 9007199254740991n;
let amount: bigint = BigInt(1000);

// Null type
let responseStatus: null = null;

// Undefined type
let userLocation: string | undefined = undefined;
```

- 변수 선언 시 **`변수명: 타입명`** 형태로 타입을 지정할 수 있다.
- 사용할 수 있는 타입에는 **`string`**, **`number`**, **`boolean`**, **`bigint`**, **`null`**, **`undefined`**, **`[]`**, **`{}`** 등이 있다.

### **타입 에러 방지**

```ts
let userName: string = 'kim';
userName = 123; // 에러 발생, number 는 안 됨
let temperature: number = 31.2;
temperature = 'hot hot'; // 에러 발생, string 은 안 됨
```

- 지정된 타입과 다른 값을 할당하려고 하면 타입스크립트는 에러 메시지를 띄워 타입 관련 버그를 사전에 방지한다.

### **배열 및 객체의 타입 지정**

```ts
let userNames: string[] = ['kim', 'park', 'choi'];
let userAge: { age: number } = { age: 22 };

// 객체 타입 예시
let user: { name: string, age: number, isActive: boolean } = {
  name: 'kim',
  age: 22,
  isActive: true,
};
```

- 배열이나 객체도 타입 지정이 가능하다

### **다중 타입 지정**

```ts
let flexibleType: string | number = 'hello';
let flexibleType: string | number = 100;
```

- 변수에 여러 타입의 데이터가 들어올 수 있는 경우 **`|`** 기호를 이용하여 다중 타입을 지정할 수 있다. (or 조건처럼)

### **타입 별칭**

```ts
type NameType = string | number;
let contactDetail: NameType = 'kim';
contactDetail = 123;
```

- **`type`** 키워드를 사용하여 복잡한 타입을 간단한 이름으로 참조할 수 있다.
- 커스텀 가능하다.

### **리터럴 타입**

```ts
type SpecificName = 'kim' | 'park';
let name: SpecificName = 'kim';

type Gender = 'm' | 'w';
const gender: Gender = 'm'
```

- 리터럴 타입을 이용하여 특정 값을 타입으로 제한할 수 있다.

### **함수의 타입 지정**

```ts
function doubleValue(x: number): number {
  return x * 2;
}
```

- 함수의 매개변수와 반환값에 타입을 지정할 수 있다.
- **`void`** 타입은 반환값이 없을 경우 사용

### **조건부 연산 검사**

```ts
function doubleValue(x: number | string) {
  if (typeof x === 'number'){
    return x * 2;
  }
}
```

- 타입스크립트는 변수의 타입이 확실하지 않으면 연산을 수행할 수 없다.
- **`typeof`** 연산자를 사용하여 타입 검사를 수행해야 한다.
- 항상 타입이 무엇인지 알려주는 것을 `narrowing` 라고 한다.

### **튜플 타입**

```ts
type UserTuple = [number, string, boolean];
let userDetails: UserTuple = [1, 'park', true];
```

- 배열 내의 타입 순서를 정확히 지정하면 튜플 타입을 사용할 수 있다.

### **복잡한 객체 타입**

```ts
type UserDetails = {
  name?: string,
  age: number
};
let user: UserDetails = { 
  name: 'park',
  age: 50
};

type User = {
  name: string;
  age: number;
  isActive: boolean;
};
let users: User[] = [
  { name: 'Alice', age: 25, isActive: true },
  { name: 'Bob', age: 30, isActive: false }
];
```

- 객체 타입이 복잡할 경우 **`type`** 키워드를 사용하여 정의할 수 있으며, 선택적 속성은 **`?`**를 사용하여 표시한다.

### **인덱스 시그니처**

```ts
type FlexibleObject = {
  [key: string]: number,
};
let userStats: FlexibleObject = { 
  age: 50,
  weight: 100,
};
```

- 객체의 속성을 미리 정의할 수 없는 경우 인덱스 시그니처를 사용하여 타입을 지정할 수 있다.

### **클래스의 타입 설정**

```ts
class Person {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}
```

- 클래스 내부에서도 타입을 설정할 수 있다.
- 생성자에서 사용되는 속성은 클래스 내에서 미리 선언해야 한다.
