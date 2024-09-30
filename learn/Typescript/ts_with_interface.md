# interface 키워드

앞에서 `type` 키워드를 이용해 타입을 변수처럼 저장해서 사용하는 것을 해봤다. 하지만 더 좋은 방법이 있다.

## Object에 사용할 수 있는 interface 문법

`interface` 문법을 사용하면 객체 자료형의 타입을 보다 편리하게 지정할 수 있다.

예를 들어 `{ color: 'red', width: 100 }` 같은 객체를 만들고 싶은데, 타입을 미리 정의하고 싶다면 `interface` 키워드를 이렇게 사용하면 된다.

```tsx
interface Square {
  color: string;
  width: number;
}

let 네모: Square = { color: 'red', width: 100 };
```

`interface`는 객체와 비슷한 모습으로 작성하면 된다. `type alias`와 용도와 기능이 거의 같다.

1. 대문자로 작명하고
2. `{ }` 안에 타입을 명시한다.

이렇게 만들어두면 앞으로 객체를 만들 때 `interface`를 타입으로 지정하면 간편하게 타입 지정을 할 수 있다.

(참고) 한 줄 끝나면 콤마 대신 세미콜론도 사용 가능하다.

### interface의 장점: extends 가능

`Student` 인터페이스와 `Teacher` 인터페이스가 필요하다고 가정해보자.

- `Student`는 `name` 속성이 들어가야 하고,
- `Teacher`는 `name` 속성과 `age` 속성이 들어가야 한다.

이를 어떻게 만들면 좋을까? 다음과 같이 만들어보자.

```tsx
interface Student {
  name: string;
}

interface Teacher extends Student {
  age: number;
}
```

`Teacher` 인터페이스가 `Student`를 `extends`하면 `Student` 안에 있던 속성을 복사해서 `Teacher`에 넣어준다. 이제 `Teacher` 타입은 `name`과 `age` 속성을 가진다.

## type 키워드와의 차이점

`type alias`와 `interface`는 거의 동일한 기능을 제공한다. 차이점은 `extends` 문법이 약간 다르다는 것이다.

- `interface`의 경우:

```tsx
interface Animal {
  name: string;
}

interface Cat extends Animal {
  legs: number;
}
```

- `type alias`의 경우:

```tsx
type Animal = {
  name: string;
};

type Cat = Animal & { legs: number };
```

`type alias`는 `extends`가 안 되지만 `&` 기호를 사용하면 객체 두 개를 합칠 수 있다. 이렇게 하면 `Cat` 타입은 `name`과 `legs` 속성을 가진다.

사실 `interface`도 `type`처럼 `&` 기호를 이용해도 복사가 가능하다.

```tsx
interface Student {
  name: string;
}

interface Teacher {
  age: number;
}

let 변수: Student & Teacher = { name: 'kim', age: 90 };
```

`&` 기호를 사용하는 것을 **intersection**이라고 부르는데, `extends`와 유사하게 사용할 수 있다.

(주의) `extends`를 쓸 때 타입끼리 중복 속성이 발견될 경우 에러가 나지만, `&`를 쓰면 상황에 따라 에러가 나지 않을 수도 있다.

### 타입 이름 중복 선언 시

```tsx
interface Animal {
  name: string;
}

interface Animal {
  legs: number;
}
```

`interface`의 경우 타입 이름 중복 선언을 허용하며, 중복 시 `extends`한 것과 동일하게 동작한다. 이러면 `Animal` 타입은 `name`과 `legs` 속성을 가진다.

(장점) 타입 선언을 자주 사용하는 외부 라이브러리 이용 시 타입 선언을 내가 덮어쓰기(override)하기 편리하다.

```tsx
type Animal = {
  name: string;
};

type Animal = {
  legs: number;
};
```

`type`의 경우 중복 선언을 허용하지 않는다. 에러가 난다.

(장점) 엄격하고 진지하다.

그래서 일반적인 상황에서는 `type` 키워드를 자주 활용하면 되는데, 다른 사람이 내 코드를 이용하는 상황이 많으면 `interface`로 유연하게 만드는 것이 좋다.

따라서 타입스크립트로 작성된 라이브러리들은 `interface`로 타입을 정해놓은 곳이 많다. 또는 객체 자료형은 전부 `interface`로 만들고, 다른 자료형은 `type` 키워드로 만들고, 이런 것도 괜찮다. `type`과 `interface` 문법을 잘 알고 있으면 기준은 정하기 나름이다.

### extends 할 때 객체 안의 속성이 중복될 경우

```tsx
interface Animal {
  name: string;
}

interface Dog extends Animal {
  name: number; // 에러 발생
}
```

`Animal`을 복사해서 `Dog` 인터페이스를 만들어봤다. 그런데 `name` 속성이 중복되는데 타입이 다르다. 이러면 에러가 난다.

```tsx
interface Animal {
  name: string;
}

interface Dog {
  name: number;
}

let 변수: Dog & Animal = { name: '멍멍' }; // 에러 발생
```

`&` 연산자로 `Dog`, `Animal`을 합쳐봤다. 그런데 `name` 속성이 중복되고 타입이 다르다. 이러면 에러가 난다. `interface`뿐만 아니라 `type` 키워드도 똑같은 현상이 일어난다.

(주의) 그런데 `name: string`, `name: string`이라면 에러가 나지 않는다. 하나로 합쳐준다.

---

## 예제

### (예제1) interface 이용해서 간단하게 타입을 만들어보자

```tsx
let 상품 = { brand: 'Samsung', serialNumber: 1360, model: ['TV', 'phone'] };
```

이런 변수가 있는데 `interface` 키워드로 타입 지정 이쁘게 하고 싶다. 어떻게 코드를 짜면 될까? 무슨 타입일지는 알아서 기입하자.

**정답**

```tsx
interface Product {
  brand: string;
  serialNumber: number;
  model: string[];
}

let 상품: Product = { brand: 'Samsung', serialNumber: 1360, model: ['TV', 'phone'] };
```

### (예제2) array 안에 object 여러 개가 필요하다

쇼핑몰 장바구니를 구현하려고 하는데

```tsx
let 장바구니 = [
  { product: '청소기', price: 7000 },
  { product: '삼다수', price: 800 },
];
```

이렇게 생긴 객체들이 잔뜩 들어갈 수 있는 배열은 어떻게 타입을 지정해야 할까? 오늘 배운 `interface` 문법을 써보자.

**정답**

```tsx
interface Product {
  product: string;
  price: number;
}

let 장바구니: Product[] = [
  { product: '청소기', price: 7000 },
  { product: '삼다수', price: 800 },
];
```

### (예제3) 다음 내용의 타입을 extends 해보자

갑자기 서비스가 업데이트되어서 일부 상품은 `card` 속성이 들어가야 한다.

```tsx
{ product: '청소기', price: 7000, card: false }
```

위에서 만든 `interface`를 `extends` 해서 이 객체의 타입을 만들어보자.

**정답**

```tsx
interface Product {
  product: string;
  price: number;
}

interface NewProduct extends Product {
  card: boolean;
}

let 상품: NewProduct = { product: '청소기', price: 7000, card: false };
```

### (예제4) object 안에 함수를 2개 넣고 싶다

1. 이 객체 자료는 `plus()` 함수를 내부에 가지고 있으며, `plus` 함수는 파라미터 2개를 입력하면 더해서 `return`해준다.
2. 이 객체 자료는 `minus()` 함수를 내부에 가지고 있으며, `minus` 함수는 파라미터 2개를 입력하면 빼서 `return`해준다.

이 객체 자료를 어떻게 만들면 될까? `interface`를 이용해서 객체에 타입 지정도 해보자.

**정답**

```tsx
interface Calculator {
  plus: (a: number, b: number) => number;
  minus: (a: number, b: number) => number;
}

let 계산기: Calculator = {
  plus(a, b) {
    return a + b;
  },
  minus(a, b) {
    return a - b;
  },
};
```

---

### 추가 설명

`interface`와 `type`은 객체 타입을 정의할 때 자주 사용된다. `interface`는 확장이 용이하고, 타입 이름 중복 선언이 가능하다는 장점이 있다. 반면 `type`은 더 엄격하고 다양한 타입을 정의할 수 있다.

- `interface`는 주로 객체 타입 정의에 사용되고, `extends`를 통해 타입을 확장할 수 있다.
- `type`은 다양한 타입(원시 타입, 유니온 타입, 튜플 등)을 정의할 수 있다.
- 상황에 따라 적절한 것을 선택해서 사용하면 된다.

또한, 타입스크립트로 작성된 라이브러리에서는 `interface`를 많이 사용하는데, 이는 타입을 확장하거나 덮어쓰기가 용이하기 때문이다.