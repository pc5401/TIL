# 자바스크립트의 기본적인 사용

## 1강. 콘솔 활용하기

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

``` js
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
``` js
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
``` js
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