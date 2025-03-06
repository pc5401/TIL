# 타이포그래피(Typography)와 폰트(Font)

웹 디자인에서 **글자**는 정보 전달의 핵심 요소이다. 좋은 타이포그래피는 가독성과 접근성을 높여 **사용자 경험**을 개선한다.

---

## 폰트 관련 주요 속성

### 1) `font-family`

글꼴(폰트) 종류를 지정한다.

웹 안전 폰트나, 웹 폰트 등을 사용할 수 있으며, 우선순위를 고려해 **쉼표로 나열**하는 습관이 중요하다.

```css
p {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

- **웹 안전 폰트**(Arial, Verdana, Times New Roman 등)는 모든 환경에서 대체로 지원됨
- 사용자 지정 폰트(웹 폰트)는 로딩을 위해 추가 설정이 필요 (`@font-face` 또는 Google Fonts 등)

### 2) `font-size`

글자 크기를 지정한다.

절대 단위(px)보다 **상대 단위(rem, em 등)**를 선호하는 편이 많다.

접근성과 반응형 디자인 측면에서도 유리하기 때문.

```css
p {
  font-size: 1rem; /* 예: HTML 루트(font-size: 16px) 기준 -> 16px */
}
```

- **절대 크기**(px)는 고정된 크기
- **상대 크기**(em, rem, %)는 상위(또는 루트) 폰트 크기를 기준으로 변경됨

### 3) `font-weight`

글자의 굵기를 지정한다.

`normal`, `bold`, 혹은 **숫자(100~900)**로 세분화할 수도 있다.

```css
strong {
  font-weight: 700; /* 보통 bold와 동일하게 사용됨 */
}

```
### 4) `font-style`

이탤릭(italic) 또는 일반(normal) 스타일을 지정한다.

```css
em {
  font-style: italic;
}
```

### 5) `line-height`

줄간격(행간)을 조절한다. 가독성을 위해 **1.4~1.6** 정도가 보통 많이 쓰인다.

```css
p {
  line-height: 1.5;
}
```

- 숫자(배수)로 설정하는 것이 일반적이며, px나 em 등으로도 설정 가능
- 여러 요소에 공통 적용 시 일관성 유지에 좋음

### 6) `letter-spacing`

글자 사이의 간격(자간)을 조절한다.

`word-spacing`으로 단어 사이 간격도 변경 가능하다.

```css
.title {
  letter-spacing: 0.05em;
}
```

---

## 텍스트 정렬 및 장식

### 1) `text-align`

수평 정렬을 결정한다.

`left`, `right`, `center`, `justify` 등이 있다.

```css
h1 {
  text-align: center;
}
```

### 2) `text-decoration`

글자에 밑줄, 취소선, 윗줄 등을 표시한다.

`none`, `underline`, `line-through`, `overline` 등이 있다.

```css
a {
  text-decoration: none;
}
```

### 3) `text-transform`

글자를 대문자·소문자 등으로 변환한다.

`uppercase`, `lowercase`, `capitalize` 등이 있다.

```css
.uppercase-text {
  text-transform: uppercase;
}
```
### 4) `white-space`

여백(공백, 줄바꿈 등)을 어떻게 처리할지 결정한다.

`normal`, `pre`, `nowrap`, `pre-wrap`, `pre-line` 등을 통해, HTML의 공백을 유지하거나 줄바꿈 처리를 제어한다.

```css
.pre-line {
  white-space: pre-line;
}
```

---

## 웹 폰트(Web Fonts) 사용

### 1) `@font-face`

원하는 폰트를 직접 호스팅하고 사용할 수 있다.

폰트 파일(.woff, .woff2, .ttf 등)을 프로젝트에 포함해야 한다.

```css
@font-face {
  font-family: "MyCustomFont";
  src: url("/fonts/MyCustomFont.woff2") format("woff2"),
       url("/fonts/MyCustomFont.woff") format("woff");
  font-weight: 400;
  font-style: normal;
}

body {
  font-family: "MyCustomFont", sans-serif;
}
```

### 2) Google Fonts 등 외부 서비스

`<link>` 태그로 외부 스타일을 불러와 간단히 웹 폰트를 적용할 수 있다.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" />
```

```css
body {
  font-family: "Noto Sans KR", sans-serif;
}
```

- 외부에 의존하므로 인터넷 연결 상태나 폰트 로딩 지연을 고려해야 한다.
- 크로스 브라우징 이슈는 대개 해결되어 있지만, 폰트 라이센스를 반드시 확인해야 한다.

---

## 최적의 타이포그래피 구성 팁

1. **일관성**:
    - 전체 문서에서 `font-family`, `font-size`, `line-height` 등 기본 설정을 통일하면 가독성이 높아진다.
2. **적절한 대비(Contrast)**:
    - 헤드라인과 본문의 크기·굵기 차이를 두어 구조를 명확히 한다.
3. **배색(색상)**:
    - 텍스트 색과 배경 색 간 충분한 명도 대비를 유지해 시인성 확보 (WCAG 기준 준수)
4. **반응형**:
    - 모바일, 태블릿, 데스크톱 등 각 뷰포트에 맞춰 유연하게 글자 크기와 줄간격을 조절한다.
5. **로드 성능**:
    - 과도한 폰트 파일(굵기·스타일별 다수)은 페이지 로딩에 영향을 준다. 필요한 폰트만 선택 사용.

---

## 예시 코드

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    /* 전역으로 기본 타이포 세팅 */
    html {
      font-size: 16px; /* 루트 폰트 크기 */
    }
    body {
      font-family: "Helvetica Neue", Arial, sans-serif;
      line-height: 1.6;
      color: #333;
      margin: 20px;
    }

    /* 제목 스타일 */
    h1, h2, h3 {
      font-weight: bold;
      margin: 1rem 0 0.5rem;
    }

    /* 본문 스타일 */
    p {
      margin-bottom: 1rem;
    }

    .highlight {
      font-weight: 700;
      color: #c0392b;
    }

    .small-text {
      font-size: 0.875rem; /* = 14px */
    }
  </style>
</head>
<body>
  <h1>타이포그래피 예시</h1>
  <p>CSS에서 폰트를 어떻게 설정하는지가 전체적인 가독성과 분위기에 큰 영향을 준다.</p>
  <p class="highlight">글자 굵기나 색상으로 중요한 정보를 강조할 수 있다.</p>
  <p class="small-text">작은 글자로 푸터나 각주 같은 보조 정보를 표시한다.</p>
</body>
</html>

```

---

## 결론

타이포그래피는 **단순히 폰트를 고르는 것**을 넘어, **정보를 효과적으로 전달**하고 **사용자의 읽기 경험**을 최적화하는 작업이다.

다음 사항을 유의하자.

- **기본 속성**(font-family, size, weight, line-height 등)을 잘 이해하고 균형 있게 사용
- **웹 폰트**(Google Fonts, @font-face 등) 적용 시 로딩 성능과 라이센스 고려
- **반응형 타이포그래피**로 다양한 화면 크기에서도 일관된 가독성 유지
- **시인성, 대비(Contrast)** 등 접근성 측면도 함께 고민

적절한 폰트 선택과 세심한 스타일링은 페이지 전체의 **완성도**를 높이고, 사용자 경험을 풍부하게 만들어줄 것