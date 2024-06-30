# 자바스크립트의 기본적인 사용

### 목차

[콘솔 활용하기](콘솔-활용하기)

[JavaScript 단축 평가 (Short-circuit Evaluation)](JavaScript-단축 평가-(short-circuit-evaluation))

[CJW vs ESM](cjw-vs-esm)

## 콘솔 활용하기

- 소개 콘솔(console)은 자바스크립트 코드를 실행하고 결과를 확인하는 데 유용한 도구이다. 

- 주로 웹 브라우저의 개발자 도구(Developer Tools)에서 사용한다. 

#### 예시

```js
console.log("Hello, world!"); // "Hello, world!"를 출력한다.
```

##### 다양한 콘솔

- **console.log()**: 메시지를 콘솔에 출력한다.
- **console.error()**: 에러 메시지를 콘솔에 출력한다.
- **console.warn()**: 경고 메시지를 콘솔에 출력한다.
- **console.table()**: 데이터를 표 형태로 콘솔에 출력한다.

##### 헷갈리기 쉬운 내용

- 콘솔에 출력되는 내용은 실제로 화면에 표시되지 않으며, 오직 개발자가 디버깅할 때만 확인할 수 있다.
- `console.log()`를 사용하면 문자열뿐만 아니라 변수, 객체 등 다양한 데이터를 출력할 수 있다.

```js
let obj = { name: "Alice", age: 25 };
console.table(obj); // 객체를 표 형식으로 출력한다.
```

## JavaScript 단축 평가 (Short-circuit Evaluation)

JavaScript에서 단축 평가는 논리 연산자 `&&`, `||`, `??`를 사용할 때 발생하는 평가 방식이다. 이 연산자들은 조건을 평가하는 도중에 불필요한 연산을 생략하여 효율성을 높인다.

## `&&` 연산자

`&&`는 논리 AND 연산자이다. 첫 번째 피연산자가 거짓이면 두 번째 피연산자를 평가하지 않고 거짓을 반환한다. 첫 번째 피연산자가 참이면 두 번째 피연산자를 반환한다.

### 예시

```javascript
let a = 0;
let b = 10;

let result = (a > 0 && b > 0); // false
```

> 위 예시에서 a > 0이 거짓이기 때문에 b > 0을 평가하지 않고 false를 반환한다.

### 조건부 실행

```js
let hasError = true;
// hasError = false;

// 앞의 것이 true일 때만 뒤의 코드 실행
hasError && console.warn('오류 발생!');
```

> `hasError`가 참일 때만 `console.warn('오류 발생!')`이 실행된다.

## `||` 연산자

`||` 연산자는 첫 번째 피연산자가 거짓일 경우에만 두 번째 피연산자를 평가하고 실행한다

### 예시

```javascript
let hasError = false;

// 앞의 것이 false일 때만 뒤의 코드 실행
hasError || console.log('이상 없음.');
```

> 위 예시에서 `hasError`가 **거짓**일 때만 `console.log('이상 없음.')`이 실행된다.

## `&&`, `||` 연산자의 반환값

`&&`, `||` 연산자는 조건 평가 후 조건에 따라 값 자체를 반환한다.

### 예시

```js
let isActive = true;
// isActive = false;

// && 연산자는 첫 번째 피연산자가 참일 경우 두 번째 피연산자를 반환
let result1 = isActive && 'Success';

// || 연산자는 첫 번째 피연산자가 거짓일 경우 두 번째 피연산자를 반환
let result2 = isActive || 'Failure';

console.log(result1, result2);
```

> 위 예시에서 isActive가 참일 경우 result1은 'Success'가 되고, result2는 true가 된다. 반면, isActive가 거짓일 경우 result1은 false가 되고, result2는 'Failure'가 된다.

## `??` 연산자

`??`는 null 병합 연산자이다. 첫 번째 피연산자가 `null` 또는 `undefined`일 경우 두 번째 피연산자를 반환하고, 그렇지 않으면 첫 번째 피연산자를 반환한다.

- `0`, `false`, `NaN`, `""` 등 falsy한 값들은 예외다. 즉 첫 번째 피연산자를 반환한다. 

### 예시

```js
let a = null;
let b = 10;

let result = (a ?? b); // 10
```

> 위 예시에서 a는 null이므로 b의 값인 10을 반환한다.

### 활용 예시: 명확한 기본값 설정

```javascript
let count = 0;
let result = count ?? 42;
console.log(result); // 0
```

> `count`가 `null` 또는 `undefined`가 아니므로 count의 값 0을 반환한다.

## CJW vs ESM

> CJW(CommonJS)와 ESM(ES6 Modules)은 자바스크립트 모듈 시스템의 두 가지 주요 유형이다. 각각의 특징과 사용 사례를 통해 비교하자.

### CommonJS (CJW)

1. **역사와 배경**:
   
   - CommonJS는 Node.js의 기본 모듈 시스템이다. Node.js의 초창기부터 사용되어왔다.
   - 서버 사이드 자바스크립트 애플리케이션을 작성할 때 널리 사용된다.
   - 최근에는 덜 쓰는 방향이다.

2. **문법**:
   
   - `require`와 `module.exports`를 사용한다.
   
   - 예시:
     
     ```javascript
     // math.js 
     const add = (a, b) => a + b; 
     module.exports = { add }; 
     
     // app.js 
     const math = require('./math'); 
     console.log(math.add(2, 3)); // 5
     ```

3. **특징**:
   
   - 동기적 로딩: 모듈을 로드할 때 파일 시스템을 동기적으로 접근한다. 이는 서버 사이드 환경에서는 문제가 되지 않지만, 클라이언트 사이드에서는 성능 문제를 야기할 수 있다.
   - 순환 참조 지원: 모듈 간에 순환 참조가 발생해도 비교적 문제없이 동작한다.

### ES6 Modules (ESM)

1. **역사와 배경**:
   
   - ES6 모듈은 ECMAScript 2015(ES6)에서 도입되었으며, 표준 자바스크립트 모듈 시스템이다.
   - 브라우저와 서버 환경 모두에서 사용 가능하다.

2. **문법**:
   
   - `import`와 `export`를 사용한다.
   
   - 예시:
     
     ```javascript
     // math.js 
     export const add = (a, b) => a + b; 
     // app.js 
     import { add } from './math.js'; 
     console.log(add(2, 3)); // 5
     ```

3. **특징**:
   
   - 비동기적 로딩: 브라우저에서 모듈을 비동기적으로 로드하여 성능을 향상시킬 수 있다.
   - 정적 분석 가능: ES6 모듈은 정적으로 분석될 수 있어, 트리 쉐이킹(tree shaking)과 같은 최적화 기술에 유리하다.

### 사용 사례 비교

1. **서버 사이드(Node.js)**:
   
   - CommonJS가 기본 모듈 시스템으로 채택되어 있으며, 대부분의 Node.js 프로젝트에서 여전히 CommonJS를 사용한다.
   - ES6 모듈도 Node.js에서 사용할 수 있지만, 현재(2024년 기준)까지는 설정이 다소 복잡할 수 있다. 
   - ES6 모듈을 사용하려면 `package.json`에 `"type": "module"`을 추가해야 한다.

2. **클라이언트 사이드(브라우저)**:
   
   - ES6 모듈이 표준으로 자리 잡았다. `<script type="module">` 태그를 사용하여 모듈을 로드할 수 있다.
   - CommonJS는 브라우저에서 직접 지원되지 않기 때문에, 번들러(예: Webpack, Browserify)를 사용하여 ES6 모듈 형식으로 변환해야 한다.

3. **번들링**:
   
   - 대부분의 모던 프론트엔드 프로젝트는 Webpack이나 Rollup 같은 번들러를 사용하여 모듈을 번들링한다. 이 경우 ES6 모듈을 사용하는 것이 일반적이다.
   - CommonJS 모듈도 번들링이 가능하지만, ES6 모듈을 사용하는 것이 트리 쉐이킹 등 최적화 측면에서 유리하다.

### 결론

- CommonJS는 주로 Node.js 환경에서 사용되며, 기존의 많은 서버 사이드 코드베이스에서 볼 수 있다.
- ES6 모듈은 브라우저와 서버 모두에서 사용할 수 있으며, 최신 자바스크립트 프로젝트에서 권장된다.
- 번들러를 사용할 때는 ES6 모듈을 사용하는 것이 더 나은 선택이다. 이는 코드 최적화와 성능 측면에서 장점을 제공하기 때문이다.