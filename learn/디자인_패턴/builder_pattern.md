# 빌더 패턴(Builder Pattern)

> 복잡한 객체들을 단계별로 생성할 수 있도록 하는 생성 디자인 패턴

- 객체의 생성과 표현을 분리하여 동일한 생성 과정에서 다른 표현 결과를 얻을 수 있다.
- 같은 제작 코드를 사용하여 객체의 다양한 유형들과 표현을 제작할 수 있다.



**인터페이스와 클래스**

```tsx
interface Builder { // 객체를 생성하기 위한 메서드를 정의
  buildPart1(): void;
  buildPart2(): void;
  getResult(): Product;
}

class Product { // 실제 생성될 객체를 정의
  parts: string[] = [];

  addPart(part: string) { // 생성될 부품을 배열로 관리
    this.parts.push(part);
  }

  show() {
    console.log("Product parts: ", this.parts.join(", "));
  }
}
// Builder 인터페이스를 구현하는 클래스
class ConcreteBuilder implements Builder { 
  private product: Product = new Product();

// Product 객체의 부품을 추가하는 로직을 구현
  buildPart1() {
    this.product.addPart("Part 1");
  }

  buildPart2() {
    this.product.addPart("Part 2");
  }

  getResult(): Product {
    return this.product;
  }
}

class Director { // Builder 객체를 사용하여 실제 객체를 구축
  construct(builder: Builder) {
    builder.buildPart1();
    builder.buildPart2();
  }
}
```

**실행 예제**

```tsx
const builder: Builder = new ConcreteBuilder();
const director = new Director();
//construct 메서드를 통해 ConcreteBuilder 객체에게 제품을 만들라고 지시
director.construct(builder);
const product: Product = builder.getResult(); // roduct 객체를 가져옴
product.show(); // Output: "Product parts: Part 1, Part 2"
```

## **실무 예시와 컨텍스트**

- **복잡한 객체 생성**: 여러 단계를 거쳐야 생성되는 복잡한 객체를 만들 때 사용됩니다.
- **플루언트 API**: 체이닝을 통한 더 명확하고 읽기 좋은 코드 생성이 가능합니다.
- **불변 객체**: 불변성을 유지하면서 객체를 생성할 때 유용합니다.

## **유명 라이브러리/프레임워크**

- **Java's StringBuilder**: Java에서 문자열을 효율적으로 만드는 데 사용되는 빌더 패턴의 예입니다.
- **Lombok's @Builder**: Java 라이브러리 Lombok에서 제공하는 빌더 패턴 애너테이션입니다.
- **Query Builders**: SQL 문을 프로그래밍적으로 생성할 때 사용되는 빌더 패턴의 일종입니다.
