# HTML 개요

HTML(HyperText Markup Language)은 웹페이지의 구조와 콘텐츠를 정의하는 마크업 언어이다

1991년 팀 버너스 리(Tim Berners-Lee)가 제안한 이후, 웹의 표준이 되어 발전을 거듭해왔다

브라우저는 HTML 문서를 해석해 화면에 표시하며, 이 과정을 통해 사용자는 웹페이지와 상호작용한다

## HTML의 특징

1. **구조와 의미 부여**
    
    HTML은 문서의 구조를 정의하는 동시에 요소(element)에 의미를 부여한다
    
    예를 들어 `<header>`는 문서의 머리말, `<nav>`는 내비게이션, `<section>`은 콘텐츠의 구분 등으로 사용된다
    
2. **레이아웃이 아닌 콘텐츠 중심**
    
    HTML은 콘텐츠가 어떤 의미를 갖는지를 나타내는 데 집중해야 한다
    
    디자인이나 배치는 주로 CSS를 통해 구현한다
    
3. **웹 표준 준수 중요성**
    
    HTML을 웹 표준에 맞춰 작성하면 다양한 브라우저와 플랫폼에서 일관성 있는 화면을 볼 수 있다
    
    접근성(Accessibility)과 검색엔진 최적화(SEO)에도 도움이 된다
    
4. **확장성과 호환성**
    
    HTML5가 등장하면서 최신 브라우저들의 기능을 활용할 수 있게 되었다
    
    오디오, 비디오, 캔버스, SVG 등의 미디어 요소를 별도 플러그인 없이 사용할 수 있다
    

## HTML 문서 예시

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>HTML 소개</title>
</head>
<body>
  <header>
    <h1>HTML 개요</h1>
  </header>

  <section>
    <h2>HTML이란 무엇인가</h2>
    <p>HTML은 웹페이지의 뼈대를 구성하는 마크업 언어이다</p>
  </section>

  <footer>
    <p>Copyright © 2024</p>
  </footer>
</body>
</html>

```

1. `<!DOCTYPE html>`은 HTML5 문서임을 선언하는 구문이다
2. `<html>` 태그는 문서의 최상위 요소이며, `lang="ko"`로 문서의 언어가 한국어임을 명시한다
3. `<head>` 요소에는 문서 메타정보, 제목(`<title>`), CSS나 스크립트 참조 등이 들어간다
4. `<body>` 요소에는 실제 화면에 표시될 콘텐츠를 작성한다
5. `<header>`, `<section>`, `<footer>`와 같은 태그는 HTML5에서 제공하는 시맨틱 태그이며, 문서를 의미 단위별로 구분한다

## 정리

HTML은 웹 개발의 출발점이며, 구조와 의미 부여에 집중해야 한다

CSS, JavaScript와 함께 사용되어 현대 웹을 구성하는 핵심 요소가 된다

반응형 디자인, 접근성, SEO 등을 고려하기 위해서는 HTML을 표준에 맞춰 정확히 작성하는 습관이 중요하다

# HTML 문서 구조

HTML 문서는 크게 **머리말(head)**과 **본문(body)** 부분으로 나뉜다

시작하기 전에 반드시 `<!DOCTYPE html>`을 통해 HTML5 문서임을 선언한다

## 문서의 기본 골격

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>문서 구조 예시</title>
</head>
<body>
  <h1>HTML 문서 구조</h1>
  <p>head와 body의 역할을 구분할 수 있다</p>
</body>
</html>
```

1. `<!DOCTYPE html>`: HTML5 문서임을 선언
2. `<html lang="ko">`: 문서 최상위 태그이며, `lang="ko"`로 문서가 한국어임을 지정
3. `<head>`: 문서의 정보를 담는 영역이다
    - `<meta charset="UTF-8">`: 문자의 인코딩 방식을 지정한다
    - `<title>`: 문서의 제목을 지정하며 브라우저 탭에 표시된다
    - `<link>`나 `<script>` 등을 통해 외부 파일을 불러올 수 있다
4. `<body>`: 실제 화면에 표시될 콘텐츠를 작성하는 영역이다
    - 텍스트, 이미지, 링크, 폼 등의 모든 요소가 이 안에 들어간다

## head 영역

- 문서 자체의 정보(메타데이터)를 정의하는 곳이다
- 검색엔진이나 소셜 미디어에서 문서를 인식하기 위한 정보가 주로 들어간다
- `<meta>`, `<title>`, `<link>`, `<script>` 태그 등을 포함한다

```html
<head>
  <meta charset="UTF-8">
  <meta name="description" content="HTML 문서 구조 정리">
  <meta name="keywords" content="HTML, 문서 구조, 웹개발">
  <meta name="author" content="홍길동">
  <title>문서 구조 예시</title>
  <link rel="stylesheet" href="styles.css">
  <script src="script.js"></script>
</head>
```

## body 영역

- 화면에 표시될 콘텐츠를 포함한다
- 텍스트, 이미지, 하이퍼링크, 시맨틱 태그 등이 사용된다
- `<header>`, `<main>`, `<footer>`와 같은 시맨틱 태그를 통해 구조를 명확히 할 수 있다

```html
<body>
  <header>
    <h1>HTML 문서 구조</h1>
    <nav>
      <ul>
        <li><a href="#section1">섹션 1</a></li>
        <li><a href="#section2">섹션 2</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <section id="section1">
      <h2>섹션 1</h2>
      <p>첫 번째 섹션의 내용이다</p>
    </section>

    <section id="section2">
      <h2>섹션 2</h2>
      <p>두 번째 섹션의 내용이다</p>
    </section>
  </main>

  <footer>
    <p>제작: 홍길동</p>
  </footer>
</body>
```

## 정리

HTML 문서 구조는 웹페이지의 뼈대를 결정한다

**head 영역**은 문서 정보를 정의하고, **body 영역**은 사용자에게 보이는 콘텐츠를 담는다

시맨틱 태그를 활용해 구조를 명확히 구성하면, 검색엔진과 접근성 측면에서도 유리하다