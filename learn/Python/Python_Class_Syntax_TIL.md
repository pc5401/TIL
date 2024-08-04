
# Python 클래스 문법 정리

## 개요
Python에서 클래스는 객체를 생성하기 위한 청사진이다. 클래스는 속성(attribute)과 메서드(method)를 정의할 수 있다. 여기에서는 Python 클래스의 주요 문법을 설명한다.

## 클래스 정의
클래스는 `class` 키워드를 사용하여 정의한다.

```python
class MyClass:
    pass
```

## 생성자와 속성
생성자는 클래스가 인스턴스화될 때 호출되는 메서드로, `__init__` 메서드를 사용하여 정의한다. 속성은 `self` 키워드를 사용하여 정의한다.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("바둑이", 3)
print(my_dog.name)  # 바둑이
print(my_dog.age)   # 3
```

## 메서드
메서드는 클래스 내부에 정의된 함수이다. 메서드는 첫 번째 인자로 항상 `self`를 받아야 한다.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name}가 짖는다."

my_dog = Dog("바둑이", 3)
print(my_dog.bark())  # 바둑이가 짖는다.
```

## 클래스 변수와 인스턴스 변수
클래스 변수는 클래스에 속한 변수로, 모든 인스턴스가 공유한다. 인스턴스 변수는 각 인스턴스에 속한 변수이다.

```python
class Dog:
    species = "Canis familiaris"  # 클래스 변수

    def __init__(self, name, age):
        self.name = name          # 인스턴스 변수
        self.age = age

my_dog = Dog("바둑이", 3)
print(Dog.species)      # Canis familiaris
print(my_dog.species)   # Canis familiaris
print(my_dog.name)      # 바둑이
print(my_dog.age)       # 3
```

## 클래스 메서드와 정적 메서드
클래스 메서드는 클래스 자체를 인자로 받으며, `@classmethod` 데코레이터를 사용하여 정의한다. 정적 메서드는 클래스나 인스턴스와 무관하게 동작하며, `@staticmethod` 데코레이터를 사용하여 정의한다.

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def is_adult(age):
        return age >= 3

print(Dog.get_species())       # Canis familiaris
print(Dog.is_adult(5))         # True
print(Dog.is_adult(1))         # False
```

## 상속
상속은 기존 클래스를 기반으로 새로운 클래스를 정의하는 방법이다. 자식 클래스는 부모 클래스의 속성과 메서드를 물려받을 수 있다.

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

## 캡슐화
캡슐화는 객체의 속성과 메서드를 외부에서 직접 접근하지 못하도록 보호하는 것이다. 이는 속성 이름 앞에 밑줄을 붙여서 구현할 수 있다.

```python
class Person:
    def __init__(self, name, age):
        self.__name = name  # __로 시작하는 변수는 비공개 속성이다.
        self.__age = age

    def get_info(self):
        return f"이름: {self.__name}, 나이: {self.__age}"

person = Person("홍길동", 25)
print(person.get_info())  # 이름: 홍길동, 나이: 25
# print(person.__name)    # 에러 발생
```

## 결론
이 문서에서는 Python 클래스의 주요 문법 요소에 대해 설명했다. 클래스 정의, 생성자와 속성, 메서드, 클래스 변수와 인스턴스 변수, 클래스 메서드와 정적 메서드, 상속, 캡슐화에 대해 다루었다. 이를 통해 Python에서 객체지향 프로그래밍을 효과적으로 사용할 수 있다.
