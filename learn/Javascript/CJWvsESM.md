# CJS vs ESM

> CJS(CommonJS)와 ESM(ES6 Modules)은 자바스크립트 모듈 시스템의 두 가지 주요 유형이다. 각각의 특징과 사용 사례를 통해 비교하자.
> 

## CommonJS (CJS)

1. **역사와 배경**
    - CommonJS는 Node.js의 기본 모듈 시스템이다. Node.js의 초창기부터 사용되어왔다.
    - 서버 사이드 자바스크립트 애플리케이션을 작성할 때 널리 사용된다.
    - 최근에는 덜 쓰는 방향이다.
2. **문법**
    - `require`와 `module.exports`를 사용한다.
    
    예시: 단일 값 내보내기
    
    - 모듈 내보내기
        
        ```jsx
        // math.js
        const add = (a, b) => a + b;
        module.exports = { add };
        ```
        
    - 모듈 가져오기
        
        ```jsx
        // app.js
        const math = require('./math');
        console.log(math.add(2, 3)); // 5
        ```
        
    
    예시: 여러 값 내보내기
    
    - 모듈 내보내기
        
        ```jsx
        // math.js
        const add = (a, b) => a + b;
        const subtract = (a, b) => a - b;
        module.exports = { add, subtract };
        ```
        
    - 모듈 가져오기
        
        ```jsx
        // app.js
        const math = require('./math');
        console.log(math.add(2, 3)); // 5
        console.log(math.subtract(5, 3)); // 2
        ```
        
3. **특징**
    - 동기적 로딩: 모듈을 로드할 때 파일 시스템을 동기적으로 접근한다. 이는 서버 사이드 환경에서는 문제가 되지 않지만, 클라이언트 사이드에서는 성능 문제를 야기할 수 있다.
    - 순환 참조 지원: 모듈 간에 순환 참조가 발생해도 비교적 문제없이 동작한다.
    - 단순함: 간단하고 직관적인 문법.
    - Node.js와의 호환성: Node.js에서 기본적으로 지원, 서버 사이드 개발에 최적화됨.
    - 동기적 로딩의 한계: 브라우저 환경에서는 비동기 로딩이 일반적이므로 비효율적일 수 있다.
    - 정적 분석 어려움: ESM에 비해 정적 분석이 어려워 트리 쉐이킹 등의 최적화가 제한적이다.

## ES6 Modules (ESM)

1. **역사와 배경**
    - ES6 모듈은 ECMAScript 2015(ES6)에서 도입되었으며, 표준 자바스크립트 모듈 시스템이다.
    - 브라우저와 서버 환경 모두에서 사용 가능하다.
2. **문법**
    - `import`와 `export`를 사용한다.
        
        예시: 단일 값 내보내기
        
        - 모듈 내보내기
            
            ```jsx
            // math.js
            const add = (a, b) => a + b;
            export default add;
            ```
            
        - 모듈 가져오기
            
            ```jsx
            // app.js
            import add from './math.js';
            console.log(add(2, 3)); // 5
            ```
            
        
        예시: 여러 값 내보내기
        
        - 모듈 내보내기
            
            ```jsx
            // math.js
            export const add = (a, b) => a + b;
            export const subtract = (a, b) => a - b;
            ```
            
        - 모듈 가져오기
            
            ```jsx
            // app.js
            import { add, subtract } from './math.js';
            console.log(add(2, 3)); // 5
            console.log(subtract(5, 3)); // 2
            ```
            
        
        예시: 단일 값 및 여러 값 혼합 내보내기
        
        - 모듈 내보내기
            
            ```jsx
            // math.js
            const multiply = (a, b) => a * b;
            const divide = (a, b) => a / b;
            export default multiply;
            export { divide };
            ```
            
        - 모듈 가져오기
            
            ```jsx
            // app.js
            import multiply, { divide } from './math.js';
            console.log(multiply(2, 3)); // 6
            console.log(divide(6, 3)); // 2
            ```
            
3. **특징**
    - 비동기적 로딩: 브라우저에서 모듈을 비동기적으로 로드하여 성능을 향상시킬 수 있다.
    - 정적 분석 가능: ES6 모듈은 정적으로 분석될 수 있어, 트리 쉐이킹(tree shaking)과 같은 최적화 기술에 유리하다.
    - 표준화: ECMAScript 표준의 일부로, 미래 지향적 개발에 적합하다.
    - 정적 구조: 컴파일 타임에 모듈의 의존성을 분석할 수 있어 최적화가 용이하다.
    - 호환성 문제: 기존의 CommonJS 모듈과의 호환성 문제가 있을 수 있다.
    - 설정 필요성: Node.js에서 ESM을 사용하려면 파일 확장자 변경(.mjs)이나 `package.json` 설정이 필요하다.

## 사용 사례 비교

1. **서버 사이드(Node.js)**
    - CommonJS가 기본 모듈 시스템으로 채택되어 있으며, 대부분의 Node.js 프로젝트에서 여전히 CommonJS를 사용한다.
    - ES6 모듈도 Node.js에서 사용할 수 있지만, 현재(2024년 기준)까지는 설정이 다소 복잡할 수 있다.
    - ES6 모듈을 사용하려면 `package.json`에 `"type": "module"`을 추가해야 한다.
2. **클라이언트 사이드(브라우저)**
    - ES6 모듈이 표준으로 자리 잡았다. `<script type="module">` 태그를 사용하여 모듈을 로드할 수 있다.
    - CommonJS는 브라우저에서 직접 지원되지 않기 때문에, 번들러(예: Webpack, Browserify)를 사용하여 ES6 모듈 형식으로 변환해야 한다.
3. **번들링**
    - 대부분의 모던 프론트엔드 프로젝트는 Webpack이나 Rollup 같은 번들러를 사용하여 모듈을 번들링한다. 이 경우 ES6 모듈을 사용하는 것이 일반적이다.
    - CommonJS 모듈도 번들링이 가능하지만, ES6 모듈을 사용하는 것이 트리 쉐이킹 등 최적화 측면에서 유리하다.

## CJS와 ESM의 주요 차이점

| 특징 | CommonJS (CJS) | ES Modules (ESM) |
| --- | --- | --- |
| **로드 방식** | 동기적 | 비동기적 |
| **내보내기** | `module.exports` 또는 `exports` | `export` 키워드 |
| **가져오기** | `require` 함수 | `import` 키워드 |
| **호환성** | Node.js에서 주로 사용 | 브라우저와 Node.js 모두에서 사용 가능 |
| **정적 분석** | 어려움 | 용이 (트리 쉐이킹, 코드 스플리팅 등 가능) |
| **파일 확장자** | `.js` | `.mjs` 또는 `package.json` 설정 필요 |
| **동적 가져오기** | `require`로 가능 | `import()` 함수로 동적 가져오기 가능 |

## 추가 확장자 .mjs 사용하기

> ES6 모듈 시스템은 .mjs 확장자를 사용하여 package.json 파일의 설정 없이도 모듈화를 지원할 수 있다.
> 

### 1️⃣ 모듈 내보내기 (Export)

- `.mjs` 확장자를 사용하여 모듈 파일을 작성. 예를 들어, `math.mjs` 파일에서 함수를 내보낸다.

```jsx
// math.mjs
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;
```

### 2️⃣ 모듈 가져오기 (Import)

- 다른 파일에서 .mjs 확장자를 사용하여 모듈을 가져온다. 예를 들어, `app.mjs` 파일에서 `math.mjs` 파일을 가져온다.

```jsx
// app.mjs
import { add, subtract } from './math.mjs';
console.log(add(2, 3)); // 5
console.log(subtract(5, 3)); // 2
```

### 3️⃣ Node.js에서 .mjs 파일 실행하기

- Node.js에서 .mjs 파일을 실행할 때는 별도의 설정이 필요 없다. 단순히 파일을 실행한다.

```bash
node app.mjs
```

### 확장자 .mjs의 장점

1. **설정 간소화**
    - `package.json` 파일에 `"type": "module"` 설정을 추가할 필요 없이, .mjs 확장자를 사용하여 ES6 모듈을 사용할 수 있다.
2. **명확한 구분**
    - .mjs 확장자를 사용하면, 해당 파일이 ES6 모듈임을 명확하게 구분할 수 있다. 이는 프로젝트 관리와 협업 시에 코드의 모듈 시스템을 쉽게 파악할 수 있게 해준다.

## Node.js에서 CJS와 ESM 사용하기

### CJS 사용

- 기본적으로 Node.js는 `.js` 파일을 CommonJS로 인식.
- `require`와 `module.exports` 사용.

### ESM 사용

- 파일 확장자를 `.mjs`로 설정하거나, `package.json`에 `"type": "module"` 추가.
- `import`와 `export` 키워드 사용.
- ESM을 사용할 경우, CJS 모듈을 `import`하기 위해서는 `createRequire`와 같은 추가적인 방법이 필요하다.

```json
// package.json
{
  "type": "module"
}
```

```jsx
// math.mjs
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;
```

```jsx
// app.mjs
import { add, subtract } from './math.mjs';
console.log(add(2, 3)); // 5
console.log(subtract(5, 2)); // 3
```

## CJS와 ESM의 상호 운용성

- **CJS에서 ESM 가져오기**: `import` 구문을 사용할 수 없으며, 동적 `import()`를 사용해야 한다.
- **ESM에서 CJS 가져오기**: `import` 구문으로 직접 가져올 수 없고, `createRequire`을 사용해야 한다.

### 예시: ESM에서 CJS 모듈 가져오기

```jsx
// app.mjs
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const cjsModule = require('./cjsModule.js');

console.log(cjsModule.someFunction());
```

## 마이그레이션 고려사항

### CJS에서 ESM으로 전환

- 파일 확장자 변경: `.js`에서 `.mjs`로 변경하거나 `package.json`에 `"type": "module"` 추가.
- `import/export` 구문 사용: `require`와 `module.exports`를 `import`와 `export`로 변경.
- 호환성 확인: 외부 라이브러리와의 호환성 점검.

### ESM에서 CJS로 전환

- 주로 필요하지 않지만, ESM 기능을 사용하지 않고 싶다면 `package.json`에서 `"type": "commonjs"` 설정.
- `import`와 `export`를 `require`와 `module.exports`로 변경.

## 결론

- CommonJS는 주로 Node.js 환경에서 사용되며, 기존의 많은 서버 사이드 코드베이스에서 볼 수 있다.
- ES6 모듈은 브라우저와 서버 모두에서 사용할 수 있으며, 최신 자바스크립트 프로젝트에서 권장된다.
- 번들러를 사용할 때는 ES6 모듈을 사용하는 것이 더 나은 선택이다. 이는 코드 최적화와 성능 측면에서 장점을 제공하기 때문이다.
- ESM의 정적 분석과 트리 쉐이킹 등의 이점을 활용할 수 있다면 ESM을 사용하는 것이 현대적인 접근이다. 그러나 레거시 코드나 일부 패키지의 호환성 문제로 인해 CJS를 계속 사용하는 경우도 많다.
- 클라이언트 사이드 개발에서는 ES6 모듈이 표준으로 자리 잡았으므로, ESM을 사용하는 것이 적합하다.

## 추가 자료

- [MDN 웹 문서: JavaScript 모듈](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Modules)