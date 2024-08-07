#Node.js에서 프로세스 메모리 관리 방식

Node.js에서 프로세스 메모리 관리는 V8 자바스크립트 엔진의 가비지 컬렉션과 힙 메모리 관리 기법을 기반으로 이루어진다. 메모리 사용을 최적화하고 메모리 누수를 방지하기 위해 다양한 도구와 기법을 사용할 수 있으며, 객체 재사용, 클로저 사용 주의, 정기적인 메모리 릴리스 등의 최적화 기법을 통해 효율적인 메모리 관리를 할 수 있다.

---

### 1. 메모리 구조

Node.js 프로세스 메모리는 크게 다음과 같은 영역으로 나뉜다:

1. **코드 영역 (Code Segment)**:
  - 실행 파일의 코드가 저장되는 영역
2. **데이터 영역 (Data Segment)**:
  - 초기화된 전역 변수와 정적 변수가 저장되는 영역
3. **힙 영역 (Heap Segment)**:
  - 동적 메모리 할당이 이루어지는 영역
  - V8 엔진의 가비지 컬렉터(Garbage Collector)가 메모리 관리를 담당
4. **스택 영역 (Stack Segment)**:
  - 함수 호출 시 매개 변수와 지역 변수가 저장되는 영역

### 2. V8 엔진의 메모리 관리

Node.js의 메모리 관리는 주로 V8 자바스크립트 엔진에 의해 이루어진다. V8 엔진은 다음과 같은 메모리 관리 기법을 사용한다:

1. **가비지 컬렉션 (Garbage Collection)**:
  - V8 엔진은 주기적으로 가비지 컬렉션을 수행하여 더 이상 사용되지 않는 객체를 메모리에서 해제한다
  - 주요 가비지 컬렉션 알고리즘:
      - **마이너 가비지 컬렉션 (Minor GC)**: 작은 힙 영역인 새로운 공간(New Space)에서 수행
      - **메이저 가비지 컬렉션 (Major GC)**: 큰 힙 영역인 오래된 공간(Old Space)에서 수행.
2. **힙 메모리 제한**:
  - Node.js는 힙 메모리에 대한 기본 제한이 있다. 이 제한은 `-max-old-space-size`와 `-max-semi-space-size` 플래그를 사용하여 조정할 수 있다.
  - 기본적으로 64비트 시스템에서는 약 1.5GB, 32비트 시스템에서는 약 512MB로 설정되어 있다.

### 3. 메모리 프로파일링과 디버깅

Node.js 애플리케이션의 메모리 사용을 프로파일링하고 디버깅하기 위해 다음과 같은 도구와 기법을 사용할 수 있다:

1. **프로세스 메모리 사용 조회**:
  - Node.js의 `process.memoryUsage()` 메서드를 사용하여 현재 프로세스의 메모리 사용량을 확인할 수 있다.
  - 반환되는 정보:
      - `rss` (Resident Set Size): 프로세스가 사용하는 전체 메모리
      - `heapTotal`: V8 힙의 총 메모리 할당량
      - `heapUsed`: V8 힙에서 실제로 사용 중인 메모리
      - `external`: V8 외부에서 사용 중인 메모리
2. **Heap Snapshot**:
  - `-inspect` 플래그를 사용하여 Node.js 애플리케이션을 디버깅 모드로 실행하고, Chrome DevTools를 사용하여 힙 스냅샷을 찍을 수 있다.
  - 힙 스냅샷을 통해 객체 그래프와 메모리 사용을 시각적으로 분석할 수 있다.
3. **메모리 누수 디버깅**:
  - `node --inspect`와 같은 디버깅 플래그를 사용하여 애플리케이션을 실행한 후, Chrome DevTools 또는 VSCode와 같은 디버깅 도구를 통해 메모리 누수를 찾아낼 수 있다.
  - `node-memwatch`와 같은 라이브러리를 사용하여 메모리 누수를 감지하고 분석할 수 있다.

### 4. 메모리 관리 최적화 tip
Node.js 애플리케이션에서 메모리 사용을 최적화하고 메모리 누수를 방지하기 위해 다양한 기법을 사용할 수 있다. 다음은 주요 메모리 관리 최적화 기법이다

1. 객체 재사용:
   - 반복적으로 생성되는 객체는 재사용하여 메모리 할당과 해제를 줄일 수 있다.
   - 예를 들어, 루프 내부에서 객체를 매번 생성하는 대신, 루프 외부에서 객체를 생성하고 값을 재설정하여 사용한다.

2. 클로저 사용 주의:
   - 클로저는 함수 내에서 함수가 정의될 때의 환경을 기억하기 때문에, 의도치 않게 메모리를 유지할 수 있다.
   - 불필요한 클로저 사용을 피하고, 클로저가 참조하는 외부 변수의 범위를 최소화한다.

3. 정기적인 메모리 릴리스:
   - 사용 후 더 이상 필요하지 않은 대규모 객체나 배열은 null 또는 undefined로 설정하여 메모리에서 해제될 수 있도록 한다.
   - 이벤트 리스너를 등록한 후에는 반드시 필요하지 않을 때 제거한다.

4. 메모리 누수 방지:
   - 글로벌 객체나 캐시된 데이터를 주의 깊게 관리하여 메모리 누수가 발생하지 않도록 한다.
   - 강한 참조와 약한 참조를 적절히 사용하여 메모리 관리를 최적화한다. WeakMap, WeakSet과 같은 구조를 사용하여 필요하지 않은 객체가 가비지 컬렉터에 의해 회수될 수 있도록 한다.

5. 효율적인 데이터 구조 사용:
   - 메모리 사용을 줄이기 위해 효율적인 데이터 구조를 사용한다. 예를 들어, 큰 배열을 사용할 때는 Uint8Array, Float32Array와 같은 TypedArray를 사용할 수 있다.
   - JSON 객체를 자주 사용하는 경우, JSON.stringify와 JSON.parse를 통해 객체를 직렬화하고 역직렬화하여 메모리를 최적화할 수 있다.

6. 비동기 작업의 주의:
   - 비동기 작업이 완료되면 사용한 메모리를 정리한다. 특히, 콜백 함수나 프로미스 체인에서 생성된 객체를 적절히 해제한다.
   - 비동기 작업에서 에러 핸들링을 제대로 구현하여 메모리 누수를 방지한다.