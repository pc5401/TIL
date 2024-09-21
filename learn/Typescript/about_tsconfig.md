## tsconfig.json 파일 생성

프로젝트 폴더에 `tsconfig.json` 파일을 생성하면, 이 파일을 통해 TypeScript 파일을 JavaScript 파일로 변환할 때의 세부 설정을 정의할 수 있다. 리액트나 뷰와 같은 프레임워크를 사용하는 경우 프로젝트 설치 시 설정할 수 있다.

### 예시

```json
// 예시
{
  "compilerOptions": {
    "target": "es5",
    "module": "commonjs"
  }
}
```

위와 같이 기본 설정을 작성한 후, 파일에 복사하여 붙여넣는다.

- **target**: TypeScript 파일을 변환할 JavaScript의 버전을 지정 가능.
    - 예: `es5`, `es2016`, `esnext`
- **module**: JavaScript 파일 간의 모듈 시스템을 지정.
    - 예: `commonjs` (require 문법), `es2015`, `esnext` (import 문법)

IE 호환성을 원할 경우 `target`을 `es5`, `module`을 `commonjs`로 설정하는 것이 일반적이다. 최신 JavaScript 기능을 사용하려면 `esnext` 등으로 설정해야 한다.

### 기타 compilerOptions 설정

추가로 설정할 수 있는 `compilerOptions` 항목들은 다음과 같다:

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "commonjs",
    "allowJs": true,
    "checkJs": true,
    "jsx": "preserve",
    "declaration": true,
    "outFile": "./",
    "outDir": "./",
    "rootDir": "./",
    "removeComments": true,
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "alwaysStrict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true}
}

```

### 주요 옵션 설명

| 옵션 | 설명 | 예시값 |
| --- | --- | --- |
| `target` | TypeScript를 변환할 JavaScript 버전 지정 | `"es5"`, `"es2015"`, `"esnext"` |
| `module` | 모듈 시스템 지정 | `"commonjs"`, `"amd"`, `"es2015"` |
| `allowJs` | JavaScript 파일을 TypeScript에서 import할 수 있는지 여부 설정 | `true`, `false` |
| `checkJs` | 일반 JavaScript 파일에서도 타입 검사 여부 설정 | `true`, `false` |
| `jsx` | TSX 파일을 JSX로 변환하는 방식 지정 | `"preserve"`, `"react"`, `"react-native"` |
| `declaration` | 컴파일 시 `.d.ts` 파일 자동 생성 여부 | `true`, `false` |
| `outFile` | 모든 TypeScript 파일을 하나의 JavaScript 파일로 컴파일 | `"./"` |
| `outDir` | JavaScript 파일의 출력 디렉토리 변경 | `"./dist"` |
| `rootDir` | 루트 디렉토리 설정 (출력 경로에 영향) | `"./src"` |
| `removeComments` | 컴파일 시 주석 제거 여부 | `true`, `false` |
| `strict` | 모든 엄격한 타입 검사 옵션 활성화 | `true`, `false` |
| `noImplicitAny` | 암시적 `any` 타입 사용 시 에러 발생 | `true`, `false` |
| `strictNullChecks` | `null` 및 `undefined` 타입에 대한 엄격한 검사 활성화 | `true`, `false` |
| `strictFunctionTypes` | 함수 매개변수 타입 검사 엄격화 | `true`, `false` |
| `strictPropertyInitialization` | 클래스 생성자에서 속성 초기화 강제 | `true`, `false` |
| `noImplicitThis` | `this`가 암시적으로 `any` 타입일 경우 에러 발생 | `true`, `false` |
| `alwaysStrict` | JavaScript `"use strict"` 모드 활성화 | `true`, `false` |
| `noUnusedLocals` | 사용하지 않는 지역 변수 있을 시 에러 발생 | `true`, `false` |
| `noUnusedParameters` | 사용하지 않는 매개변수 있을 시 에러 발생 | `true`, `false` |
| `noImplicitReturns` | 함수에서 모든 경로가 값을 반환하지 않을 경우 에러 발생 | `true`, `false` |
| `noFallthroughCasesInSwitch` | `switch` 문에서 `case`가 의도치 않게 빠져나갈 경우 에러 발생 | `true`, `false` |

전체 옵션에 대한 자세한 정보는 [TypeScript 공식 문서](https://www.typescriptlang.org/tsconfig)를 참고.