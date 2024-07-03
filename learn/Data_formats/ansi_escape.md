# ANSI 이스케이프 시퀀스 표준

위키피디아 참고 : [ANSI escape code - Wikipedia](https://en.wikipedia.org/wiki/ANSI_escape_code)

-  초기에는 표준이 정해지지 않아 터미널을 설계하는 회사마다 동작이 달랐다.
  
- 터미널이 가져야 할 기본적인 동작들을 모아 **ANSI 이스케이프 시퀀스 표준**이 탄생한다.
  
- **ANSI 이스케이프 시퀀스 표준**를 이용하면 **삭막한 터미널**에 활력을 불어넣을 수 있다!
  

## 이스케이프 시퀀스 구조

- `\033` : 이스케이프 시퀀스를 시작한다.
- `[` : 색상을 지정하는 부분이다.
- `33` : 전경색을 노란색으로 설정한다.
- `m` : 설정의 끝을 나타낸다.

예를 들어, `\033[33m`은 텍스트 색상을 노란색으로 설정하고, `\033[39m`은 색상을 터미널 기본값으로 되돌린다.

```js
console.log('\033[33m Hello World \033[39m'); // Hello World(노랑색)
```

### ANSI 이스케이프 코드 모음

편리하게 사용하기 위해 ANSI 이스케이프 코드를 JavaScript 객체로 정리하였다:

```js
const ansiEscapes = {
  reset: "\x1b[0m", // 모든 스타일을 초기화
  bright: "\x1b[1m", // 굵게
  dim: "\x1b[2m", // 희미하게
  underscore: "\x1b[4m", // 밑줄
  blink: "\x1b[5m", //깜박임
  reverse: "\x1b[7m", // 반전
  hidden: "\x1b[8m", // 숨김

  fg: { // 텍스트 컬러
    black: "\x1b[30m",
    red: "\x1b[31m",
    green: "\x1b[32m",
    yellow: "\x1b[33m",
    blue: "\x1b[34m",
    magenta: "\x1b[35m",
    cyan: "\x1b[36m",
    white: "\x1b[37m",
    crimson: "\x1b[38m"
  },

  bg: { // 배경 컬러
    black: "\x1b[40m",
    red: "\x1b[41m",
    green: "\x1b[42m",
    yellow: "\x1b[43m",
    blue: "\x1b[44m",
    magenta: "\x1b[45m",
    cyan: "\x1b[46m",
    white: "\x1b[47m",
    crimson: "\x1b[48m"
  }
};
```

#### 사용 예시

1. **텍스트 색상 설정**: 노란색 텍스트
  
  ```js
  console.log(${ansiEscapes.fg.yellow}Hello World${ansiEscapes.reset});
  ```
  
2. **배경색 설정**:
  
  ```js
  console.log(${ansiEscapes.bg.blue}${ansiEscapes.fg.white}Hello World${ansiEscapes.reset});
  ```
  
3. **텍스트 스타일 설정**:
  
  ```js
  console.log(${ansiEscapes.bright}Bold Text${ansiEscapes.reset}); // 굵은 텍스트
  console.log(${ansiEscapes.underscore}Underlined Text${ansiEscapes.reset}); // 밑줄 텍스트
  console.log(${ansiEscapes.reverse}Reversed Colors Text${ansiEscapes.reset}); // 반전된 색상
  ```
  
  ANSI 이스케이프 코드를 직접 사용하면 쉽게 이해가 간다.