# 전처리기(Preprocessor) - Sass, Less, Stylus

CSS 전처리기는 코드를 더 **유지보수하기 쉽고 재사용성** 있게 작성하도록 도와주는 툴이다.

주요 기능으로 **변수(variables)**, **중첩(nesting)**, **믹스인(mixins)**, **함수(functions)** 등이 있으며,

이는 **반복**을 줄이고 **구조적**으로 코드를 관리할 수 있게 해준다.

대표적인 전처리기:

1. **Sass(SCSS)**
2. **Less**
3. **Stylus**

---

## 공통적인 장점

- **변수**: 색상, 폰트 크기 등 자주 사용되는 값을 변수로 관리
- **중첩**: 선택자를 중첩해 코드를 계층적으로 표현 (CSS의 계층 구조를 반영)
- **믹스인(mixin)**: 반복되는 코드 조각을 재사용할 수 있는 개념
- **함수/연산**: 색상 연산, 수치 계산 등 프로그래밍적 로직 활용
- **임포트**: 여러 파일로 분리해 모듈화하고, 최종 빌드시 하나의 CSS로 합침
- 결국 **코드 가독성**, **생산성**, **유지보수성**을 향상

---

## 1) Sass(SCSS)

- **Sass**는 “Syntactically Awesome Style Sheets”의 약자
- 두 가지 문법:
    1. **`.sass`** (중괄호와 세미콜론 없이, 들여쓰기 기반)
    2. **`.scss`** (CSS와 유사한 문법, 중괄호와 세미콜론 사용)
- 가장 인기 있고, 많은 라이브러리(Compass 등)가 Sass 기반으로 제공

### 기본 예시 (SCSS 문법)

```scss
$primary-color: #3498db;  // 변수 정의

body {
  font-family: "Helvetica", sans-serif;
  background-color: $primary-color;

  // 중첩
  header {
    padding: 10px;
    h1 {
      color: white;
    }
  }
}

// 믹스인
@mixin center-flex {
  display: flex;
  justify-content: center;
  align-items: center;
}

// 사용(include)
.container {
  @include center-flex;
  height: 200px;
  background-color: darken($primary-color, 10%);
}
```

- *변수 `$primary-color`*로 배경색 관리
- **중첩**으로 구조화 (`header h1` 부분 등)
- *`@mixin`*과 **`@include`*로 재사용 (flexbox 센터 정렬)
- 색상 함수 `darken()`로 색상 어둡게 변환

Sass/SCSS 파일(`.scss`)을 빌드하면 **일반 CSS**로 변환된 파일(`.css`)이 생성된다.

---

## 2) Less

- “Leaner CSS”의 약자로, Sass와 유사한 전처리기
- **JavaScript 기반**으로 동작하며, Node.js 환경 또는 브라우저에서도 실시간 변환 가능
- 변수 선언 시 `@`를 사용

### 기본 예시

```less
@primary-color: #3498db;

body {
  font-family: "Helvetica", sans-serif;
  background-color: @primary-color;

  header {
    padding: 10px;
    h1 {
      color: white;
    }
  }
}

// 믹스인
.center-flex() {
  display: flex;
  justify-content: center;
  align-items: center;
}

// 사용
.container {
  .center-flex();
  height: 200px;
  background-color: darken(@primary-color, 10%);
}
```

- Less 역시 **중첩**, **변수**, **믹스인**을 지원
- 함수 형태는 Less 기본 제공 또는 플러그인 통해 확장 가능
- Less는 **JS로 컴파일**이 가능해, 브라우저에서 `<link rel="stylesheet/less" ...>`로 실시간 변환하는 방식도 있었다(프로덕션에서는 미리 컴파일된 CSS를 사용 권장).

---

## 3) Stylus

- 매우 **유연한 문법**을 가진 전처리기. 세미콜론, 중괄호조차도 선택적으로 사용 가능
- Node.js 기반으로 동작
- 다른 전처리기들과 유사하게 **변수**, **중첩**, **믹스인**, **함수** 등을 지원

### 기본 예시 (중괄호와 콜론 생략한 문법)

```
primary-color = #3498db

body
  font-family "Helvetica", sans-serif
  background-color primary-color

  header
    padding 10px
    h1
      color white

// 믹스인
center-flex()
  display flex
  justify-content center
  align-items center

.container
  center-flex()
  height 200px
  background-color darken(primary-color, 10%)
```

- 탭이나 공백 들여쓰기를 통해 **구조**를 나타냄
- `=`로 변수 선언, 함수 호출시 `()` 가능
- 다양한 **단축 문법**을 제공 (만약 CSS와 유사하게 중괄호, 세미콜론을 쓰고 싶다면 쓸 수도 있음)