## Class 타입 지정

### 필드값 타입 지정

클래스 내부에는 모든 인스턴스에서 사용할 수 있는 속성을 정의할 수 있다. 예를 들어, 모든 `Person` 클래스의 인스턴스에 `data`라는 속성을 부여하려면 다음과 같이 작성한다.

```tsx
typescript
코드 복사
class Person {
  data = 0;
}

const john = new Person();
const jane = new Person();

console.log(john.data); // 출력: 0
console.log(jane.data); // 출력: 0

```

클래스의 중괄호 안에 변수처럼 필드를 선언하면 된다. `var`, `let` 키워드를 사용하지 않는다. 이 방법으로 클래스의 모든 인스턴스에 `data` 속성이 자동으로 복사된다. 필드라고 부르는 이러한 속성은 인스턴스가 객체이기 때문에 점(`.`)을 사용하여 접근할 수 있다.

타입스크립트는 필드의 초기값을 기반으로 자동으로 타입을 추론한다. 예를 들어, `data` 필드의 초기값이 `0`이므로 `data`는 `number` 타입으로 간주된다. 그러나 명시적으로 타입을 지정할 수도 있다.

```tsx
typescript
코드 복사
class Person {
  data: number = 0;
}

const john = new Person();
john.data = '1'; // 에러 발생: Type 'string' is not assignable to type 'number'.

```

타입을 명시적으로 지정하면 해당 필드에 잘못된 타입의 값을 할당할 경우 컴파일 에러가 발생한다.

### Constructor 타입 지정

클래스는 객체를 생성하는 복사기 역할을 한다. 예를 들어, `{ name: 'Alice', age: 30 }`와 같은 객체를 생성하는 클래스를 만들려면 `constructor` 함수를 사용한다. ES6 문법에서는 `constructor` 함수를 통해 초기화를 진행한다.

```tsx
typescript
코드 복사
class Person {
  name: string;
  age: number;

  constructor(name: string) {
    this.name = name;
    this.age = 20;
  }
}

const alice = new Person('Alice');
console.log(alice); // 출력: { name: 'Alice', age: 20 }

```

타입스크립트에서는 `constructor` 함수의 파라미터에도 타입을 지정해야 한다. 위 예제에서는 `name` 파라미터를 `string` 타입으로 지정하였다. 필드와 파라미터의 타입을 일치시킴으로써 타입 안전성을 확보할 수 있다.

또한, 기본 파라미터 값을 지정할 수 있다. 파라미터에 값을 입력하지 않으면 기본값이 할당된다.

```tsx
typescript
코드 복사
class Person {
  name: string;
  age: number;

  constructor(name: string = 'Unknown') {
    this.name = name;
    this.age = 20;
  }
}

const bob = new Person();
console.log(bob); // 출력: { name: 'Unknown', age: 20 }

```

`constructor` 함수는 반환 타입을 지정할 필요가 없다. 항상 객체를 반환하기 때문이다.

### 클래스와 `constructor`의 차이점

클래스 내의 필드 선언과 `constructor` 함수는 유사한 역할을 하지만, `constructor`를 통해 인스턴스 생성 시 초기값을 동적으로 설정할 수 있다. `new Person('Alice')`와 같이 인스턴스를 생성할 때 파라미터를 전달하여 각 인스턴스마다 다른 값을 설정할 수 있다.

### 메서드 타입 지정

클래스 내부에는 함수를 메서드로 정의할 수 있다. 메서드도 함수와 마찬가지로 파라미터와 반환 타입을 지정할 수 있다.

```tsx
typescript
코드 복사
class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  incrementAge(): number {
    this.age += 1;
    return this.age;
  }
}

const carol = new Person('Carol', 25);
console.log(carol.incrementAge()); // 출력: 26

```

위 예제에서 `incrementAge` 메서드는 반환 타입을 `number`로 지정하였다. 이 메서드는 `age` 필드를 증가시키고, 증가된 값을 반환한다.

### 과제

### 과제 1: `Car` 클래스 생성

다음 요구사항을 충족하는 `Car` 클래스를 작성하라.

1. `{ model: 'Sonata', price: 3000 }`와 같은 객체를 생성하는 클래스.
2. 각 인스턴스는 `.tax()` 메서드를 사용할 수 있으며, `price`의 10%를 반환한다.
3. `model`과 `price` 속성의 타입을 명확히 지정하고, `.tax()` 메서드의 반환 타입도 지정한다.

**예제 구현:**

```tsx
typescript
코드 복사
class Car {
  model: string;
  price: number;

  constructor(model: string, price: number) {
    this.model = model;
    this.price = price;
  }

  tax(): number {
    return this.price * 0.1;
  }
}

const car1 = new Car('Sonata', 3000);
console.log(car1);        // 출력: Car { model: 'Sonata', price: 3000 }
console.log(car1.tax());  // 출력: 300

```

### 과제 2: `Word` 클래스 생성

다음 요구사항을 충족하는 `Word` 클래스를 작성하라.

1. `new Word()`를 호출할 때 숫자 또는 문자를 임의의 개수만큼 입력할 수 있다.
2. 숫자는 `num` 속성에, 문자는 `str` 속성에 각각 배열 형태로 저장된다.
3. `num`과 `str` 속성의 타입을 명확히 지정한다.

**동작 예시:**

```tsx
typescript
코드 복사
const obj = new Word('kim', 3, 5, 'park');
console.log(obj.num); // 출력: [3, 5]
console.log(obj.str); // 출력: ['kim', 'park']

```

**예제 구현:**

```tsx
typescript
코드 복사
class Word {
  num: number[];
  str: string[];

  constructor(...args: (number | string)[]) {
    this.num = [];
    this.str = [];

    args.forEach(element => {
      if (typeof element === 'number') {
        this.num.push(element);
      } else if (typeof element === 'string') {
        this.str.push(element);
      }
    });
  }
}

const obj = new Word('kim', 3, 5, 'park');
console.log(obj.num); // 출력: [3, 5]
console.log(obj.str); // 출력: ['kim', 'park']

```

**설명:**

1. `Word` 클래스는 `num`과 `str`이라는 두 개의 배열 필드를 가진다.
2. `constructor`는 나머지 파라미터(`...args`)를 받아, 각 요소의 타입을 검사하여 해당 배열에 추가한다.
3. 숫자는 `num` 배열에, 문자는 `str` 배열에 저장된다.
4. 타입 지정 덕분에 잘못된 타입의 값이 할당될 경우 컴파일 에러가 발생한다.

### 결론

타입스크립트에서 클래스의 필드, `constructor`, 메서드에 타입을 지정함으로써 코드의 안정성과 가독성을 높일 수 있다. 클래스 필드의 타입을 명시적으로 지정하면, 인스턴스 생성 시 잘못된 타입의 값이 할당되는 것을 방지할 수 있다. 또한, 메서드의 파라미터와 반환 타입을 지정함으로써 함수의 사용을 명확하게 할 수 있다.

타입스크립트의 자동 타입 추론 기능을 활용하면, 대부분의 경우 타입을 명시적으로 지정하지 않아도 되지만, 복잡한 클래스 구조에서는 명시적인 타입 지정이 권장된다. 이를 통해 코드의 오류를 사전에 방지하고, 유지보수성을 향상시킬 수 있다.