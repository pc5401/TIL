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
