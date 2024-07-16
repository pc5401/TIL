# JSDoc 기본
## JSDoc 주석의 기본 구조
JSDoc 주석은 주석 시작과 끝을 구분하는 특수한 주석 기호 /** ... */ 사이에 작성된다. 주석은 여러 개의 태그를 포함할 수 있으며, 각 태그는 특정 정보를 제공한다.

```js
/**
 * 설명
 * @태그 {타입} 이름 설명
 */
```

## 주요 태그
### @param
함수의 매개변수를 설명하는 데 사용한다.

```javascript
/**
 * 두 수를 더하다.
 * @param {number} a 첫 번째 수
 * @param {number} b 두 번째 수
 * @returns {number} 두 수의 합
 */
function add(a, b) {
  return a + b;
}
```

### @returns
함수의 반환 값을 설명하는 데 사용한다.

```javascript
/**
 * 문자열의 길이를 반환하다.
 * @param {string} str 문자열
 * @returns {number} 문자열의 길이
 */
function getStringLength(str) {
  return str.length;
}
```
### @typedef
커스텀 타입을 정의하는 데 사용한다.

```javascript
/**
 * 사용자 객체
 * @typedef {Object} User
 * @property {string} name 이름
 * @property {number} age 나이
 */

/**
 * 사용자 객체를 반환하다.
 * @returns {User} 사용자 객체
 */
function getUser() {
  return {
    name: 'John Doe',
    age: 30
  };
}
```

### @example
예제 코드를 제공하는 데 사용한다.

```javascript
/**
 * 두 수를 곱하다.
 * @param {number} a 첫 번째 수
 * @param {number} b 두 번째 수
 * @returns {number} 두 수의 곱
 * @example
 * // 2와 3을 곱하다.
 * const result = multiply(2, 3);
 * console.log(result); // 6
 */
function multiply(a, b) {
  return a * b;
}
```
### @deprecated
더 이상 사용되지 않는 함수나 변수를 표시하는 데 사용한다.

``` javascript
/**
 * @deprecated use subtractNew instead.
 * 두 수를 빼다.
 * @param {number} a 첫 번째 수
 * @param {number} b 두 번째 수
 * @returns {number} 두 수의 차
 */
function subtract(a, b) {
  return a - b;
}
``` 

## 클래스 문서화
JSDoc은 클래스와 클래스 멤버를 문서화하는 데에도 사용할 수 있다.

```javascript
/**
 * 사람을 나타내는 클래스이다.
 */
class Person {
  /**
   * 사람 객체를 생성하다.
   * @param {string} name 이름
   * @param {number} age 나이
   */
  constructor(name, age) {
    /**
     * @property {string} name - 이름
     */
    this.name = name;
    /**
     * @property {number} age - 나이
     */
    this.age = age;
  }

  /**
   * 나이를 한 살 더 먹다.
   * @returns {number} 증가된 나이
   */
  haveBirthday() {
    this.age += 1;
    return this.age;
  }
}
```

## 모듈 문서화
ES6 모듈을 문서화하는 방법이다.

```
코드 복사
/**
 * 유틸리티 함수 모듈이다.
 * @module utils
 */

/**
 * 두 수를 더하다.
 * @param {number} a 첫 번째 수
 * @param {number} b 두 번째 수
 * @returns {number} 두 수의 합
 */
export function add(a, b) {
  return a + b;
}
```