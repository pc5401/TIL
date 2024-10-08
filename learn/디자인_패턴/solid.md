# SOLID: 객체지향 개발 5대 원리

## 단일 책임 원칙(SRP,Single Responsibility principle)

하나의 클래스는 **목적에 부합하는 하나의 책임**만 가져야 한다.

- 책임이란 기준이 모호하기 때문에 **변경**을 책임의 기준으로 삼으면 설계에 용이할 수 있다.
- 어떤 역할에 대해 변경 사항이 발생했을 때, 영향을 받는 기능만 모아둔 클래스라면, 동일한 책임을 지닌 기능이 모인 집합으로 SRP 원칙이 적용된 설계라고 볼 수 있다.
- 이처럼 **변경 사항이 있을 때, 애플리케이션의 파급 효과가 적으면** SRP 원칙을 잘 따른 것으로 볼 수 있다.

예시

```python
class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

# SRP 위반: User 클래스가 이메일 전송 책임도 가지고 있음
class UserWithMail(User):
    def send_email(self, message: str):
        print(f"Sending email to {self.email} with message: {message}")

# SRP 준수: 이메일 전송 책임을 분리
class EmailService:
    def send_email(self, email: str, message: str):
        print(f"Sending email to {email} with message: {message}")

user = User("john_doe", "john@example.com")
email_service = EmailService()
email_service.send_email(user.email, "Welcome to our service!")
```

## 개방-폐쇄 원칙(OCP, Open-Closed Principle)

**코드는 확장에 열려있고 수정에 닫혀있어야 한다.**

- **높은 응집도와 낮은 결합도**가 핵심!
- 높은 응집도
  - 하나의 모듈, 클래스가 하나의 책임 또는 관심사에만 집중한다.
  - 객체 변경이 발생해도 다른 곳에 미치는 영향이 제한적이다.
- 낮은 결합도
  - 결합도란, 객체가 변경될 때 관계를 맺고 있는 다른 객체에게 변화를 요구하는 정도다. → 변경 요구의 전파 수
  - 책임과 관심사가 다른 객체와 모듈과는 낮은 결합도를 유지해야 한다.
  - 높은 응집도 보다 민감하고 중요하다.

예시

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# 새로운 도형을 추가할 때 기존 코드 수정 없이 확장 가능
class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
```

## 리스코프 치환 법칙(LSP, Liskov Substitution Principle)

**부모 타입 객체가 자식 타입 객체로 변환되어도 프로그램 동작에는 이상이 없어야 한다.**

- **다형성**을 지원하기 위한 원칙
- 객체는 프로그램의 정확성을 깨지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 한다.
- 하위 클래스는 인터페이스 규약을 지켜서 작성되어야 한다.

예시

```python
class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(Bird):
    def fly(self):
        print("Ostriches can't fly")

def make_bird_fly(bird: Bird):
    bird.fly()

sparrow = Sparrow()
make_bird_fly(sparrow)  # 정상 작동

ostrich = Ostrich()
make_bird_fly(ostrich)  # "Ostriches can't fly" 출력
```

## 인터페이스 분리원칙(ISP, Interface segregation rinciple)

범용 인터페이스 하나보다는 특정 클라이언트를 위한 여러 개의 인터페이스 분리가 더 좋다.

- 클라이언트 관점에서 맞춤을 제공하기 용이하다.

ex. 복합기(범용) 하나 보다 프린터(특정), 복사기(특정) 스캐너(특정), 팩스(특정)를 더하는 게 낫다.

예시

```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionDevice(Printer, Scanner):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

class SimplePrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")

# 특정 클라이언트를 위한 인터페이스 분리
printer = SimplePrinter()
printer.print("My Document")

multi_function_device = MultiFunctionDevice()
multi_function_device.print("My Document")
multi_function_device.scan("My Document")
```

## 의존관계 역전(DIP Dependency inversion Principle)

구체적인 개념보다는 추상적인 개념에 의존해야 한다.

예시

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing payment of {amount} through Stripe")

class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing payment of {amount} through PayPal")

class CheckoutService:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def checkout(self, amount: float):
        self.payment_processor.process_payment(amount)

# 사용 예
stripe_processor = StripePaymentProcessor()
checkout_service = CheckoutService(stripe_processor)
checkout_service.checkout(100.0)

paypal_processor = PayPalPaymentProcessor()
checkout_service = CheckoutService(paypal_processor)
checkout_service.checkout(200.0)
```


