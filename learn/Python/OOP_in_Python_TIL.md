# 객체지향 프로그래밍 (OOP) in Python

## 개요

객체지향 프로그래밍(Object-Oriented Programming, OOP)은 데이터를 객체로 취급하여 프로그래밍하는 방법이다. 객체는 데이터와 해당 데이터를 처리하는 메서드를 포함한다. OOP의 주요 개념으로는 클래스(Class), 객체(Object), 상속(Inheritance), 다형성(Polymorphism), 캡슐화(Encapsulation), 추상화(Abstraction) 등이 있다. Python은 이러한 객체지향 개념을 효과적으로 지원하여 코드의 재사용성과 유지보수성을 높이는 데 유용하다.

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

```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # 속성
        self.age = age    # 속성

    def bark(self):
        print(f"{self.name}이(가) 멍멍 짖습니다.")
```

### 객체(Object)

객체는 클래스의 인스턴스(instance)로, 클래스에 정의된 구조를 따른 실제 실체이다.

**예제:**

```python
my_dog = Dog("바둑이", 3)
your_dog = Dog("초코", 5)

my_dog.bark()    # 출력: 바둑이가(가) 멍멍 짖습니다.
your_dog.bark()  # 출력: 초코가(가) 멍멍 짖습니다.

print(f"{my_dog.name}의 나이는 {my_dog.age}살입니다.")  # 출력: 바둑이의 나이는 3살입니다.
```

### 2. 상속(Inheritance)

상속은 기존 클래스(부모 클래스)를 기반으로 새로운 클래스(자식 클래스)를 만드는 개념이다. 자식 클래스는 부모 클래스의 속성과 메서드를 물려받아 사용할 수 있으며, 필요에 따라 추가적인 속성이나 메서드를 정의할 수 있다.

**예제:**

```python
# 부모 클래스
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # 자식 클래스에서 구현

# 자식 클래스
class Cat(Animal):
    def speak(self):
        print(f"{self.name}이(가) 야옹 소리를 냅니다.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}이(가) 멍멍 소리를 냅니다.")

# 객체 생성
kitty = Cat("나비")
doggy = Dog("바둑이")

kitty.speak()  # 출력: 나비가(가) 야옹 소리를 냅니다.
doggy.speak()  # 출력: 바둑이가(가) 멍멍 소리를 냅니다.
```

### 3. 캡슐화(Encapsulation)

캡슐화는 객체의 내부 상태(속성)를 외부에서 직접 접근하지 못하도록 보호하고, 메서드를 통해서만 접근하도록 하는 개념이다. 이를 통해 데이터의 무결성을 유지할 수 있다.

**예제:**

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # __로 시작하면 비공개 속성

    # 잔액 확인 메서드
    def get_balance(self):
        return self.__balance

    # 입금 메서드
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount}원이 입금되었습니다.")
        else:
            print("유효한 금액을 입력하세요.")

    # 출금 메서드
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount}원이 출금되었습니다.")
        else:
            print("잔액이 부족하거나 유효하지 않은 금액입니다.")

# 객체 생성
account = BankAccount("홍길동", 1000)

# 메서드를 통한 접근
account.deposit(500)         # 출력: 500원이 입금되었습니다.
account.withdraw(200)        # 출력: 200원이 출금되었습니다.
print(account.get_balance()) # 출력: 1300

# 직접 접근 시도 (실패)
# print(account.__balance)  # AttributeError 발생
```

### 4. 다형성(Polymorphism)

다형성은 같은 이름의 메서드가 다양한 형태로 동작할 수 있는 능력이다. 주로 상속과 함께 사용되며, 부모 클래스의 메서드를 자식 클래스에서 재정의(오버라이딩)하여 구현한다.

**예제:**

```python
class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("야옹!")

class Dog(Animal):
    def speak(self):
        print("멍멍!")

class Cow(Animal):
    def speak(self):
        print("음메!")

# 여러 객체를 리스트에 저장
animals = [Cat(), Dog(), Cow()]

for animal in animals:
    animal.speak()
    # 출력:
    # 야옹!
    # 멍멍!
    # 음메!
```

### 5. 추상화(Abstraction)

추상화는 복잡한 시스템을 단순화하여 중요한 부분만을 모델링하는 개념이다. Python에서는 `abc` 모듈을 사용하여 추상 클래스를 정의할 수 있다.

**예제:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

# 객체 생성 및 사용
rect = Rectangle(3, 4)
circle = Circle(5)

print(f"Rectangle area: {rect.area()}")  # 출력: Rectangle area: 12
print(f"Circle area: {circle.area()}")    # 출력: Circle area: 78.53981633974483
```

## 추가 보완 내용

### 클래스 변수와 인스턴스 변수

클래스 변수는 클래스 전체에서 공유되는 변수이며, 인스턴스 변수는 각 객체마다 별도로 존재하는 변수이다.

**예제:**

```python
class Dog:
    species = "Canis familiaris"  # 클래스 변수

    def __init__(self, name, age):
        self.name = name    # 인스턴스 변수
        self.age = age      # 인스턴스 변수

# 객체 생성
dog1 = Dog("바둑이", 3)
dog2 = Dog("초코", 5)

print(dog1.species)  # 출력: Canis familiaris
print(dog2.species)  # 출력: Canis familiaris

# 클래스 변수를 변경하면 모든 객체에 반영됨
Dog.species = "Canis lupus familiaris"
print(dog1.species)  # 출력: Canis lupus familiaris
print(dog2.species)  # 출력: Canis lupus familiaris
```

### 메서드의 종류

1. **인스턴스 메서드**: 객체의 상태를 변경하거나 객체의 속성에 접근하는 메서드이다. 첫 번째 매개변수로 `self`를 받는다.
2. **클래스 메서드**: 클래스 자체에 작용하는 메서드로, 첫 번째 매개변수로 `cls`를 받는다. `@classmethod` 데코레이터를 사용한다.
3. **정적 메서드**: 클래스나 객체 상태와 무관하게 동작하는 메서드로, 특별한 매개변수를 받지 않는다. `@staticmethod` 데코레이터를 사용한다.

**예제:**

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 인스턴스 메서드
    def bark(self):
        print(f"{self.name}이(가) 멍멍 짖습니다.")

    # 클래스 메서드
    @classmethod
    def get_species(cls):
        return cls.species

    # 정적 메서드
    @staticmethod
    def is_domestic():
        return True

# 사용 예
dog = Dog("바둑이", 3)
dog.bark()             # 출력: 바둑이가(가) 멍멍 짖습니다.

print(Dog.get_species())  # 출력: Canis familiaris
print(Dog.is_domestic())  # 출력: True
print(dog.get_species())  # 출력: Canis familiaris
print(dog.is_domestic())  # 출력: True
```

### 연산자 오버로딩

Python에서는 클래스에 특정 연산자를 정의하여 객체 간의 연산을 커스터마이징할 수 있다. 이를 연산자 오버로딩이라고 한다.

**예제:**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 문자열 표현
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # 덧셈 연산자 오버로딩
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

# 객체 생성
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# 덧셈 연산
v3 = v1 + v2
print(v3)  # 출력: Vector(6, 8)
```

### 예외 처리와 OOP

객체지향 프로그래밍에서는 사용자 정의 예외를 만들어 특정 상황에서 예외를 처리할 수 있다.

**예제:**

```python
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount}원이 입금되었습니다.")
        else:
            print("유효한 금액을 입력하세요.")

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientFundsError("잔액이 부족합니다.")
        self.__balance -= amount
        print(f"{amount}원이 출금되었습니다.")

# 사용 예
account = BankAccount("홍길동", 1000)
account.deposit(500)         # 출력: 500원이 입금되었습니다.
try:
    account.withdraw(2000)
except InsufficientFundsError as e:
    print(e)                 # 출력: 잔액이 부족합니다.
```