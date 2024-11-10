# 객체지향 프로그래밍 (OOP) in TypeScript

## 개요

객체지향 프로그래밍(Object-Oriented Programming, OOP)은 데이터를 객체로 취급하여 프로그래밍하는 방법이다. 객체는 데이터와 해당 데이터를 처리하는 메서드를 포함한다. OOP의 주요 개념으로는 클래스(Class), 객체(Object), 상속(Inheritance), 다형성(Polymorphism), 캡슐화(Encapsulation), 추상화(Abstraction) 등이 있다. TypeScript는 이러한 객체지향 개념을 효과적으로 지원하여 코드의 재사용성과 유지보수성을 높이는 데 유용하다.

## 객체지향 프로그래밍의 주요 개념

1. **클래스(Class)와 객체(Object)**
2. **상속(Inheritance)**
3. **캡슐화(Encapsulation)**
4. **다형성(Polymorphism)**
5. **추상화(Abstraction)**

### 1. 클래스(Class)와 객체(Object)

### 클래스(Class)

클래스는 객체를 생성하기 위한 청사진 또는 템플릿이다. 클래스는 속성(Attribute)과 메서드(Method)를 포함할 수 있다.

**예제:**

```tsx
class Dog {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name; // 속성
        this.age = age;   // 속성
    }

    bark(): void {
        console.log(`${this.name}이(가) 멍멍 짖습니다.`);
    }
}
```

### 객체(Object)

객체는 클래스의 인스턴스(instance)로, 클래스에 정의된 구조를 따른 실제 실체이다.

**예제:**

```tsx
const myDog = new Dog("바둑이", 3);
const yourDog = new Dog("초코", 5);

myDog.bark();    // 출력: 바둑이가(가) 멍멍 짖습니다.
yourDog.bark();  // 출력: 초코가(가) 멍멍 짖습니다.

console.log(`${myDog.name}의 나이는 ${myDog.age}살입니다.`);  // 출력: 바둑이의 나이는 3살
```

### 2. 상속(Inheritance)

상속은 기존 클래스(부모 클래스)를 기반으로 새로운 클래스(자식 클래스)를 만드는 개념이다. 자식 클래스는 부모 클래스의 속성과 메서드를 물려받아 사용할 수 있으며, 필요에 따라 추가적인 속성이나 메서드를 정의할 수 있다.

**예제:**

```tsx
// 부모 클래스
class Animal {
    name: string;

    constructor(name: string) {
        this.name = name;
    }

    speak(): void {
        // 자식 클래스에서 구현
    }
}

// 자식 클래스
class Cat extends Animal {
    speak(): void {
        console.log(`${this.name}이(가) 야옹 소리를 냅니다.`);
    }
}

class Dog extends Animal {
    speak(): void {
        console.log(`${this.name}이(가) 멍멍 소리를 냅니다.`);
    }
}

// 객체 생성
const kitty = new Cat("나비");
const doggy = new Dog("바둑이");

kitty.speak();  // 출력: 나비가(가) 야옹 소리를 냅니다.
doggy.speak();  // 출력: 바둑이가(가) 멍멍 소리를 냅니다.
```

### 3. 캡슐화(Encapsulation)

캡슐화는 객체의 내부 상태(속성)를 외부에서 직접 접근하지 못하도록 보호하고, 메서드를 통해서만 접근하도록 하는 개념이다. 이를 통해 데이터의 무결성을 유지할 수 있다.

**예제:**

```tsx
class BankAccount {
    owner: string;
    private balance: number; // private으로 비공개 속성 선언

    constructor(owner: string, balance: number = 0) {
        this.owner = owner;
        this.balance = balance;
    }

    // 잔액 확인 메서드
    getBalance(): number {
        return this.balance;
    }

    // 입금 메서드
    deposit(amount: number): void {
        if (amount > 0) {
            this.balance += amount;
            console.log(`${amount}원이 입금되었습니다.`);
        } else {
            console.log("유효한 금액을 입력하세요.");
        }
    }

    // 출금 메서드
    withdraw(amount: number): void {
        if (0 < amount && amount <= this.balance) {
            this.balance -= amount;
            console.log(`${amount}원이 출금되었습니다.`);
        } else {
            console.log("잔액이 부족하거나 유효하지 않은 금액입니다.");
        }
    }
}

// 객체 생성
const account = new BankAccount("홍길동", 1000);

// 메서드를 통한 접근
account.deposit(500);          // 출력: 500원이 입금되었습니다.
account.withdraw(200);         // 출력: 200원이 출금되었습니다.
console.log(account.getBalance()); // 출력: 1300

// 직접 접근 시도 (실패)
// console.log(account.balance);  // Error: Property 'balance' is private and only accessible within class 'BankAccount'.
```

### 4. 다형성(Polymorphism)

다형성은 같은 이름의 메서드가 다양한 형태로 동작할 수 있는 능력이다. 주로 상속과 함께 사용되며, 부모 클래스의 메서드를 자식 클래스에서 재정의(오버라이딩)하여 구현한다.

**예제:**

```tsx
class Animal {
    speak(): void {
        // 기본 구현 없음
    }
}

class Cat extends Animal {
    speak(): void {
        console.log("야옹!");
    }
}

class Dog extends Animal {
    speak(): void {
        console.log("멍멍!");
    }
}

class Cow extends Animal {
    speak(): void {
        console.log("음메!");
    }
}

// 여러 객체를 배열에 저장
const animals: Animal[] = [new Cat(), new Dog(), new Cow()];

for (const animal of animals) {
    animal.speak();
    // 출력:
    // 야옹!
    // 멍멍!
    // 음메!
}
```

### 5. 추상화(Abstraction)

추상화는 복잡한 시스템을 단순화하여 중요한 부분만을 모델링하는 개념이다. TypeScript에서는 `abstract` 키워드를 사용하여 추상 클래스를 정의할 수 있다.

**예제:**

```tsx
abstract class Shape {
    abstract area(): number;
}

class Rectangle extends Shape {
    width: number;
    height: number;

    constructor(width: number, height: number) {
        super();
        this.width = width;
        this.height = height;
    }

    area(): number {
        return this.width * this.height;
    }
}

class Circle extends Shape {
    radius: number;

    constructor(radius: number) {
        super();
        this.radius = radius;
    }

    area(): number {
        return Math.PI * this.radius ** 2;
    }
}

// 객체 생성 및 사용
const rect = new Rectangle(3, 4);
const circle = new Circle(5);

console.log(`Rectangle area: ${rect.area()}`);  // 출력: Rectangle area: 12
console.log(`Circle area: ${circle.area()}`);    // 출력: Circle area: 78.5398163397448
```

## 추가 보완 내용

### 클래스 변수와 인스턴스 변수

TypeScript에서는 `static` 키워드를 사용하여 클래스 변수(정적 변수)를 정의할 수 있다. 클래스 변수는 클래스 전체에서 공유되며, 인스턴스 변수는 각 객체마다 별도로 존재한다.

**예제:**

```tsx
class Dog {
    static species: string = "Canis familiaris"; // 클래스 변수

    name: string;    // 인스턴스 변수
    age: number;     // 인스턴스 변수

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
}

// 객체 생성
const dog1 = new Dog("바둑이", 3);
const dog2 = new Dog("초코", 5);

console.log(Dog.species);   // 출력: Canis familiaris
console.log(Dog.species);   // 출력: Canis familiaris

// 클래스 변수를 변경하면 모든 객체에 반영됨
Dog.species = "Canis lupus familiaris";
console.log(Dog.species);   // 출력: Canis lupus familiaris
console.log(Dog.species);   // 출력: Canis lupus familiaris
```

### 메서드의 종류

1. **인스턴스 메서드**: 객체의 상태를 변경하거나 객체의 속성에 접근하는 메서드이다. 첫 번째 매개변수로 `this`를 사용한다.
2. **클래스 메서드**: 클래스 자체에 작용하는 메서드로, `static` 키워드를 사용하여 정의한다.
3. **정적 메서드**: 클래스나 객체 상태와 무관하게 동작하는 메서드로, `static` 키워드를 사용하여 정의한다.

**예제:**

```tsx
class Dog {
    static species: string = "Canis familiaris";

    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }

    // 인스턴스 메서드
    bark(): void {
        console.log(`${this.name}이(가) 멍멍 짖습니다.`);
    }

    // 클래스 메서드
    static getSpecies(): string {
        return Dog.species;
    }

    // 정적 메서드
    static isDomestic(): boolean {
        return true;
    }
}

// 사용 예
const dog = new Dog("바둑이", 3);
dog.bark();                   // 출력: 바둑이가(가) 멍멍 짖습니다.

console.log(Dog.getSpecies());    // 출력: Canis familiaris
console.log(Dog.isDomestic());    // 출력: true
console.log(dog.getSpecies());    // Error: Property 'getSpecies' does not exist on type 'Dog'.
console.log(dog.isDomestic());    // Error: Property 'isDomestic' does not exist on type 'Dog'.
```

**참고:** TypeScript에서는 정적 메서드는 클래스 자체에서만 호출 가능하며, 인스턴스에서는 호출할 수 없다.

### 연산자 오버로딩

TypeScript는 JavaScript를 기반으로 하기 때문에 직접적인 연산자 오버로딩을 지원하지 않는다. 그러나 메서드를 통해 유사한 기능을 구현할 수 있다.

**예제:**

```tsx
class Vector {
    x: number;
    y: number;

    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
    }

    // 문자열 표현
    toString(): string {
        return `Vector(${this.x}, ${this.y})`;
    }

    // 벡터 덧셈 메서드
    add(other: Vector): Vector {
        return new Vector(this.x + other.x, this.y + other.y);
    }
}

// 객체 생성
const v1 = new Vector(2, 3);
const v2 = new Vector(4, 5);

// 덧셈 연산
const v3 = v1.add(v2);
console.log(v3.toString());  // 출력: Vector(6, 8
```

### 예외 처리와 OOP

객체지향 프로그래밍에서는 사용자 정의 예외를 만들어 특정 상황에서 예외를 처리할 수 있다.

**예제:**

```tsx
class InsufficientFundsError extends Error {
    constructor(message: string) {
        super(message);
        this.name = "InsufficientFundsError";
    }
}

class BankAccount {
    owner: string;
    private balance: number;

    constructor(owner: string, balance: number = 0) {
        this.owner = owner;
        this.balance = balance;
    }

    deposit(amount: number): void {
        if (amount > 0) {
            this.balance += amount;
            console.log(`${amount}원이 입금되었습니다.`);
        } else {
            console.log("유효한 금액을 입력하세요.");
        }
    }

    withdraw(amount: number): void {
        if (amount > this.balance) {
            throw new InsufficientFundsError("잔액이 부족합니다.");
        }
        this.balance -= amount;
        console.log(`${amount}원이 출금되었습니다.`);
    }

    getBalance(): number {
        return this.balance;
    }
}

// 사용 예
const account = new BankAccount("홍길동", 1000);
account.deposit(500);          // 출력: 500원이 입금되었습니다.

try {
    account.withdraw(2000);
} catch (e) {
    if (e instanceof InsufficientFundsError) {
        console.log(e.message);    // 출력: 잔액이 부족합니다.
    } else {
        console.log("알 수 없는 오류가 발생했습니다.");
    }
}

```