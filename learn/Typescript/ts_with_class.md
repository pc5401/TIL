# Class 타입 지정

## 필드값 타입 지정

클래스 내부에는 모든 인스턴스에서 사용할 수 있는 속성을 정의할 수 있다. 예를 들어, 모든 `Person` 클래스의 인스턴스에 `data`라는 속성을 부여하려면 다음과 같이 작성한다.

```tsx
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
class Person {
  data: number = 0;
}

const john = new Person();
john.data = '1'; // 에러 발생: Type 'string' is not assignable to type 'number'.

```

타입을 명시적으로 지정하면 해당 필드에 잘못된 타입의 값을 할당할 경우 컴파일 에러가 발생한다.

## Constructor 타입 지정

클래스는 객체를 생성하는 복사기 역할을 한다. 예를 들어, `{ name: 'Alice', age: 30 }`와 같은 객체를 생성하는 클래스를 만들려면 `constructor` 함수를 사용한다. ES6 문법에서는 `constructor` 함수를 통해 초기화를 진행한다.

```tsx
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

## 클래스와 `constructor`의 차이점

클래스 내의 필드 선언과 `constructor` 함수는 유사한 역할을 하지만, `constructor`를 통해 인스턴스 생성 시 초기값을 동적으로 설정할 수 있다. `new Person('Alice')`와 같이 인스턴스를 생성할 때 파라미터를 전달하여 각 인스턴스마다 다른 값을 설정할 수 있다.

### 메서드 타입 지정

클래스 내부에는 함수를 메서드로 정의할 수 있다. 메서드도 함수와 마찬가지로 파라미터와 반환 타입을 지정할 수 있다.

```tsx
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
const obj = new Word('kim', 3, 5, 'park');
console.log(obj.num); // 출력: [3, 5]
console.log(obj.str); // 출력: ['kim', 'park']

```

**예제 구현:**

```tsx
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

## 접근 제어 키워드

> `public`, `private`, `protected`, `static`
> 

### `public`과 `private` 키워드를 사용한 접근 제어

TypeScript를 사용하면 JavaScript에는 없는 접근 제어 키워드인 `public`, `private`, `protected`, `static` 등을 사용할 수 있다. 이들 키워드를 통해 클래스 내부의 속성과 메서드에 대한 접근 권한을 설정할 수 있다.

### `public` 키워드

`public` 키워드를 클래스 속성 앞에 붙이면, 해당 속성은 클래스 외부에서 자유롭게 접근하고 수정할 수 있다. 기본적으로 클래스 속성은 `public`으로 간주되므로, `public` 키워드를 명시적으로 붙이지 않아도 동일한 효과를 가진다.

```tsx
class User {
  public name: string;

  constructor() {
    this.name = 'Alice';
  }
}

const user1 = new User();
user1.name = 'Bob'; // 가능
console.log(user1.name); // 출력: Bob

```

**주의 사항**:

- `public` 키워드를 붙이든 붙이지 않든 클래스 속성은 동일하게 동작한다.
- 클래스의 프로토타입 함수에도 `public` 키워드를 사용할 수 있다.

### `private` 키워드

`private` 키워드를 클래스 속성 앞에 붙이면, 해당 속성은 클래스 내부에서만 접근하고 수정할 수 있으며, 클래스 외부나 상속받은 클래스에서도 접근할 수 없다.

```tsx
class User {
  public name: string;
  private familyName: string;

  constructor() {
    this.name = 'Alice';
    this.familyName = 'Smith';
    console.log(this.familyName + ' 안녕하세요'); // 내부 접근 가능
  }

  changeFamilyName(newName: string) {
    this.familyName = newName; // 내부에서 수정 가능
  }
}

const user1 = new User();
user1.name = 'Bob'; // 가능
user1.familyName = 'Johnson'; // 에러: Property 'familyName' is private and only accessible within class 'User'.
user1.changeFamilyName('Johnson'); // 가능

```

**`private` 키워드의 특징**:

- 클래스 외부에서 `private` 속성에 직접 접근하거나 수정할 수 없다.
- 클래스 내부에서만 `private` 속성을 사용할 수 있으며, 필요한 경우 이를 수정하기 위한 메서드를 제공할 수 있다.

**예제: `private` 속성 수정 메서드**

```tsx
class User {
  public name: string;
  private familyName: string;

  constructor(name: string, familyName: string) {
    this.name = name;
    this.familyName = familyName;
  }

  changeFamilyName(newName: string): void {
    this.familyName = newName;
  }

  getFullName(): string {
    return `${this.name} ${this.familyName}`;
  }
}

const user1 = new User('Alice', 'Smith');
console.log(user1.getFullName()); // 출력: Alice Smith
user1.changeFamilyName('Johnson');
console.log(user1.getFullName()); // 출력: Alice Johnson

```

### `protected` 키워드

`protected` 키워드는 `private`과 유사하지만, 상속받은 클래스에서는 접근이 가능하다. 이는 상속 관계에서만 접근을 허용하고, 클래스 외부에서는 접근을 제한하고자 할 때 유용하다.

```tsx
class User {
  public name: string;
  protected age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
}

class Admin extends User {
  constructor(name: string, age: number) {
    super(name, age);
  }

  getAge(): number {
    return this.age; // 가능
  }
}

const admin1 = new Admin('Charlie', 30);
console.log(admin1.name); // 출력: Charlie
console.log(admin1.age); // 에러: Property 'age' is protected and only accessible within class 'User' and its subclasses.
console.log(admin1.getAge()); // 출력: 30

```

### `static` 키워드

`static` 키워드를 클래스 속성이나 메서드 앞에 붙이면, 해당 속성이나 메서드는 클래스 자체에 속하게 된다. 즉, 클래스의 인스턴스가 아닌 클래스 자체에서 접근할 수 있다.

```tsx
class User {
  static skill: string = 'JavaScript';
  public name: string;

  constructor(name: string) {
    this.name = name;
  }

  static changeSkill(newSkill: string): void {
    User.skill = newSkill;
  }

  introduce(): string {
    return `${this.name}은 ${User.skill} 전문가입니다.`;
  }
}

const user1 = new User('Alice');
console.log(User.skill); // 출력: JavaScript
console.log(user1.introduce()); // 출력: Alice은 JavaScript 전문가입니다.

User.changeSkill('Python');
const user2 = new User('Bob');
console.log(User.skill); // 출력: Python
console.log(user2.introduce()); // 출력: Bob은 Python 전문가입니다.

```

**`static` 키워드의 특징**:

- 클래스 인스턴스가 아닌 클래스 자체에서 접근 가능하다.
- `private`, `protected`, `public`과 함께 사용할 수 있다.

```tsx
class User {
  private static count: number = 0;
  public name: string;

  constructor(name: string) {
    this.name = name;
    User.count++;
  }

  public static getCount(): number {
    return User.count;
  }
}

const user1 = new User('Alice');
const user2 = new User('Bob');
console.log(User.getCount()); // 출력: 2
console.log(User.count); // 에러: Property 'count' is private and only accessible within class 'User'.

```

### `public`과 `private`의 결합 예제

```tsx
class User {
  public name: string;
  private familyName: string;

  constructor(name: string, familyName: string) {
    this.name = name;
    this.familyName = familyName;
  }

  public getFullName(): string {
    return `${this.name} ${this.familyName}`;
  }

  public setFamilyName(newFamilyName: string): void {
    this.familyName = newFamilyName;
  }
}

const user1 = new User('Alice', 'Smith');
console.log(user1.name); // 출력: Alice
console.log(user1.getFullName()); // 출력: Alice Smith
user1.setFamilyName('Johnson');
console.log(user1.getFullName()); // 출력: Alice Johnson
user1.familyName = 'Williams'; // 에러: Property 'familyName' is private and only accessible within class 'User'.

```

### `protected`와 `static`의 결합 예제

```tsx
class User {
  public name: string;
  protected age: number;
  private static count: number = 0;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
    User.count++;
  }

  public static getUserCount(): number {
    return User.count;
  }
}

class Admin extends User {
  constructor(name: string, age: number) {
    super(name, age);
  }

  public getAge(): number {
    return this.age; // 가능
  }
}

const admin1 = new Admin('Charlie', 30);
console.log(Admin.getUserCount()); // 출력: 1
console.log(admin1.getAge()); // 출력: 30
console.log(admin1.age); // 에러: Property 'age' is protected and only accessible within class 'User' and its subclasses.

```

### 결론

TypeScript의 `public`, `private`, `protected`, `static` 키워드를 활용하면 클래스의 속성과 메서드에 대한 접근 권한을 세밀하게 제어할 수 있다. 이를 통해 코드의 캡슐화(encapsulation)를 강화하고, 의도하지 않은 외부 접근으로 인한 버그를 예방할 수 있다.

- **`public`**: 모든 곳에서 접근 가능.
- **`private`**: 클래스 내부에서만 접근 가능.
- **`protected`**: 클래스 내부 및 상속받은 클래스에서 접근 가능.
- **`static`**: 클래스 자체에서 접근 가능하며, 인스턴스에서는 접근 불가.

이러한 접근 제어를 적절히 활용하여 보다 견고하고 유지보수하기 쉬운 객체 지향 코드를 작성할 수 있다.

### 추가 참고 사항

- TypeScript 클래스 공식 문서를 참고하여 클래스 관련 다양한 기능과 타입 지정 방법을 학습할 수 있다.
- 클래스 상속, 인터페이스 구현 등 고급 클래스 기능을 활용하여 더욱 견고한 객체 지향 코드를 작성할 수 있다.

### 과제 <- 접근 제어자 적용

### 과제 1: `Car` 클래스 생성

다음 요구사항을 충족하는 `Car` 클래스를 작성하라.

1. `{ model: 'Sonata', price: 3000 }`와 같은 객체를 생성하는 클래스.
2. 각 인스턴스는 `.tax()` 메서드를 사용할 수 있으며, `price`의 10%를 반환한다.
3. `model`과 `price` 속성의 타입을 명확히 지정하고, `.tax()` 메서드의 반환 타입도 지정한다.

**예제 구현:**

```tsx
class Car {
  public model: string;
  public price: number;

  constructor(model: string, price: number) {
    this.model = model;
    this.price = price;
  }

  public tax(): number {
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
const obj = new Word('kim', 3, 5, 'park');
console.log(obj.num); // 출력: [3, 5]
console.log(obj.str); // 출력: ['kim', 'park']

```

**예제 구현:**

```tsx
class Word {
  public num: number[];
  public str: string[];

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

### 요약

TypeScript의 접근 제어 키워드인 `public`, `private`, `protected`, `static`을 활용하면 클래스의 속성과 메서드에 대한 접근 권한을 세밀하게 조절할 수 있다. 이를 통해 코드의 캡슐화를 강화하고, 의도하지 않은 외부 접근으로 인한 오류를 방지할 수 있다. 클래스와 관련된 이러한 기능들을 적절히 사용하여 보다 안전하고 유지보수하기 쉬운 객체 지향 코드를 작성할 수 있다.