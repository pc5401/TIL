# you don't konw js

> 책 학습

## ch.1 자바스크립트

> 자바스크립트 역사 및 소소한 이야기

- ECMAScript 표준을 구현한 언어
- TC39 위원회가 사양 관리
- 브라우저와 Node.js 등 다양한 환경에서 동작
- 웹 환경이 핵심 축을 이룸
- Java와 직접적 관계 없음, 마케팅적 명명에서 비롯된 이름

#### 사양과 표준

- ECMAScript 표준(ES2019 등)에 따라 매년 언어가 개선
- 모든 주요 브라우저 및 JS 엔진은 이 표준을 따름
- 과거 JScript(IE용) 등 분리된 버전 존재했으나 현재는 사실상 단일 표준

#### 백워드 호환성(Backwards Compatibility)

- 기존에 유효했던 코드는 미래에도 동작하도록 함
- "웹을 깨지 않는다"는 원칙을 지킴
- 이는 언어 개선에 제약을 주지만, 안정적인 생태계 유지에 도움이 됨

#### 언어와 환경의 관계

- JS 자체에는 `alert()`나 `console.log()` 같은 API 정의 없음
- 브라우저 환경, Node.js 환경 등 각 환경은 JS 엔진 위에 자체 API를 제공
- 예: 브라우저는 `alert()`로 알림 상자를 띄울 수 있고, `fetch()`로 네트워크 요청 가능
- Node.js는 `fs` 모듈을 통해 파일 시스템 접근 등 환경별 특화 기능 제공

```js
// 브라우저 환경 전용 예시 (표준 JS 아님)
alert("Hello, JS!");
console.log("이 출력은 콘솔이라는 환경 API를 활용한 것");
```

#### 개발자 도구 콘솔 주의점

- 브라우저 개발자 콘솔은 순수 JS 환경이 아닌, 개발 편의를 위한 도구
- 콘솔에서 가능한 문법·기능이 실제 JS 파일 실행 시와 다를 수 있음
- 콘솔 상 동작 결과를 언어 사양과 완전히 동일하다고 가정하지 말 것

#### 다중 패러다임 지원

- 절차적, 객체 지향, 함수형 프로그래밍 모두 가능
- 특정 패러다임에 갇히지 않고 자유롭게 스타일 혼용 가능

#### 새로운 기능 도입과 호환성 이슈

- 새로운 문법이나 API는 구형 환경에서 동작하지 않을 수 있음
- 이런 문제 해결을 위해 트랜스파일링(Transpiling)과 폴리필(Polyfill)을 활용

```js
// 최신 문법(let) 사용 예
// 구형 환경 지원을 위해 Babel 같은 트랜스파일러로 변환 가능
if (condition) {
    let x = 3;
    console.log(x);
} else {
    let x = 4;
    console.log(x);
}
```

```js
// 새로운 API(Promise.prototype.finally) 폴리필 예시
if (!Promise.prototype.finally) {
    Promise.prototype.finally = function(onFinally) {
        return this.then(
            value => Promise.resolve(onFinally()).then(() => value),
            reason => Promise.resolve(onFinally()).then(() => { throw reason; })
        );
    };
}
```

#### JS의 실행 방식

- JS는 파싱 후 AST(Abstract Syntax Tree) 생성, 이후 내부적으로 컴파일 단계를 거침
- JIT(Just-In-Time) 최적화를 통해 성능 향상
- 형식상 인터프리터처럼 보이나 실제로는 컴파일 과정을 포함하는 하이브리드 접근

#### WebAssembly(WASM)

- JS 엔진 위에서 동작하는 이진 형태의 코드 실행 방식
- C/C++ 같은 언어를 웹에서 고성능으로 돌리기 위한 수단
- JS를 대체하는 것이 아닌 보완적 존재

#### 엄격 모드(Strict Mode)

- ES5에서 도입된 "use strict"를 통해 보다 엄격한 규칙 적용
- 실수나 애매한 문법 사용을 사전에 차단하여 더 안전하고 최적화된 코드 작성 유도
- ES6 모듈 사용 시 자동으로 엄격 모드 적용

```js
"use strict";

function test() {
    // 중복 매개변수나 암묵적 전역 변수 선언 등 금지
    let a = 1;
    // let a = 2; // 오류 발생
    return a;
}
```

#### 정리

- JS는 단일 표준을 기반으로 하는 다중 패러다임 언어
- 웹 중심의 호환성·백워드 호환성 원칙 유지
- 트랜스파일링, 폴리필 등으로 최신 기능 적극 활용 가능
- 환경별 API 제공으로 다양한 플랫폼 지원
- 엄격 모드와 컴파일 단계를 통해 안정적이고 최적화된 코드 작성 가능하다.


### ch.2 자바스크립트 조망하기

#### 개요

JS 학습의 핵심은 코드를 직접 작성하면서 언어의 동작 방식을 이해하는 것  
2장은 JS 언어 요소들을 개괄적으로 살펴보는 장이며, 이후 심화 학습을 위한 토대 구축이 목적  
단순 문법 나열이 아닌 개념적 지형 파악에 초점

#### 각 파일이 하나의 프로그램

- 전통적 상황에서 `.js` 파일 하나가 하나의 독립된 프로그램으로 취급된다
- 여러 파일을 로드해도 각 파일은 개별 프로그램으로 파싱 및 실행된다
- 하나의 애플리케이션은 다양한 JS 파일(프로그램)을 전역 범위(global scope)에서 상호 작용시키거나, ES6 모듈 방식을 통해 서로 import/export하며 협업한다

#### 값(Values)

- JS의 정보 기본 단위는 값(Value)
- 원시값(primitive)과 객체(object)로 구분된다
- 원시값: string, number, boolean, undefined, null, symbol, bigint
- 문자열은 `" "`나 `' '`로 묶으며, `` ` ` `` 백틱을 사용하면 `${변수}` 형식으로 값 삽입(인터폴레이션) 가능
- ```js
  let firstName = "Kyle";
  console.log(`My name is ${ firstName }.`);
  
  ```

- 숫자는 정수, 실수, 큰 정수(bigint) 등 표현 가능
- boolean은 `true` / `false`로 논리값 표현
- `null` 과 `undefined`는 "값 없음"을 나타내는 특수한 값
- symbol은 주로 내부적, 또는 고유한 키로 객체에 활용

#### 배열(Array)와 객체(Object)

- 배열: 순서가 있으며 인덱스로 접근하는 객체 형태
- ```js
  let names = [ "Frank", "Kyle", "Susan" ];
  console.log(names[1]); // "Kyle"
  
  ```

- 객체: 키-값 쌍의 집합, 순서 없음
- ```js
  let me = {
    first: "Kyle",
    last: "Simpson",
    age: 39
  };
  console.log(me.first); // "Kyle"
  
  ```

- typeof 연산자로 타입 확인
- ```js
  typeof 42; // "number"
  typeof "abc"; // "string"
  typeof null; // "object" (버그성 반환)
  typeof [1,2,3]; // "object"
  typeof function(){}; // "function" (특수 반환)
  ```



#### 변수 선언

- `var`, `let`, `const` 키워드로 변수 선언
- `var`는 함수 범위(function scope), `let`과 `const`는 블록 범위(block scope)
- `const`는 재할당 불가. 단, 객체 참조 값은 바뀌지 않지만 내부 변경 가능
- 파라미터나 `catch` 등의 구문에서도 변수 선언 발생

```js
var myName = "Kyle";
let age = 39;
const isBirthday = true;

if (isBirthday) {
  age = age + 1;
  // isBirthday = false; // 에러 발생 (const 재할당 불가)
}

```

#### 함수 (Function)

- 코드의 재사용 가능한 블록
- 입력(파라미터)을 받고, 처리 후 결과를 `return`으로 반환 가능
- 함수는 값이며, 변수나 객체 프로퍼티로 할당 가능
- 함수 선언: `function fnName(){}`
- 함수 표현식: `var fn = function(){};`
- 객체 메서드로도 정의 가능

```js
function greeting(myName) {
  return `Hello, ${myName}!`;
}

let msg = greeting("Kyle");
console.log(msg); // "Hello, Kyle!"

```



#### 비교 연산

- `===`는 엄격 비교이지만 `NaN`과 `-0`에 대해 특수 동작: `NaN === NaN`은 false, `0 === -0`은 true
- `Object.is()`를 통해 이러한 특수 케이스 제대로 비교 가능
- `==`는 타입이 다르면 강제 변환(coercion) 수행 후 비교
- 대소 비교 `<`, `>` 등도 타입 다르면 숫자로 변환하여 비교
- 객체 비교 시 참조 동일성(identity)을 비교하고, 구조적 동등성은 기본적으로 지원하지 않음

```js
42 === "42"; // false
42 == "42"; // true, "42"가 숫자로 변환되어 비교
Object.is(NaN, NaN); // true
Object.is(0, -0); // false
```



#### 클래스(Class)

- 데이터와 동작을 하나로 묶는 전통적 객체지향 패턴
- `class` 키워드로 정의하며 `new`로 인스턴스 생성
- `extends`를 통한 상속(inheritance)과 `super`를 통한 부모 클래스 메서드 호출 가능

```js
class Publication {
  constructor(title, author, pubDate) {
    this.title = title;
    this.author = author;
    this.pubDate = pubDate;
  }
  print() {
    console.log(`${this.title} by ${this.author} on ${this.pubDate}`);
  }
}

class Book extends Publication {
  constructor(details) {
    super(details.title, details.author, details.publishedOn);
    this.publisher = details.publisher;
  }
  print() {
    super.print();
    console.log(`Publisher: ${this.publisher}`);
  }
}

let myBook = new Book({
  title: "You Don't Know JS",
  author: "Kyle Simpson",
  publishedOn: "June 2014",
  publisher: "O'Reilly"
});
myBook.print();

```



#### 모듈(Module)

- 모듈은 데이터와 기능을 묶고 외부에 명시적으로 export하여 재사용하는 패턴
- 전통적 방식: 함수로 감싸고 반환 객체로 public API 제공(클래식 모듈 패턴)
- ES 모듈(ESM): 파일 단위의 모듈, `import` / `export` 구문 사용
- ESM은 싱글 인스턴스. 필요한 경우 모듈에서 팩토리 함수 제공하여 다중 인스턴스 생성 가능

```js
// publication.js
export function create(title,author,pubDate) {
  return {
    print() {
      console.log(`${title} by ${author} on ${pubDate}`);
    }
  };
}

// blogpost.js
import { create as createPub } from "./publication.js";
export function create(title, author, pubDate, URL) {
  let pub = createPub(title, author, pubDate);
  return {
    print() {
      pub.print();
      console.log(URL);
    }
  };
}

// main.js
import { create as newBlogPost } from "./blogpost.js";
let post = newBlogPost("Title", "Kyle", "Today", "http://example.com");
post.print();

```

#### 정리

- 2장은 JS 언어 요소를 폭넓게 살펴보는 개괄적 여정이었다.
- 각 파일 단위 프로그램 인식, 원시값/객체, 변수 스코프, 함수, 비교, 클래스와 모듈 패턴까지 두루 훑음
- 이후 심층적 학습 이전에 이 개념들을 재차 검토하고 익숙해지는 과정 필요
- 모듈, 클래스, 비교 연산, 스코프 등 핵심 기초를 바탕으로 이후 내용을 더욱 깊이 이해할 수 있음

## ch.3 자바스크립트 뿌리 파헤치기

### 개요

JS 이해를 심화하기 위해 언어의 근본적 작동 원리를 살펴본다.

단순 문법 외에, 이터레이션(반복), 클로저(closure), this, 프로토타입 등 핵심 뿌리 개념 다루기

이해가 어려울 수 있으므로 여유를 가지고 반복 숙지 권장

### 이터레이션(Iteration) 패턴

- 데이터를 한 번에 다루는 대신, 한 요소씩 순차적으로 처리하는 표준화된 접근 방식
- ES6 이후 표준 이터레이션 프로토콜 도입
- `next()` 메서드를 통해 `value`와 `done`을 가진 이터레이터 결과 반환
- `for..of` 문, 스프레드(`...`) 문법 등을 사용해 이터레이터 소비(consume) 가능

```
for (let val of iterable) {
  console.log(val);
}

let arr = [...iterable]; // 이터러블을 배열로 복사
```

### 이터러블(Iterable)과 이터레이터(Iterator)

- 이터러블: 반복 가능한 값, 예: 문자열, 배열, Map, Set 등
- 이터러블은 `for..of`나 스프레드 문법으로 쉽고 직관적으로 순회 가능
- `arr.entries()`나 `map.values()`와 같은 메서드로 특정 키나 값, 엔트리만 추출 가능
- 사용자 정의 자료구조도 이터레이션 프로토콜을 구현하면 동일한 방식으로 순회 가능

### 클로저(Closure)

- 함수가 자신의 외부 스코프 변수를 참조하고 그 참조를 유지하는 능력
- 함수가 정의된 스코프 밖에서 실행되더라도, 원래 스코프 변수 접근 가능
- 비동기 콜백, 이벤트 핸들러 등에서 자주 활용
- 값이 아닌 변수를 기억하기 때문에, 변수 값 변화도 반영

```
function counter(step=1) {
  let count = 0;
  return function() {
    count += step;
    return count;
  };
}

let inc = counter();
inc(); // 1
inc(); // 2
```

### this 키워드

- 함수의 실행 컨텍스트(context)와 관련
- 함수가 어떻게 호출되었는지에 따라 `this`가 동적으로 결정
- 객체 메서드로 호출하면 그 객체를 this로, `call()` 또는 `apply()`로 호출하면 지정한 객체를 this로 사용
- 스코프와 달리 this는 정의 시점이 아닌 호출 시점에 결정
- 유연한 재사용성을 제공

```
function study() {
  console.log(`Study ${this.topic}`);
}
let obj = { topic: "JS", study };
obj.study(); // "Study JS"
```

### 프로토타입(Prototype)

- 객체간 링크를 통해 속성/메서드 상호 위임(delegate)하는 메커니즘
- `Object.create()`를 이용하여 특정 객체를 프로토타입으로 하는 새 객체 생성 가능
- 프로토타입 체인에서 속성 탐색 시 해당 객체에 없으면 상위 프로토타입 객체로 거슬러 올라가 검색
- this와 결합하면 상속(또는 델리게이션)된 메서드를 다른 객체에서도 재사용 가능

```
let base = { study() { console.log(`Study ${this.topic}`); } };
let jsObj = Object.create(base);
jsObj.topic = "JS";
jsObj.study(); // "Study JS"
```

### 왜(Why?) 질문하기

- JS에는 표면 뒤에 많은 메커니즘 존재
- 이터레이션, 클로저, this, 프로토타입 등 근본적인 작동 원리를 이해하면 언어 활용 능력 향상
- 충분히 소화하지 못한 부분은 질문과 탐구 지속 필요
- 다음 장에서 JS를 더 구체적으로 나누어 다루며, 본 시리즈의 다른 책들에서 심층 이해 가능

##  ch.4 더 큰 그림
> part 1의 마지막 4장은 이후 part에 대한 설명이다.

JS 언어가 크게 3가지 축(스코프/클로저, 프로토타입, 타입/강제변환)으로 나뉘어 있음
나아가 시리즈 전체의 학습 순서와 방향성에 대해 조언한다.

### 세 가지 핵심 개념

1. **스코프와 클로저(Scope & Closure)**
    - 변수와 스코프 구조는 모든 프로그래밍 언어에서 핵심적 요소
    - JS는 렉시컬 스코프 기반
    - var, let, const, TDZ(Temporal Dead Zone) 등 JS 특유의 스코프 동작을 정확히 이해해야 함
    - 클로저는 함수가 외부 스코프 변수를 참조하고 유지하는 현상으로, 모듈 등 중요 패턴의 근간
    
2. **프로토타입(Prototypes)**
    - JS는 객체를 클래스 없이 직접 만들고 연결할 수 있는 독특한 언어
    - 프로토타입 체인을 통한 객체 간 위임(delegation)은 JS 고유의 강력한 특징
    - 클래스 문법도 프로토타입 위에 쌓인 추상화일 뿐, 클래스 외에도 프로토타입을 활용하는 다양한 패턴(행위 위임) 고려 가능
    
3. **타입과 강제 변환(Types & Coercion)**
    - 대부분의 개발자가 JS 타입 시스템에 대한 오해나 피상적 이해를 갖고 있음
    - 타입 변환, 암묵적 강제 변환(coercion)을 정확히 이해하면 더 견고한 코드 작성 가능
    - TypeScript나 Flow 같은 정적 타입 도구를 쓰더라도, JS 타입 작동 원리를 알아야 최대 효용
    

### JS를 대하는 태도

- 군중심리나 기존 관행을 무비판적으로 따르기보다, JS 고유의 "결"(grain)을 이해하고 활용하자.
- 스펙에 기반한 사실(팩트)와 저자의 의견(옵니언)을 구분하고, 자신의 의견으로 소화한 뒤 필요 시 논리적으로 방어할 수 있어야 함.
- JS 고유 패턴과 문법적 특성을 수용하고, 자신의 팀 문화나 기존 코드베이스와 조화롭게 점진적 개선 추구

## APPENDIX A 더 멀리 나가기
### 1. 값(Values) vs. 참조(References)

- **원시값(Primitives)**: 문자열, 숫자 등은 복사(copy)되어 전달
    
    ```jsx
    let myName = "Kyle";
    let yourName = myName; // 별도의 "Kyle" 생성
    myName = "Frank";
    console.log(yourName); // "Kyle" (영향 없음)
    ```
    
- **객체값(Objects)**: 배열, 객체, 함수 등은 참조(reference)로 전달
    
    ```jsx
    let myAddress = { street: "123 JS Blvd" };
    let yourAddress = myAddress; // 참조 복사
    myAddress.street = "456 TS Ave";
    console.log(yourAddress.street); // "456 TS Ave"
    ```
    
- JS는 값의 종류(원시 vs. 객체)에 따라 자동으로 복사/참조 여부 결정

### 2. 다양한 함수 정의 방식 (So Many Function Forms)

- **익명 함수 표현식(Anonymous Function Expression)**
    
    ```jsx
    let fn = function(x) { return x * 2; };
    ```
    
    - 할당 시 `fn.name`은 `"fn"`으로 추론되지만 실제 식별자는 없음
- **명명된 함수 표현식(Named Function Expression)**
    
    ```jsx
    let fn = function double(x) { return x * 2; };
    ```
    
    - 함수 내부에서 `double()`로 재귀 호출, 디버깅 시 추적 가능
- **다양한 선언/표현식**: 제너레이터(`function *`), async 함수(`async function`), 클래스 메서드, 화살표 함수(`=>`), IIFE 등
- 화살표 함수(`=>`)는 **항상 익명**이며, `this`를 렉시컬 스코프로 바인딩

### 3. 조건문에서의 강제 변환(Coercive Conditional Comparison)

- `if (x) {...}` 등 조건식은 내부적으로 `Boolean(x)`로 강제 변환 후 판단
    
    ```jsx
    let x = "hello";
    if (x) { /* "hello" -> true로 변환, 블록 실행 */ }
    ```
    
- `== true`와 `if(x)`는 동일하지 않음. 후자는 `Boolean(x)` 로 처리
- JS에서 `if`, `while`, `for` 등 제어문의 조건은 항상 **부울(boolean) 변환**이 일어남

### 4. 프로토타입 "클래스"(Prototypal "Classes")

- ES6 이전에 **생성자 함수**와 `prototype` 객체로 사실상 ‘클래스 흉내’를 내던 방식
    
    ```jsx
    function Classroom() {}
    Classroom.prototype.welcome = function() {
      console.log("Welcome!");
    };
    let mathClass = new Classroom();
    mathClass.welcome(); // "Welcome!"
    ```
    
- 현재는 ES6의 `class` 문법이 권장됨
    
    ```jsx
    class Classroom {
      welcome() {
        console.log("Welcome!");
      }
    }
    let mathClass = new Classroom();
    mathClass.welcome(); // "Welcome!"
    ```
    
- 프로토타입 체인 자체는 동일하나, 클래스 문법이 더 명확하고 직관적임