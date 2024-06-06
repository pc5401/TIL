# 팩토리 메서드 패턴 (Factory Method Pattern)

팩토리 메서드 패턴은 생성 패턴 중 하나로, 부모 객체를 생성할 때 필요한 인터페이스를 정의하고, 어떤 클래스의 인스턴스를 만들지는 서브클래스(자식)에서 처리한다. 

- 객체 생성의 책임을 전담하는 '팩토리' 메서드를 정의하여 객체를 생성하는 과정과 클래스를 분리한다.

- 객체 생성 로직을 분리하여 유지보수가 쉬워지고, 코드의 재사용성과 확장성도 높아진다.

- 팩토리로 손쉽게 객체를 생성해도 여러 가지 추가 기능이 필요할 수 있다.
  
  - 예시: 객체 정보, 상태, 새로운 기능 추가
  
  ## 예제 코드

### TypeScript

```typescript
// 인터페이스 정의
interface Product { 
  operation(): string;
}

// ConcreteProduct 클래스
class ConcreteProductA implements Product {
  public operation(): string {
    return 'ConcreteProductA의 operation 메서드';
  }
}

class ConcreteProductB implements Product {
  public operation(): string {
    return 'ConcreteProductB의 operation 메서드';
  }
}

// Creator 클래스
abstract class Creator {
  public abstract factoryMethod(): Product;

  public someOperation(): string {
    const product = this.factoryMethod();
    return `Creator: ${product.operation()}`;
  }
}

// ConcreteCreator 
class ConcreteCreatorA extends Creator {
  public factoryMethod(): Product {
    return new ConcreteProductA();
  }
}

class ConcreteCreatorB extends Creator {
  public factoryMethod(): Product {
    return new ConcreteProductB();
  }
}

// 메인
const creator1: Creator = new ConcreteCreatorA();
console.log(creator1.someOperation());  
// "Creator: ConcreteProductA의 operation 메서드

const creator2: Creator = new ConcreteCreatorB();
console.log(creator2.someOperation());  
// "Creator: ConcreteProductB의 operation 메서드
```

### python

```py
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProductA(Product):
    def operation(self) -> str:
        return 'ConcreteProductA의 operation 메서드'

class ConcreteProductB(Product):
    def operation(self) -> str:
        return 'ConcreteProductB의 operation 메서드'

class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f'Creator: {product.operation()}'

class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

creator1 = ConcreteCreatorA()
print(creator1.some_operation())
# "Creator: ConcreteProductA의 operation 메서드"

creator2 = ConcreteCreatorB()
print(creator2.some_operation())
# "Creator: ConcreteProductB의 operation 메서드"
```
