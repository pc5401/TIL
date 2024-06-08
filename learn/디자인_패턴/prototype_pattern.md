# 프로토타입 패턴(Prototype Pattern)

> 생성 패턴, 기존 객체를 복제하여 새로운 객체를 생성하는 디자인 패턴

- 큰 데이터나 복잡한 객체를 생성하는 데 비용이 많이 들 때, 기존 객체의 복사본을 사용하여 새로운 객체를 빠르게 생성

**인터페이스와 클래스**

```tsx
interface Prototype {
  clone(): Prototype; // 복사 기능 필수
}

class ConcretePrototype implements Prototype {
  private field: string;

  constructor(field: string) {
    this.field = field;
  }
// Prototype 인터페이스를 구현
  clone(): ConcretePrototype {
// clone 메서드에서는 객체의 복사본을 반환
    return new ConcretePrototype(this.field);
  }

  showField(): void {
    console.log(`Field value: ${this.field}`);
  }
}
```

**실행 예제**

```tsx
// ConcretePrototype 객체를 생성
const prototype1 = new ConcretePrototype("A");
// 해당 객체의 showField 메서드로 필드 값을 출
prototype1.showField();  // Output: "Field value: A"

// clone 메서드를 사용하여 기존 객체의 복사본을 생성
const prototype2 = prototype1.clone();
// 복사된 객체의 필드 값을 확
prototype2.showField();  // Output: "Field value: A"
```

## **실무 예시와 컨텍스트**

- **캐시와 객체 재사용**: 비용이 많이 드는 객체의 상태를 저장해두고 필요할 때 복제하여 사용할 수 있습니다.
- **변형 없는 객체 생성**: 기존 객체의 상태를 변경하지 않고, 새로운 객체를 생성하려는 경우에 사용됩니다.

프로토타입 패턴은 객체를 새로 생성하는 것이 비용이 클 때, 특히 초기화 시간이 길거나 리소스를 많이 사용하는 객체의 경우에 효과적입니다. 이 패턴을 사용하면 기존 객체를 복제하여 빠르게 새 객체를 생성할 수 있습니다.