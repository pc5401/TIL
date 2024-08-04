
# 객체지향 프로그래밍 (OOP) in Python

## 개요
객체지향 프로그래밍(Object-Oriented Programming, OOP)은 데이터를 객체로 취급하여 프로그래밍하는 방법이다. 객체는 데이터와 해당 데이터를 처리하는 메서드를 포함한다. OOP의 주요 개념으로는 클래스(Class), 객체(Object), 상속(Inheritance), 다형성(Polymorphism), 캡슐화(Encapsulation), 추상화(Abstraction) 등이 있다.

## 클래스와 객체
### 클래스
클래스는 객체를 생성하기 위한 청사진이다. 클래스는 속성(Attribute)과 메서드(Method)를 포함할 수 있다.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name}가 짖는다."
```

### 객체
객체는 클래스의 인스턴스(instance)이다. 객체는 클래스에 정의된 구조를 따른다.

```python
my_dog = Dog("바둑이", 3)
print(my_dog.bark())  # 바둑이가 짖는다.
```

## 상속
상속은 한 클래스가 다른 클래스의 속성과 메서드를 물려받는 것이다. 상속을 통해 코드의 재사용성을 높일 수 있다.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name}가 움직인다."

class Dog(Animal):
    def bark(self):
        return f"{self.name}가 짖는다."

my_dog = Dog("바둑이")
print(my_dog.move())  # 바둑이가 움직인다.
print(my_dog.bark())  # 바둑이가 짖는다.
```

## 다형성
다형성은 여러 클래스가 동일한 메서드를 가질 때, 해당 메서드가 각 클래스에 따라 다르게 동작하는 것을 의미한다.

```python
class Cat(Animal):
    def sound(self):
        return f"{self.name}가 야옹한다."

class Dog(Animal):
    def sound(self):
        return f"{self.name}가 짖는다."

animals = [Cat("야옹이"), Dog("바둑이")]

for animal in animals:
    print(animal.sound())

# 출력:
# 야옹이가 야옹한다.
# 바둑이가 짖는다.
```

## 캡슐화
캡슐화는 객체의 속성과 메서드를 하나로 묶고, 일부를 외부에 감추어 객체의 내부 상태를 보호하는 것이다.

```python
class Person:
    def __init__(self, name, age):
        self.__name = name  # __로 시작하는 변수는 비공개 속성이다.
        self.__age = age

    def get_info(self):
        return f"이름: {self.__name}, 나이: {self.__age}"

person = Person("홍길동", 25)
print(person.get_info())  # 이름: 홍길동, 나이: 25
```

## 추상화
추상화는 불필요한 세부사항을 감추고, 중요한 속성이나 메서드만을 노출하여 복잡성을 줄이는 것이다.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "멍멍"

class Cat(Animal):
    def sound(self):
        return "야옹"

dog = Dog()
cat = Cat()
print(dog.sound())  # 멍멍
print(cat.sound())  # 야옹
```

## 결론
객체지향 프로그래밍은 클래스를 통해 객체를 생성하고, 상속, 다형성, 캡슐화, 추상화 등의 개념을 활용하여 코드의 재사용성과 유지보수성을 높이는 프로그래밍 패러다임이다. Python은 강력한 객체지향 기능을 제공하여 이러한 개념을 쉽게 구현할 수 있다.
