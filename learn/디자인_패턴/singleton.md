# Singleton Pattern (싱글턴 패턴)
- **목적**: 특정 클래스의 인스턴스가 단 하나만 존재하도록 보장하는 디자인 패턴이다. 전역 변수를 사용하지 않고도 애플리케이션 어디서든 해당 인스턴스에 접근할 수 있게 제공한다.
- **용도**: 로깅, 드라이버 객체, 캐싱, 스레드 풀, 데이터베이스 연결 등에서 유용하게 사용된다.

### 장점
- 하나의 인스턴스를 기반으로 해당 인스턴스를 다른 모듈들이 공유하여 사용하기 때문에 인스턴스를 생성할 때 드는 비용이 감소된다.
- 많은 인스턴스 생성 비용이 드는 I/O 바운드 작업에 많이 사용된다.

### 단점
- 의존성이 높아지며 테스트 주도 개발(TDD)에서 테스트가 어렵다.
  - 전역 상태를 가지므로 테스트 케이스 간에 상태가 공유될 수 있어 테스트하기 어렵다.
  - 이 문제를 해결하기 위해 싱글턴 객체를 재설정할 수 있는 메서드를 제공할 수 있으나, 이는 싱글턴의 원칙을 약간 왜곡하는 것이다.
- 클라이언트가 구체 클래스에 의존하게 된다.
  - 싱글턴 객체를 인터페이스를 통해 접근하도록 설계함으로써 어느 정도 해결할 수 있다.
- 상태 있는 설계 문제
  - 객체가 상태를 갖게 되면 그 상태가 전역으로 공유되므로 예상치 못한 부작용이 발생할 수 있다. 따라서 무상태(stateless)로 설계하는 것이 좋다.
  - 여러 클라이언트가 동시에 해당 객체를 사용해 서로에게 영향을 주게 되면 안 된다.
  - 특히 멀티 스레드 환경에서는 필드를 최대한 읽기 전용으로 만들고, 상태가 필요한 연산은 메서드의 지역 변수나 파라미터, 또는 ThreadLocal 등을 사용하여 처리하는 것이 좋다.


## 예시 코드

```tsx
class Singleton {
  private static instance: Singleton; // 클래스 내부에서 유일한 인스턴스를 저장하는 정적 멤버
  // private 로 선언하여 클래스 외부에서 new 키워드를 이용한 인스턴스 생성을 방지
  private constructor() { 
    // 초기화 로직
  }

  public static getInstance(): Singleton { 
    if (!Singleton.instance) { // 인스턴스가 아직 생성되지 않았다면 새로 생성하여 반환
      Singleton.instance = new Singleton();
    }
    return Singleton.instance; // 유일한 인스턴스를 반환하는 정적 메서드
  } 
}

const instance1 = Singleton.getInstance();
const instance2 = Singleton.getInstance();

console.log(instance1 === instance2);  // true

```

```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # True
```

```java
public class Singleton {
    private static Singleton instance;
    
    private Singleton() {}
    
    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}

Singleton instance1 = Singleton.getInstance();
Singleton instance2 = Singleton.getInstance();
System.out.println(instance1 == instance2);  // true
```

```C++
class Singleton {
private:
    static Singleton* instance;
    Singleton() {}

public:
    static Singleton* getInstance() {
        if (!instance) {
            instance = new Singleton();
        }
        return instance;
    }
};

Singleton* Singleton::instance = nullptr;

Singleton* instance1 = Singleton::getInstance();
Singleton* instance2 = Singleton::getInstance();
std::cout << (instance1 == instance2) << std::endl;  // 1
```

## **사용 사례**

**로깅**

- 여러 부분에서 로그를 남길 때, 모든 로그를 한 군데에서 관리할 수 있습니다.

**데이터베이스 연결**

- 데이터베이스 연결 객체를 하나만 유지하면, 불필요한 연결을 방지하고 자원을 효율적으로 사용할 수 있습니다.

**설정 관리**

- 애플리케이션의 설정 정보를 중앙에서 관리할 때 싱글턴을 사용하면 편리합니다.

### **유명 라이브러리**

**Node.js의 `global`**

- Node.js에서는 **`global`** 객체가 싱글턴 패턴으로 동작합니다.

**Spring Framework**

- Spring에서 빈(bean) 객체가 기본적으로 싱글턴 스코프로 생성됩니다.

**Redux**

- Redux의 store는 애플리케이션에 하나만 존재하는 싱글턴 객체입니다.