
# TIL: AssemblyScript로 간단한 계산기 웹 애플리케이션 만들기

## 개요

WASM(웹어셈블리) 에 대해서 알아보는 도중  (`AssemblyScript`)[https://www.assemblyscript.org/compiler.html#compiler-options] 에 대해서 알게 되었다. 공식 문서의 예제를 사용해 간단한 계산기 웹 애플리케이션을 만들어 봤다. 꽤나 흥미로웠고 유익했다.

### AssemblyScript 특징
- TypeScript와의 유사성 :  AssemblyScript는 TypeScript의 문법을 거의 그대로 사용한다.
- WebAssembly의 성능 이점 : 저수준 접근: AssemblyScript는 WebAssembly의 성능 이점을 극대화하기 위해 설계되었다.
  -  이는 빠른 로드 시간과 낮은 메모리 사용을 가능하게 한다.
- 가비지 컬렉션 : 자동 가비지 컬렉션 기능도 제공한다.
  - 직접 메모리 관리에 신경 쓰지 않아도 되는 편리함을 제공
  - 그 결과, Rust, c/c++ 에 비해서 성능이 아쉽다.
- 타입 정의 : AssemblyScript는 강력한 타입 시스템을 가지고 있다.
  -  숫자 타입을 `Number` 가 아닌 `i32`, `i64`, `f64` 처럼 WASM 에 최적화 시켰다.
-  Node.js 지원: AssemblyScript는 Node.js 환경에서도 잘 동작한다.
   -  이는 서버 측에서 고성능 WebAssembly 모듈을 사용하려는 경우 확장성이 좋을 것이다.
-  제약 사항
   -  AssemblyScript는 WebAssembly의 기능을 최대한 활용하기 위해 설계되었지만, 일부 고수준의 JavaScript 기능이 지원되지 않음
   -  AssemblyScript는 아직 발전 중인 프로젝트이다. 일부 기능이 아직 완전히 안정적이지 않을 수 있으며, 성능 최적화나 새로운 기능이 추가될 여지가 있다.

## 과정
### 1. 프로젝트 초기 설정

AssemblyScript 를 시작하기 위해 먼저 Node.js와 npm이 설치되어 있어야 한다. 

프로젝트를 초기화하고(`npm init`), AssemblyScript 컴파일러를 개발 의존성으로 설치했다.(`npm install --save-dev assemblyscript`) 이후 `npx asinit .` 명령어를 통해 기본적인 프로젝트 구조를 생성했다.

```bash
npm init
npm install --save-dev assemblyscript
npx asinit .
```

이 명령어들을 실행하면, 다음과 같은 디렉토리 구조와 파일들이 생성된다:

- `./assembly`: AssemblyScript 소스 파일을 포함하는 디렉토리.
- `./build`: 컴파일된 WebAssembly 파일이 저장되는 디렉토리.
- `./asconfig.json`: 프로젝트 설정 파일.
- `./package.json`: npm 설정 파일.
- `./index.html`: WebAssembly 모듈을 로드하는 예제 HTML 파일.

### 2. AssemblyScript 코드 작성

- `assembly/index.ts` 파일에 기본적인 연산을 수행하는 함수를 작성했다. 덧셈, 뺄셈, 곱셈은 정수 타입인 `i32`를 사용하고, 나눗셈은 실수 타입인 `f64`를 사용하여 결과를 반환하도록 구현했다.
- `Typescript` 와 거의 유사하지만, 숫자 타입이 `Number` 가 아닌 `i32`, `i64`, `f64` 이다.

```typescript
export function add(a: i32, b: i32): i32 {
  return a + b;
}

export function subtract(a: i32, b: i32): i32 {
  return a - b;
}

export function multiply(a: i32, b: i32): i32 {
  return a * b;
}

export function divide(a: f64, b: f64): f64 {
  if (b == 0.0) {
    return 0.0;
  }
  const result = a / b;
  return result;
}
```

### 3. WebAssembly 모듈 빌드

- 그 다음으로 작성한 AssemblyScript 코드를 WebAssembly 모듈로 컴파일하기 위해 `npm run asbuild` 명령어를 실행했다. 
- 이 명령어를 통해 컴파일이 되는데, 대표적으로 `build/release.wasm` 파일이 생성되었는데, 바로 이것이 wasm 파일이다. 이걸 웹 애플리케이션에서 적용해서 사용한다.

```bash
npm run asbuild
```

### 4. HTML 파일 작성 및 WebAssembly 모듈 통합

- `index.html` 파일을 작성하여, JavaScript 모듈(`release.js`)을 로드하고 WebAssembly 함수를 호출하는 기능을 구현했다. 
- 이 웹 페이지는 사용자가 두 숫자를 입력하고, 덧셈, 뺄셈, 곱셈, 나눗셈을 선택하면 그 결과를 표시한다.
- `wasm` 를 곧바로 `html` 파일에 적용하지는 못하고 `js` 파일을 통해서 적용된다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AssemblyScript Calculator</title>
</head>
<body>
    <h1>AssemblyScript Calculator</h1>
    <input type="number" id="num1" placeholder="Number 1">
    <input type="number" id="num2" placeholder="Number 2">
    <br>
    <button onclick="calculate('add')">더하기</button>
    <button onclick="calculate('subtract')">빼기</button>
    <button onclick="calculate('multiply')">곱하기</button>
    <button onclick="calculate('divide')">나누기</button>
    <br>
    <h2>계산 결과: <span id="result">0</span></h2>

    <script type="module">
        import { add, subtract, multiply, divide } from './build/release.js';

        function calculate(operation) {
            const num1 = parseInt(document.getElementById('num1').value) || 0;
            const num2 = parseInt(document.getElementById('num2').value) || 0;

            let result;

            switch(operation) {
                case 'add':
                    result = add(num1, num2);
                    break;
                case 'subtract':
                    result = subtract(num1, num2);
                    break;
                case 'multiply':
                    result = multiply(num1, num2);
                    break;
                case 'divide':
                    result = divide(num1, num2);
                    break;
            }

            document.getElementById('result').innerText = result;
        }
        window.calculate = calculate;
    </script>
</body>
</html>
```

### 5. 결론
AssemblyScript를 사용해 WebAssembly 모듈을 컴파일하고, 이를 JavaScript와 함께 웹 애플리케이션에서 사용하는 방법을 익혔다. 웹어셈블리 찍먹으로 괜찮은 거 같다.
